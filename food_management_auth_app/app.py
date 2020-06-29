from django.apps import AppConfig


class FoodManagementAuthAppAppConfig(AppConfig):
    name = "food_management_auth_app"

    def ready(self):
        from food_management_auth_app import signals # pylint: disable=unused-variable
