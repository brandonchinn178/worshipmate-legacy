from django.apps import AppConfig

class DatabaseConfig(AppConfig):
    name = 'database'
    verbose_name = "Database App"

    def ready(self):
        import database.signals
