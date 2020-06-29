from abc import ABC
from abc import abstractmethod
from datetime import datetime
from typing import List
from food_management.exceptions.exceptions import MealCourseDoesNotExist
from food_management.dtos.dtos import ItemAndQuantityDto
from food_management.constants.enums import TypeOfMeal, CourseType
from food_management.interactors.storages.dtos import (
    HomePageDto, SetMealPreferenceDto
)

class MealStorageInterface(ABC):

    @abstractmethod
    def check_date_if_exists(self, date_obj: datetime) -> bool:
        pass

    @abstractmethod
    def get_home_page(self, date_obj: datetime, user_id: int) -> HomePageDto:
        pass

    @abstractmethod
    def get_meal_preference(
            self, meal_id: int) -> SetMealPreferenceDto:
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

