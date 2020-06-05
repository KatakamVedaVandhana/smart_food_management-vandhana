from datetime import datetime
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface


class GetMealHeadCountInteractor:

    def __init__(self, presenter: PresenterInterface, meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_meal_head_count(self, meal_type: TypeOfMeal, date_obj: datetime):

        self._check_if_date_has_a_meal(date_obj=date_obj, meal_type=meal_type)
        head_count_dto = self.meal_storage.get_meal_head_count(
            meal_type=meal_type, date_obj=date_obj
        )
        response = self.presenter.get_meal_head_count_response(
            head_count_dto=head_count_dto
        )
        return response

    def _check_if_date_has_a_meal(self, date_obj, meal_type):
        is_date_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            date_obj=date_obj, meal_type=meal_type
        )
        is_date_not_having_a_meal = not is_date_having_a_meal
        if is_date_not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()
