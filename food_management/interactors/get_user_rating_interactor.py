from datetime import datetime
from food_management.constants.enums import TypeOfMeal
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.storages.storage_interface import \
    StorageInterface


class GetUserRatingInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            meal_storage:MealStorageInterface,
            storage: StorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage
        self.storage = storage

    def get_user_rating(self, meal_type: TypeOfMeal, user_id: int, date_obj:datetime):

        self._check_if_date_has_a_meal(meal_type=meal_type, date_obj=date_obj)

        meal_id = self.meal_storage.get_meal_id(meal_type=meal_type, date_obj=date_obj)

        is_user_has_a_rating = \
            self._check_if_user_has_a_rating(meal_id=meal_id, user_id=user_id)
        if is_user_has_a_rating:
            user_rating_dto = self.storage.get_user_rating(meal_id=meal_id, user_id=user_id)
            user_rating_dict = self.presenter.get_user_rating_response(
                user_rating_dto=user_rating_dto
            )
            return user_rating_dict

    def _check_if_date_has_a_meal(self, meal_type, date_obj):
        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        not_having_a_meal = not is_having_a_meal
        if not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()

    def _check_if_user_has_a_rating(self, meal_id, user_id):
        is_user_has_a_rating = self.storage.check_if_user_has_a_rating(
            meal_id=meal_id, user_id=user_id
        )
        is_user_not_have_rating = not is_user_has_a_rating
        if is_user_not_have_rating:
            return []
        return is_user_has_a_rating