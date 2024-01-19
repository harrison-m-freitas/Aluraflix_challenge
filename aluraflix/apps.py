from django.apps import AppConfig


class AluraflixConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluraflix'

    def ready(self) -> None:
        import aluraflix.signals
        return super().ready()