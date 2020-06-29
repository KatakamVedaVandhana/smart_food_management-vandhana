from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface


class GetItemsListInteractor:

    def __init__(self, meal_storage: MealStorageInterface, presenter: PresenterInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_items_list(self):

        items_list_dto = self.meal_storage.get_items_list()
        items_list = self.presenter.get_items_list_response(
            items_list_dto=items_list_dto
        )
        return items_list