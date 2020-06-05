from food_management.constants.enums import (
    CourseType, TypeOfMeal, CategoryType, UnitType,
    BaseUnitType
)
from datetime import time
from datetime import date
from typing import List, Optional
from dataclasses import dataclass
from food_management.dtos.dtos import ItemAndRatingDto

@dataclass
class UserRatingDto:
    items_and_ratings: List[ItemAndRatingDto]
    description: str

@dataclass
class UserDto:
    user_id: int
    username: str
    password: str


@dataclass
class MealCourseDto:
    meal_course: CourseType
    meal_id: int
    meal_type: TypeOfMeal

@dataclass
class ItemDto:
    item_id: int
    item: str
    category: CategoryType
    units: UnitType
    meal_id: Optional[int]


@dataclass
class MealDto:
    meal_id: int
    meal_type: TypeOfMeal
    date: date
    from_time_string: time
    to_time_string: time

@dataclass
class HomePageDto:
    meal: List[MealDto]
    meal_course: List[MealCourseDto]
    items: List[ItemDto]


@dataclass
class AnnouncementDtos:
    title: str
    subtitle: str
    description: str
    image: str


@dataclass
class MealCourseCompleteDetailsDto:
    item_id: int
    meal_course: CourseType
    quantity: int


@dataclass
class SetMealPreferenceDto:
    meal_course: List[MealCourseCompleteDetailsDto]
    items: List[ItemDto]


@dataclass
class MealScheduleDto:
    meal: MealDto
    items: List[ItemDto]


@dataclass
class MealCourseCountDto:
    meal_course: CourseType
    meal_course_count: int


@dataclass
class ItemsCountDto:
    item: str
    item_id: int
    item_count: str


@dataclass
class HeadCountDto:
    meal_course_count: List[MealCourseCountDto]
    items_count: List[ItemsCountDto]
    total_meal_head_count: int
    completed_meal_head_count: int


@dataclass
class ItemAndWastageDto:
    item_id: int
    item: str
    food_prepared: int
    food_wasted: int
    base_unit: BaseUnitType


@dataclass
class FoodWastageDto:
    food_wasted: int
    food_prepared: int
    base_unit: BaseUnitType
    items_and_wastage: List[ItemAndWastageDto]

