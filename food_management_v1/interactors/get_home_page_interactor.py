from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from datetime import date
from datetime import datetime

class HomePageInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_home_page(self, date_obj: datetime, user_id: int):

        valid_date = self.meal_storage.check_if_date_has_meals(
            date_obj=date_obj
        )
        not_a_valid_date = not valid_date
        if not_a_valid_date:
            self.presenter.raise_exception_for_invalid_date()

        home_page_dto = self.meal_storage.get_home_page(
            date_obj=date_obj, user_id=user_id
        )

        home_page_response = self.presenter.get_home_page_response(
            home_page_dto=home_page_dto
        )
        return home_page_response
