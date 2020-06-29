from django.apps import AppConfig


class FoodManagementAuthAppConfig(AppConfig):
    name = "food_management_auth"

    def ready(self):
        from food_management_auth import signals # pylint: disable=unused-variable
