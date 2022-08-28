from django.apps import AppConfig


class OpayListenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'opay_listen'

    def ready(self):
        import opay_listen.polling