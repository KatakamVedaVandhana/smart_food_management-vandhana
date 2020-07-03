from typing import List

from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.exceptions.exceptions import InvalidUserIds

class GetUserDtosInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_dtos(self, user_ids: List[int]):
        valid_user_ids = self.storage.get_user_ids()
        invalid_user_ids = [
            user_id
            for user_id in user_ids
            if user_id not in valid_user_ids
        ]
        if invalid_user_ids:
            raise InvalidUserIds
        else:
            user_dtos = self.storage.get_user_dtos(user_ids=user_ids)
        return user_dtos