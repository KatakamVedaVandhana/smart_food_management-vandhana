from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import \
    InvalidUsername, InvalidPassword
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from food_management.exceptions.exceptions import UserDoesNotExist

class LoginInteractor:
    def __init__(
            self, storage: StorageInterface,
            presenter: PresenterInterface, oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def login(self, username: str, password: str):

        try:
            self.storage.validate_username(username=username)
        except InvalidUsername:
            self.presenter.raise_exception_for_invalid_username()

        try:
            self.storage.validate_password(
                username=username, password=password
            )
        except InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()

        user_id, is_admin = self.storage.get_user_details(
            username=username, password=password
        )

        oauth_auth_user_tokens_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )

        token_dto = oauth_auth_user_tokens_service.create_user_auth_tokens(
            user_id=user_id
        )

        return self.presenter.login_user_details_response(token_dto, is_admin=is_admin)