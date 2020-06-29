from typing import List
from abc import abstractmethod
from abc import ABC

from food_management_auth.interactors.storages.dtos import UserDetailsDto

class StorageInterface(ABC):

    @abstractmethod
    def validate_user_ids(self, user_ids: List[int]) -> bool:
        pass

    def get_user_dtos(self, user_ids: List[int]) -> List[UserDetailsDto]:
        pass