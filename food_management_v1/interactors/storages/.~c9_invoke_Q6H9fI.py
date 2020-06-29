from food_management.constants.enums import (
    CourseType, TypeOfMeal, CategoryType, UnitType
)
from datetime import time
from datetime import date
from typing import List
from dataclasses import dataclass

@dataclass
class UserDto:
    user_id: int
    username: str
    password: str

@dataclass
class ItemDto:
    item_id: int
    item: str
    category: CategoryType
    units: UnitType
    meal_id: int

@dataclass
class MealDto:
    meal_id: int
    meal_type: TypeOfMeal
    date: date
    from_time_string: time
    to_time_string: time


@dataclass
class MealCourseDto:
    meal_course_id: int
    meal_course: CourseType
    meal_id: int


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
    meal_id: int
    meal_course: CourseType
    quantity: int
    meal_course_id: int


@dataclass
class SetMealPreferenceDto:
    meal_course: List[MealCourseCompleteDetailsDto]
    items: List[ItemDto]