from dataclasses import dataclass
from datetime import datetime
from typing import List
from food_management.constants.enums import TypeOfMeal, CourseType, RatingType

@dataclass
class ItemAndQuantityDto:
    item_id: int
    quantity: int


@dataclass
class CustomeMealUpdateDto:
    user_id: int
    date: datetime
    meal_type : TypeOfMeal
    #meal_id: int
    meal_course: CourseType
    items_and_quantities: List[ItemAndQuantityDto]


@dataclass
class ItemAndRatingDto:
    item_id: int
    quality: RatingType
    taste: RatingType


@dataclass
class RatingDto:
    user_id: int
    meal_type: TypeOfMeal
    date: datetime
    description: str
    items_and_ratings: List[ItemAndRatingDto]


@dataclass
class ItemDetailsDto:
    item_id : int
    meal_course : CourseType
    quantity: int


@dataclass
class UpdateMealScheduleDto:
    meal_type: TypeOfMeal
    date: datetime
    items: List[ItemDetailsDto]
