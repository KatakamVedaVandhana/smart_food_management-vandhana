from typing import List

from food_management.interactors.get_user_dtos import \
    GetUserDtosInteractor
from food_management.storages.storage_implementation import \
    StorageImplementation

class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = GetUserDtosInteractor(storage=storage)
        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos