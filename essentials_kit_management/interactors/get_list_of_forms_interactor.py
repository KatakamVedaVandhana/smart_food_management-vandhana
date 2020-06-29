from essesntials_kit_management.interactors.storages.storage_interface import \
    StorageInterface
from essesntials_kit_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetListOfFormsInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_list_of_forms(self, offset: int, limit: int, user_id: int):

        self._check_if_its_valid_offset(offset=offset)
        self._check_if_its_valid_limit(limit=limit)
        list_of_forms_dtos = self.storage.get_list_of_forms(
            offset=offset, limit=limit
        )

    def _check_if_its_valid_offset(self, offset):
        if offset < 0:
            raise self.presenter.raise_exception_for_invalid_offset()

    def _check_if_its_valid_limit(self, limit):
        if limit < 1:
            raise self.presenter.raise_exception_for_invalid_limit()

