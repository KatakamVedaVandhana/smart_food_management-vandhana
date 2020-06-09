from abc import ABC
from abc import abstractmethod
from datetime import datetime
from datetime import time
from typing import List
from food_management.dtos.dtos import ItemAndQuantityDto, UpdateMealScheduleDto
from food_management.constants.enums import TypeOfMeal, CourseType
from food_management.interactors.storages.dtos import (
    HomePageDto, SetMealPreferenceDto, MealScheduleDto, ItemDto, HeadCountDto,
    FoodWastageDto
)

class MealStorageInterface(ABC):

    @abstractmethod
    def check_if_date_has_meals(self, date_obj: datetime) -> bool:
        pass

    @abstractmethod
    def get_home_page(self, date_obj: datetime, user_id: int) -> HomePageDto:
        pass

    @abstractmethod
    def get_meal_preference(
            self, meal_id: int, user_id: int) -> SetMealPreferenceDto:
        pass

    @abstractmethod
    def check_if_its_valid_meal_id(self, meal_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_meal_course_if_user_has_a_meal(
            self,user_id: int, meal_id: int) -> CourseType:
        pass

    @abstractmethod
    def create_user_meal_status(
            self,user_id: int, meal_id: int, meal_course: CourseType):
        pass

    @abstractmethod
    def update_user_meal_status(
            self, meal_id: int, meal_course: CourseType,
            user_id: int):
        pass

    @abstractmethod
    def udpate_custom_meal_status(
            self, meal_id: int, meal_course: CourseType, user_id: int,
            items_and_quantities: List[ItemAndQuantityDto]):
        pass

    @abstractmethod
    def create_custom_meal_status(
            self, meal_id: int, meal_course: CourseType, user_id: int,
            items_and_quantities: List[ItemAndQuantityDto]):
        pass

    @abstractmethod
    def check_if_user_has_a_meal(
            self, meal_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def check_if_it_has_valid_item_ids_for_that_meal(
            self, items_ids: List[int],
            meal_id: int) -> bool:
        pass

    @abstractmethod
    def get_meal_schedule(self, date_obj: datetime, meal_type: TypeOfMeal) -> MealScheduleDto:
        pass

    @abstractmethod
    def get_meal_id(self, meal_type: TypeOfMeal, date_obj: datetime):
        pass

    @abstractmethod
    def get_items_list(self) -> List[ItemDto]:
        pass

    @abstractmethod
    def check_if_date_has_a_meal(
            self, date_obj: datetime, meal_type: TypeOfMeal) -> bool:
        pass

    @abstractmethod
    def create_meal_schedule(
            self, update_meal_schedule_dto: UpdateMealScheduleDto,
            from_time_string: time, to_time_string: time):
        pass

    @abstractmethod
    def check_if_item_exits(self, item_ids: List[int]) -> bool:
        pass

    @abstractmethod
    def update_meal_schedule(self, update_meal_schedule_dto: UpdateMealScheduleDto):
        pass

    @abstractmethod
    def get_meal_head_count(self, meal_type: TypeOfMeal, date_obj: datetime) -> HeadCountDto:
        pass

    @abstractmethod
    def get_food_wastage(self, meal_type: TypeOfMeal, date_obj: datetime) -> FoodWastageDto:
        pass