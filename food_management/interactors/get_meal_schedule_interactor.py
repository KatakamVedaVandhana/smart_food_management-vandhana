from datetime import datetime
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.constants.enums import TypeOfMeal
from food_management.constants.constants import (
    BREAKFAST_START_TIME, BREAKFAST_END_TIME, LUNCH_START_TIME,
    LUNCH_END_TIME, DINNER_START_TIME, DINNER_END_TIME
)

class GetMealScheduleInteractor:
    def __init__(self, presenter: PresenterInterface,
                meal_storage: MealStorageInterface):
        self.presenter = presenter
        self.meal_storage = meal_storage

    def get_meal_schedule(self, date_obj: datetime, meal_type: TypeOfMeal):
        is_having_a_meal = self.meal_storage.check_if_date_has_a_meal(
            date_obj=date_obj, meal_type=meal_type
        )
        if is_having_a_meal:
            meal_schedule_dto = self.meal_storage.get_meal_schedule(
                date_obj=date_obj, meal_type=meal_type
            )
            meal_schedule_list = self.presenter.get_meal_schedule_response(
                meal_schedule_dto=meal_schedule_dto
            )
            return meal_schedule_list
        else:
            meal_schedule_list = []
            return meal_schedule_list
