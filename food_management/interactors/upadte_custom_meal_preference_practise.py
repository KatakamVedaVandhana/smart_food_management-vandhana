from typing import List
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.dtos.dtos import UpdateCustomMealPreferenceDto
from food_management.exceptions.exceptions import (
    InvalidMealId, InvalidItemIds, DuplicateItemIds
)

class UpdateCustomMealPreferenceInteractor:

    def __init__(self, meal_storage: MealStorageInterface):
        self.meal_storage = meal_storage

    def udpate_user_custom_meal_preference_wrapper(self,
                                              presenter: PresenterInterface,
                                              update_custom_meal_preference_dto: UpdateCustomMealPreferenceDto):
        try:
            self.update_user_custom_meal_preference(
                update_custom_meal_preference_dto=update_custom_meal_preference_dto
                )

        except InvalidMealId:
            presenter.raise_exception_for_invalid_meal_id()

        except InvalidItemIds:
            presenter.raise_exception_for_invalid_item_ids()

        except DuplicateItemIds:
            presenter.raise_exception_for_duplicate_item_ids()



    def update_user_custom_meal_preference(self,
                                           update_custom_meal_preference_dto: UpdateCustomMealPreferenceDto):
        meal_id = update_custom_meal_preference_dto.meal_id
        user_id = update_custom_meal_preference_dto.user_id
        items_and_quantities = update_custom_meal_preference_dto.items_and_quantities

        # TODO - Check valid meal id
        self._validate_meal_id(meal_id=meal_id)

        items_ids_list = [
            item_and_quantity.item_id for item_and_quantity in items_and_quantities
        ]
        quantities_list = [
            item_and_quantity.quantity for item_and_quantity in items_and_quantities
        ]

        # TODO - Check valid items
        # i) valid item  like all are positive
        self._check_if_items_are_positive(items_ids_list)

        # TODO - Check valid items
        # iii) no duplication
        self._check_if_items_are_unique(items_ids_list)

        # TODO - Check valid items
        # ii) valid item for that meal

    def _validate_meal_id(self, meal_id: int):

        is_valid_meal_id = self.meal_storage.check_if_its_valid_meal_id(meal_id=meal_id)
        not_a_valid_meal_id = not is_valid_meal_id

        if not_a_valid_meal_id:
            raise InvalidMealId

    def _check_if_items_are_positive(self, items_ids_list: List[int]):

        is_positive_item_ids = all(item_id > 0 for item_id in items_ids_list)
        not_positive_item_ids = not is_positive_item_ids
        
        if not_positive_item_ids:
            raise InvalidItemIds

    def _check_if_items_are_unique(self, items_ids_list: List[int]):

        unique_item_ids_list = list(set(items_ids_list))
        is_unique_item_ids = sorted(items_ids_list) == sorted(unique_item_ids_list)
        not_unique_item_ids = not is_unique_item_ids
        if not_unique_item_ids:
            raise DuplicateItemIds


# TODO - Check valid items
        # i) valid item  like all are positive
        # ii) valid item for that meal
        # iii) no duplication
# TODO - Check quantities
# TODO - If user has a meal or not 
        # i) if yes update
        # ii) else create