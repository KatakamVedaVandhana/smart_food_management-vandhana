from django_swagger_utils.drf_server.exceptions import NotFound

from food_management_auth_app.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management_auth_app.constants.exception_messages import INVALID_USERNAME
from food_management_auth_app.constants.exception_messages import INVALID_PASSWORD

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self):
        return NotFound(INVALID_USERNAME)

    def raise_exception_for_invalid_password(self):
        return NotFound(INVALID_PASSWORD)

