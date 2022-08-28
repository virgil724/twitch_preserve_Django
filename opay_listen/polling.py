from django_apscheduler.jobstores import DjangoJobStore
from lib2to3.pgen2.token import OP
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Donate_data, Opay
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import requests
import re

sch = BackgroundScheduler()


def opay_job(link, twitchId):
    s = requests.Session()

    url = "https://payment.opay.tw/Broadcaster/AlertBox/"+link

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'}

    response = s.request("GET", url, headers=headers)

    token = re.findall(
        "(value=)(.*)", response.text)[0][1].split()[0].replace('"', '')
    url = "https://payment.opay.tw/Broadcaster/CheckDonate/"+link

    payload = {
        "__RequestVerificationToken": token
    }
    headers = {
        'content-type': "application/x-www-form-urlencoded;charset=utf-8",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
    }

    response = s.request("POST", url, data=payload, headers=headers)
    if (response.status_code == 200):
        data_list = response.json()["lstDonate"]
        [Donate_data(twitchId=twitchId, donateId=data['donateid'], name=data['name'], amount=data['amount'], msg=data['msg']).save()
            for data in data_list]
        # bulk=Donate_data.objects.bulk_create([Donate_data(**{
        #     'donateId': data['donateid'],
        #     'name':data['name'],
        #     'amount':data['amount'],
        #     'msg':data['msg']
        # })
        #     for data in data_list])
        # bulk.save()
    else:
        sch.remove_job(link)


def ecpay(link,twitchId):

    url = "https://payment.ecpay.com.tw/Broadcaster/CheckDonate/"+link

    headers = {
        'content-type': "application/x-www-form-urlencoded;charset=utf-8",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
    }

    response = requests.request("POST", url, headers=headers)
    if (response.status_code == 200):
        data_list=response.json()
        [Donate_data(twitchId=twitchId, donateId=data['donateid'], name=data['name'],
                     amount=data['amount'], msg=data['msg']).save()for data in data_list]
        pass


@receiver(post_save, sender=Opay)
def create_schedule_task(sender, instance: Opay, created, **kwargs):
    if instance.opay_link != None:
        link = instance.opay_link.split("/")[-1]
        sch.add_job(opay_job, trigger=CronTrigger(
            second="*/5"), args=[link, instance.twitchId], id=link)
    if instance.ecpay_link != None:
        link = instance.ecpay_link.split("/")[-1]
        sch.add_job(ecpay, trigger=CronTrigger(
            second="*/5"), args=[link, instance.twitchId], id=link)

    pass


@receiver(post_delete, sender=Opay)
def del_schedule_task(sender, instance: Opay, **kwargs):
    link = instance.opay_link.split("/")[-1]
    sch.remove_job(link)

sch.add_jobstore(DjangoJobStore(), "default")
sch.start()


@receiver(post_save, sender=Donate_data)
def notify_twitch(sender, instance: Donate_data, created, **kwargs):
    print(instance.__dict__)
    pass
