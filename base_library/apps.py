from django.apps import AppConfig


class BaseLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_library'
