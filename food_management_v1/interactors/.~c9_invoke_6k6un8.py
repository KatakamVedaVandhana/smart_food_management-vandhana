from datetime import date
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class SetMealPreferenceInteractor:

    def __init__(
            self, meal_storage:MealStorageInterface,
            presenter: PresenterInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def set_meal_preference(self, meal_type: TypeOfMeal, date_obj: date):
        try:
            self.meal_storage.

        is_valid_date = self.meal_storage.check_date_if_exists(
            date_obj=date_obj
        )
        not_a_valid_date = not is_valid_date
        if not_a_valid_date:
            self.presenter.raise_exception_for_invalid_date()

        meal_data_dto = self.meal_storage.set_meal_preference(
            meal_type=meal_type, date_obj=date_obj
        )
        response = self.presenter.set_meal_preference_response(
            meal_data_dto=meal_data_dto
        )
        return response
