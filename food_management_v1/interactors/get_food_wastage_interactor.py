from datetime import datetime
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetFoodWastageInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            meal_storage:MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_food_wastage(self, meal_type: TypeOfMeal, date_obj: datetime):

        self._check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )

        food_wastage_dto = self.meal_storage.get_food_wastage(
            meal_type=meal_type, date_obj=date_obj
        )

        food_wastage_dict = self.presenter.get_food_wastage_response(
            food_wastage_dto=food_wastage_dto
        )

        return food_wastage_dict

    def _check_if_date_has_a_meal(self, meal_type, date_obj):
        is_date_having_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        is_date_not_having_a_meal = not is_date_having_meal
        if is_date_not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()