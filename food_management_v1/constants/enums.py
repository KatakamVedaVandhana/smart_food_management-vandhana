import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"


class CategoryType(BaseEnumClass, enum.Enum):
    indian_bread = "Indian-Bread"
    curry = "Curry"
    rice = "Rice"


class UnitType(BaseEnumClass, enum.Enum):
    pieces = "pieces"
    cups = "cups"
    laddles = "laddles"


class TypeOfMeal(BaseEnumClass, enum.Enum):
    breakfast = "Breakfast"
    lunch = "Lunch"
    dinner = "Dinner"


class CourseType(BaseEnumClass, enum.Enum):
    half_meal = 'Half-meal'
    full_meal = 'Full-meal'
    custom_meal = 'Custom-meal'
    skip_meal = 'Skip-meal'


class RatingType(BaseEnumClass, enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

class BaseUnitType(BaseEnumClass, enum.Enum):
    pieces = 'pieces'
    kilogram = 'kg'
