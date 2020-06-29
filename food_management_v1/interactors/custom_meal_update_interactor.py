from typing import List
from datetime import date
from food_management.exceptions.exceptions import ItemDoesNotExist
from food_management.constants.enums import TypeOfMeal
from food_management.dtos.dtos import CustomeMealUpdateDto
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class CustomeMealUpdateInteractor:

    def __init__(
            self, meal_storage: MealStorageInterface,
            presenter: PresenterInterface):
        self.meal_storage = meal_storage
        self.presenter = presenter

    def custom_meal_update(self, custom_meal_udpate_dto: CustomeMealUpdateDto):

        user_id = custom_meal_udpate_dto.user_id
        meal_type = custom_meal_udpate_dto.meal_type
        self._check_is_valid_meal_type(meal_type)

        date_obj = custom_meal_udpate_dto.date
        self._check_if_date_has_a_meal(date_obj)

        meal_items_and_quantities = custom_meal_udpate_dto.items_and_quantities
        self._check_if_its_valid_items_for_that_meal(
            meal_items_and_quantities, meal_type, date_obj
        )

        is_having_a_meal = self.meal_storage.check_meal_status_of_the_user(
            meal_type=meal_type, date_obj=date_obj, user_id=user_id)
        if is_having_a_meal:
            self.meal_storage.update_custom_user_meal_status(
                meal_type=meal_type, meal_items_and_quantities=meal_items_and_quantities,
                date_obj=date_obj, user_id=user_id
            )
        else:
            self.meal_storage.create_user_custom_meal_status(
                meal_type=meal_type,
                meal_items_and_quantities=meal_items_and_quantities,
                date_obj=date_obj, user_id=user_id
            )

    def _check_is_valid_meal_type(self, meal_type):

        try:
            TypeOfMeal(meal_type)
        except ValueError:
            self.presenter.raise_exception_for_invalid_meal_type()

    def _check_if_date_has_a_meal(self, date_obj):
        is_valid_date = self.meal_storage.check_date_if_exists(date_obj=date_obj)
        not_a_valid_date = not is_valid_date
        if not_a_valid_date:
            self.presenter.raise_exception_for_invalid_date()

    def _check_if_its_valid_items_for_that_meal(
            self, meal_items_and_quantities, meal_type, date_obj):
        item_ids_list = []
        for meal_item_and_quantity in meal_items_and_quantities:
            item_ids_list.append(meal_item_and_quantity.item_id)

        
        valid_item_ids = self.meal_storage.is_valid_item_ids(
            item_ids_list=item_ids_list, date_obj=date_obj, meal_type=meal_type)
        not_valid_item_ids = not valid_item_ids
        if not_valid_item_ids:
            self.presenter.raise_exception_for_invalid_item_id()

        return item_ids_list
