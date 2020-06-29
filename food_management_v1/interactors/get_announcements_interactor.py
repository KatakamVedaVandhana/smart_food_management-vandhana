from datetime import datetime
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetAnnouncementsInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_announcements(self, date_obj: datetime):

        announcement_dtos = self.storage.get_announcements(date_obj=date_obj)
        response = self.presenter.get_announcements_response(
            announcement_dtos=announcement_dtos
        )
        return response
