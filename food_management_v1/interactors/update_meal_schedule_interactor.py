from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.constants.enums import TypeOfMeal
from food_management.constants.constants import (
    BREAKFAST_END_TIME, BREAKFAST_START_TIME, LUNCH_END_TIME,
    LUNCH_START_TIME, DINNER_END_TIME, DINNER_START_TIME
)
from food_management.dtos.dtos import UpdateMealScheduleDto


class UpdateMealScheduleInteractor:

    def __init__(self, presenter: PresenterInterface, meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def update_meal_schedule(self, update_meal_schedule_dto: UpdateMealScheduleDto):

        items = update_meal_schedule_dto.items
        self._check_if_item_ids_exists(items=items)

        meal_type = update_meal_schedule_dto.meal_type
        date_obj = update_meal_schedule_dto.date
        is_having_a_meal = self._check_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )

        if is_having_a_meal:
            self.meal_storage.update_meal_schedule(
                update_meal_schedule_dto=update_meal_schedule_dto
            )
            return
        else:
            print(meal_type)
            from_time_string, to_time_string = self._check_meal_type(meal_type)
            self.meal_storage.create_meal_schedule(
                from_time_string=from_time_string,
                to_time_string=to_time_string,
                update_meal_schedule_dto=update_meal_schedule_dto
            )

    def _check_date_has_a_meal(self, meal_type, date_obj):
        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            meal_type=meal_type, date_obj=date_obj
        )
        return is_having_a_meal

    def _check_if_item_ids_exists(self, items):
        item_ids_list = {item.item_id for item in items}
        is_valid_item_ids = self.meal_storage.check_if_item_exits(item_ids=item_ids_list)
        not_is_valid_items = not is_valid_item_ids
        if not_is_valid_items:
            self.presenter.raise_exception_for_invalid_item_id()

    def _check_meal_type(self, meal_type):
 
        is_breakfast_type = meal_type == TypeOfMeal.breakfast.value
        if is_breakfast_type:
            from_time_string = BREAKFAST_START_TIME
            to_time_string = BREAKFAST_END_TIME

        is_lunch_type = meal_type == TypeOfMeal.lunch.value
        if is_lunch_type:
            from_time_string = LUNCH_START_TIME
            to_time_string = LUNCH_END_TIME

        is_dinner_type = meal_type == TypeOfMeal.dinner.value
        if is_dinner_type:
            from_time_string = DINNER_START_TIME
            to_time_string = DINNER_END_TIME

        return from_time_string, to_time_string