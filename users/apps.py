from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # django docs. recommend to do it this way, to avoid the side effects of how imports work
        import users.signals
