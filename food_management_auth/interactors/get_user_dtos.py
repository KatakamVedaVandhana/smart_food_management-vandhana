from typing import List

from food_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from food_management_auth.interactors.presenters.presenter_interface import\
    PresenterInterface
from food_management_auth.exceptions.exceptions import InvalidUserIds

class GetUserDtosInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_dtos_wrapper(self, presenter: PresenterInterface, user_ids: List[int]):

        try:
            return self._get_user_dtos(user_ids=user_ids, presenter=presenter)
        except InvalidUserIds:
            presenter.raise_exception_for_invalid_user_ids()

    def _get_user_dtos(self, user_ids: List[int], presenter: PresenterInterface):
        user_dtos = self.get_user_dtos(user_ids=user_ids)
        return presenter.get_user_dtos_response(user_dtos=user_dtos)

    def get_user_dtos(self, user_ids: List[int]):

        #TODO check valid user ids
        self._validate_user_ids(user_ids=user_ids)

        #get user dto from storage
        user_dtos = self.storage.get_user_dtos(user_ids=user_ids)
        return user_dtos

    def _validate_user_ids(self, user_ids):

        print("hi")
        is_valid_user_ids = self.storage.validate_user_ids(user_ids=user_ids)
        print(is_valid_user_ids)
        not_a_valid_user_ids = not is_valid_user_ids
        if not_a_valid_user_ids:
            raise InvalidUserIds
