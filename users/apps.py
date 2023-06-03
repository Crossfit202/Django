from django.apps import AppConfig


class UsersConfig(AppConfig):
    # Set the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the app
    name = 'users'