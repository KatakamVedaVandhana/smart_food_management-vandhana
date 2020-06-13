from django.apps import AppConfig


class EssesntialsKitManagementAppConfig(AppConfig):
    name = "essesntials_kit_management"

    def ready(self):
        from essesntials_kit_management import signals # pylint: disable=unused-variable
