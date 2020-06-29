from abc import abstractmethod
from abc import ABC

from typing import List

from food_management_auth.interactors.storages.dtos import UserDetailsDto

class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_user_ids(self):
        pass

    @abstractmethod
    def get_user_dtos_response(self, user_dtos: List[UserDetailsDto]):
        pass