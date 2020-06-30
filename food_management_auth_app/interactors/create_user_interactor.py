from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class CreateUserInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_user(self, username: str, password: str):

        is_existing_user = self.storage.check_if_user_exists(
            username, password
        )

        if is_existing_user:
            self.presenter.raise_exception_if_user_exists()

        else:
            self.storage.create_user(username, password)
