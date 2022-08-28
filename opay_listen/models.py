from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Opay(models.Model):
    opay_link = models.CharField(max_length=100, null=True,help_text="填入Opay贊助動畫連結")
    ecpay_link = models.CharField(max_length=100, null=True,help_text="填入ecpay贊助動畫連結")
    twitchId = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    # owner= models.CharField(max_length=200)
    # owner =


class Donate_data(models.Model):
    twitchId = models.ForeignKey(
        get_user_model(), max_length=100, on_delete=models.CASCADE)
    donateId = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=40)
    amount = models.DecimalField(decimal_places=0, max_digits=10)
    msg = models.TextField()
