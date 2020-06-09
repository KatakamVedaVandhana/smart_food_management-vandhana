from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.dtos.dtos import RatingDto

class UpdateUserRatingInteractor:

    def __init__(self, presenter: PresenterInterface,
                 storage: StorageInterface,
                 meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.storage = storage
        self.meal_storage = meal_storage

    def update_user_rating(self, rating_dto: RatingDto):

        meal_type = rating_dto.meal_type
        date_obj = rating_dto.date

        self._check_if_date_has_a_meal(meal_type=meal_type, date_obj=date_obj)

        meal_id = self.meal_storage.get_meal_id(meal_type=meal_type, date_obj=date_obj)


        user_id = rating_dto.user_id

        items_and_ratings = rating_dto.items_and_ratings
        self._check_if_it_has_valid_item_ids_for_that_meal(
            items_and_ratings=items_and_ratings,
            meal_id=meal_id
        )
        is_user_has_a_rating = self._check_if_user_have_a_rating_for_that_meal(
            meal_id=meal_id, user_id=user_id
        )
        if is_user_has_a_rating:
            self.storage.update_user_rating(rating_dto=rating_dto)
        else:
            self.storage.create_user_rating(rating_dto=rating_dto)

    def _check_if_date_has_a_meal(self, meal_type, date_obj):
        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        not_having_a_meal = not is_having_a_meal
        if not_having_a_meal:
            self.presenter.raise_exception_for_invalid_date_for_that_meal()
        return is_having_a_meal

    def _check_if_it_has_valid_item_ids_for_that_meal(
            self, items_and_ratings, meal_id):
        items_ids = [item.item_id for item in items_and_ratings]
        valid_item_ids = self.meal_storage.check_if_it_has_valid_item_ids_for_that_meal(
            items_ids=items_ids, meal_id=meal_id
        )
        not_valid_items = not valid_item_ids
        if not_valid_items:
            self.presenter.raise_exception_for_invalid_item_id()

    def _check_if_user_have_a_rating_for_that_meal(self, user_id, meal_id):
        is_user_has_a_rating = self.storage.check_if_user_has_a_rating(
            user_id=user_id, meal_id=meal_id
        )
        return is_user_has_a_rating