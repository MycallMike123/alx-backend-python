from django.apps import AppConfig

class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Django-Chat.Models'

    def ready(self):
        import Django-Chat.Models.signals

