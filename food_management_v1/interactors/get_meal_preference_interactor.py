from datetime import datetime
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class MealInteractor:

    def __init__(
            self, meal_storage:MealStorageInterface,
            presenter: PresenterInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_meal_preference(
            self, meal_type: TypeOfMeal, date_obj:datetime,
            user_id: int):

        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        if is_having_a_meal:
            meal_id = self.meal_storage.get_meal_id(
                meal_type=meal_type, date_obj=date_obj,
            )

        not_having_a_meal = not is_having_a_meal
        if not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()

        meal_data_dto = self.meal_storage.get_meal_preference(
           meal_id=meal_id, user_id=user_id
        )
        response = self.presenter.get_meal_preference_response(
            meal_data_dto=meal_data_dto
        )
        return response
