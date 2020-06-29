from datetime import datetime
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import DateHasNoMeal


class GetMealPreferenceInteractor:

    def __init__(self, meal_storage: MealStorageInterface):
        self.meal_storage = meal_storage

    def get_meal_preference_wrapper(self,
                                    presenter: PresenterInterface,
                                    meal_type: TypeOfMeal,
                                    date_obj: datetime):

        try:
            get_meal_preference_dto = self.get_meal_preference(
                meal_type=meal_type, date_obj=date_obj
            )

        except DateHasNoMeal:
            presenter.raise_exception_for_invalid_date_for_that_meal()

        presenter.get_meal_preference_response(
            meal_data_dto=get_meal_preference_dto
        )

    def get_meal_preference(self, meal_type: TypeOfMeal, date_obj: datetime):

        is_date_having_a_meal = self._check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        if is_date_having_a_meal:
            meal_id = self.meal_storage.get_meal_id(
                meal_type=meal_type, date_obj=date_obj
            )

        get_meal_preference_dto = self.meal_storage.get_meal_preference(
            meal_id=meal_id
        )

        return get_meal_preference_dto

    def _check_if_date_has_a_meal(self, meal_type, date_obj):

        is_date_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type, date_obj
        )

        is_date_not_having_a_meal = not is_date_having_a_meal

        if is_date_not_having_a_meal:
            raise DateHasNoMeal

        return is_date_having_a_meal

