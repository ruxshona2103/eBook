from django.apps import AppConfig


class EbookAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ebook_app'

    def ready(self):
        import ebook_app.signals
