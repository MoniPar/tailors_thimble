from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        Overrides the ready() method of the UsersConfig class to
        perform an initialisation task which is registering signals
        """
        import users.signals
