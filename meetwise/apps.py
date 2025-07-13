from django.apps import AppConfig


class MeetwiseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meetwise'

    def ready(self):
        import meetwise.signals 