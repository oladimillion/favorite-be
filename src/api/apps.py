from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    label = 'api'
    verbose_name = 'api'

    def ready(self):
        import api.signals
