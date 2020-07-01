from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def login_user_details_response(self, token_dto: UserAuthTokensDTO, is_admin):
        pass