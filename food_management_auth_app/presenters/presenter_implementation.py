from django_swagger_utils.drf_server.exceptions import NotFound

from food_management_auth_app.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management_auth_app.constants.exception_messages import INVALID_USERNAME
from food_management_auth_app.constants.exception_messages import INVALID_PASSWORD
from common.dtos import UserAuthTokensDTO

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self):
        raise NotFound(INVALID_USERNAME)

    def raise_exception_for_invalid_password(self):
        raise NotFound(INVALID_PASSWORD)

    def login_user_details_response(self, token_dto: UserAuthTokensDTO, is_admin:bool):
        response_dict = {
            "user_id": token_dto.user_id,
            "access_token": token_dto.access_token,
            "refresh_token": token_dto.refresh_token,
            "expires_in": str(token_dto.expires_in),
            "is_admin": is_admin
        }
        return response_dict