from abc import ABC
from abc import abstractmethod
from typing import List

from food_management_auth_app.interactors.storages.dtos import UserDetailsDto

class StorageInterface(ABC):

    @abstractmethod
    def get_user_ids(self):
        pass

    @abstractmethod
    def get_user_dtos(self, user_ids: List[int]) -> List[UserDetailsDto]:
        pass
