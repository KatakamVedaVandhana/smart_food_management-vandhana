import pytest
import re
from freezegun import freeze_time
from dataclasses import dataclass
from typing import Pattern
from django.utils import timezone
from datetime import datetime
from datetime import time
from common.dtos import UserAuthTokensDTO
from food_management.constants.constants import DEFAULT_TIME_FORMAT
from food_management.constants.enums import (
    TypeOfMeal, CourseType, UnitType, CategoryType
)
from food_management.interactors.storages.dtos import (
    MealDto, ItemDto, MealCourseDto, HomePageDto, AnnouncementDtos,
    SetMealPreferenceDto, MealCourseCompleteDetailsDto, MealScheduleDto,
    UserRatingDto, ItemAndWastageDto, FoodWastageDto
)
from food_management.dtos.dtos import ItemAndRatingDto

@pytest.fixture
@freeze_time('2020-02-12')
def user_auth_token_dto():
    user_id = 1
    access_token = '125'
    refresh_token = '521'
    expires_in = str(timezone.now())
    user_auth_token_dto = UserAuthTokensDTO(
        user_id=user_id, access_token=access_token,
        refresh_token=refresh_token, expires_in=expires_in
    )
    return user_auth_token_dto

@pytest.fixture
@freeze_time('2020-02-12')
def login_details_response_dict():
    response_dict = {
        "user_id": 1,
        "access_token": '125',
        "refresh_token": '521',
        'expires_in': str(timezone.now()),
        'is_admin': False
    }
    return response_dict


@pytest.fixture
@freeze_time('2020-02-12')
def meal_dtos():
    meal_dtos_list = [
        MealDto(
            meal_id=1, meal_type=TypeOfMeal.breakfast.value,
            date=timezone.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        ),
        MealDto(
            meal_id=2, meal_type=TypeOfMeal.lunch.value,
            date=timezone.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        ),
        MealDto(
            meal_id=3, meal_type=TypeOfMeal.dinner.value,
            date=timezone.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        )
        ]
    return meal_dtos_list

@pytest.fixture
def item_dtos():
    item_dtos_list = [
        ItemDto(
            item_id=1, item='Idly', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=2, item='Poori', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=3, item='MasalaRice', category=CategoryType.rice.value,
            units=UnitType.laddles.value, meal_id=1
        ),
        ItemDto(
            item_id=4, item='WhiteRice', category=CategoryType.rice.value,
            units=UnitType.laddles.value, meal_id=2
        ),
        ItemDto(
            item_id=5, item='Dal', category=CategoryType.curry.value,
            units=UnitType.cups.value, meal_id=2
        ),
        ItemDto(
            item_id=6, item='PotatoCurry', category=CategoryType.curry.value,
            units=UnitType.cups.value, meal_id=2
        ),
        ItemDto(
            item_id=7, item='Curd', category=CategoryType.curry.value,
            units=UnitType.cups.value, meal_id=2
        ),
        ItemDto(
            item_id=8, item='Roti', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=3
        ),
        ItemDto(
            item_id=9, item='Rajma', category=CategoryType.curry.value,
            units=UnitType.cups.value, meal_id=3
        ),
        ItemDto(
            item_id=10, item='FriedRice', category=CategoryType.rice.value,
            units=UnitType.laddles.value, meal_id=3
        )
    ]
    return item_dtos_list


@pytest.fixture
def meal_course_dtos():
    meal_course_dtos_list = [
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
            meal_id=1, meal_type=TypeOfMeal.breakfast.value
        ),
        MealCourseDto(
            meal_course=CourseType.full_meal.value,
            meal_id=2, meal_type=TypeOfMeal.lunch.value
        ),
        MealCourseDto(
            meal_course=CourseType.full_meal.value,
            meal_id=3, meal_type=TypeOfMeal.dinner.value
        )
    ]
    return meal_course_dtos_list



@pytest.fixture
def home_page_dto(meal_course_dtos, meal_dtos, item_dtos):
    return HomePageDto(
        meal_course=meal_course_dtos,
        items=item_dtos,
        meal=meal_dtos
    )

@pytest.fixture
@freeze_time('2020-02-12')
def home_page_response_dict():
    response_list = [
        {
            'meal_id': 1,
            'meal_type': 'Breakfast',
            'items': [
                {
                    'item_id': 1,
                    'item': 'Idly',
                    'units': 'pieces',
                    'category': 'Indian-Bread'
                },
                {
                    'item_id': 2,
                    'item': 'Poori',
                    'units': 'pieces',
                    'category': 'Indian-Bread'
                },
                {
                    'item_id': 3,
                    'item': 'MasalaRice',
                    'units': 'laddles',
                    'category': 'Rice'
                },
            ],
            'from_time_string': '00:00',
            'to_time_string': '00:00',
            'meal_course': 'Half-meal'
        },
        {
            'meal_id': 2,
            'meal_type': 'Lunch',
            'items': [
                {
                    'item_id': 4,
                    'item': 'WhiteRice',
                    'units': 'laddles',
                    'category': 'Rice'
                },
                {
                    'item_id': 5,
                    'item': 'Dal',
                    'units': 'cups',
                    'category': 'Curry'
                },
                {
                    'item_id': 6,
                    'item': 'PotatoCurry',
                    'units': 'cups',
                    'category': 'Curry'
                },
                {
                    'item_id': 7,
                    'item': 'Curd',
                    'units': 'cups',
                    'category': 'Curry'
                }
            ],
            'from_time_string': '00:00',
            'to_time_string': '00:00',
            'meal_course': 'Full-meal'
        },
        {
            'meal_id': 3,
            'meal_type': 'Dinner',
            'items': [
                {
                    'item_id': 8,
                    'item': 'Roti',
                    'units': 'pieces',
                    'category': 'Indian-Bread'
                },
                {
                    'item_id': 9,
                    'item': 'Rajma',
                    'units': 'cups',
                    'category': 'Curry'
                },
                {
                    'item_id': 10,
                    'item': 'FriedRice',
                    'units': 'laddles',
                    'category': 'Rice'
                }
            ],
            'from_time_string': '00:00',
            'to_time_string': '00:00',
            'meal_course': 'Full-meal'
        }
    ]
    return response_list

@pytest.fixture
def meal_data_response_dict():
    meal_list = [
        {
            "item_id": 1,
            "item": "Idly",
            "category": "Indian-Bread",
            "units": "pieces",
            "meal_courses": [
                {
                    "meal_course": "Half-meal",
                    "quantity": 2
                },
                {
                    "meal_course": "Full-meal",
                    "quantity": 3
                }
            ]
        },
        {
            "item_id": 2,
            "item": "Poori",
            "category": "Indian-Bread",
            "units": "pieces",
            "meal_courses": [
                {
                    "meal_course": "Half-meal",
                    "quantity": 2
                },
                {
                    "meal_course": "Full-meal",
                    "quantity": 3
                }
            ]
        },
        {
            "item_id": 3,
            "item": "MasalaRice",
            "category": "Rice",
            "units": "laddles",
            "meal_courses": [
                {
                    "meal_course": "Half-meal",
                    "quantity": 1
                },
                {
                    "meal_course": "Full-meal",
                    "quantity": 3
                }
            ]
        }
    ]
    return meal_list

@pytest.fixture
def announcement_dtos():
    announcement_dtos_list = [
        AnnouncementDtos(
            title='Birthday Special!',
            subtitle='Special Item added',
            description='on the occasion of our friend birthday \
                         a new meal has been added',
            image='https://www.pexels.com/search/flower/'
        ),
        AnnouncementDtos(
            title='Festival Special!',
            subtitle='Special Item added',
            description='on the occasion of our ramzan \
                         a new meal has been added',
            image='https://www.pexels.com/search/flower/'
        ),
        AnnouncementDtos(
            title='Event Special!',
            subtitle='Special Item added',
            description='on the occasion of our college fest \
                         a new meal has been added',
            image='https://www.pexels.com/search/flower/'
        )
        ]
    return announcement_dtos_list

@pytest.fixture
def announcement_response_list():
    announcement_list = [
        {
            "title": "Birthday Special!",
            "subtitle": "Special Item added",
            "description": "on the occasion of our friend birthday \
                         a new meal has been added",
            "image": "https://www.pexels.com/search/flower/",
        },
        {
            "title": "Festival Special!",
            "subtitle": "Special Item added",
            "description": "on the occasion of our ramzan \
                         a new meal has been added",
            "image": "https://www.pexels.com/search/flower/",
        },
        {
            "title": "Event Special!",
            "subtitle": "Special Item added",
            "description": "on the occasion of our college fest \
                         a new meal has been added",
            "image": "https://www.pexels.com/search/flower/",
        }
    ]
    return announcement_list

@pytest.fixture
def meal_items_dtos():
    item_dtos_list = [
        ItemDto(
            item_id=1, item='Idly', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=2, item='Poori', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=3, item='MasalaRice', category=CategoryType.rice.value,
            units=UnitType.laddles.value, meal_id=1
        )
    ]
    return item_dtos_list


@pytest.fixture
def meal_course_complete_details_dtos():
    meal_course_details_list = [
        MealCourseCompleteDetailsDto(
            item_id=1, meal_course=CourseType.half_meal.value, quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=2, meal_course=CourseType.half_meal.value, quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=3, meal_course=CourseType.half_meal.value, quantity=1
        ),
        MealCourseCompleteDetailsDto(
            item_id=1, meal_course=CourseType.full_meal.value, quantity=3
        ),
        MealCourseCompleteDetailsDto(
            item_id=2, meal_course=CourseType.full_meal.value, quantity=3
        ),
        MealCourseCompleteDetailsDto(
            item_id=3, meal_course=CourseType.full_meal.value, quantity=3
        )
    ]
    return meal_course_details_list

@pytest.fixture
def meal_data_dtos(meal_course_complete_details_dtos, meal_items_dtos):
    return SetMealPreferenceDto(
        meal_course=meal_course_complete_details_dtos,
        items=meal_items_dtos
    )

@pytest.fixture
def breakfast_items():
    item_dtos = [
        ItemDto(
            item_id=1, item='Idly', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=2,item='Poori', category=CategoryType.indian_bread.value,
            units=UnitType.pieces.value, meal_id=1
        ),
        ItemDto(
            item_id=3,item='MasalaRice', category=CategoryType.rice.value,
            units=UnitType.laddles.value, meal_id=1
        )
    ]
    return item_dtos

@pytest.fixture
@freeze_time('2020-02-12')
def meal_breakfast_dto():
    datetime_obj = datetime(20,2,12)
    return MealDto(
            meal_id=1, meal_type=TypeOfMeal.breakfast.value,
            date=datetime.now(),
            from_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            to_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        )

@pytest.fixture
def meal_schedule_dto(breakfast_items, meal_breakfast_dto):
    return MealScheduleDto(
        items=breakfast_items,
        meal=meal_breakfast_dto
    )

@pytest.fixture
@freeze_time('2020-02-12')
def meal_schedule_dict():
    schedule_dict = {
            "meal_type": "Breakfast",
            "meal_id": 1,
            "date": datetime.now(),
            "items_list":[
                {
                    "item_id":1,
                    "item": "Idly",
                    "category": "Indian-Bread",
                    "units": "pieces"
                },
                {
                    "item_id":2,
                    "item": "Poori",
                    "category": "Indian-Bread",
                    "units": "pieces"
                },
                {
                    "item_id":3,
                    "item": "MasalaRice",
                    "category": "Rice",
                    "units": "laddles"
                }
                ]
        }
    return schedule_dict

@pytest.fixture
def list_of_items_dtos():

    items_list = [
        ItemDto(item_id=1, item='Idly', category='Indian-Bread', units='pieces', meal_id=0),
        ItemDto(item_id=2, item='Poori', category='Indian-Bread', units='pieces', meal_id=0),
        ItemDto(item_id=3, item='MasalaRice', category='Rice', units='laddles', meal_id=0),
        ItemDto(item_id=4, item='AlooCurry', category='Curry', units='cups', meal_id=0),
        ItemDto(item_id=5, item='Rice', category='Rice', units='laddles', meal_id=0),
        ItemDto(item_id=6, item='Dal', category='Curry', units='cups', meal_id=0),
        ItemDto(item_id=7, item='CabbageCurry', category='Curry', units='cups', meal_id=0),
        ItemDto(item_id=8, item='Roti', category='Indian-Bread', units='pieces', meal_id=0),
        ItemDto(item_id=9, item='Rajma', category='Curry', units='cups', meal_id=0),
        ItemDto(item_id=10, item='Curd', category='Curry', units='cups', meal_id=0)
    ]
    return items_list

@pytest.fixture
def list_of_items():
    items_list = [
        {
            'item_id': 1,
            'item': 'Idly',
            'category': 'Indian-Bread',
            'units': 'pieces'
        },
        {
            'item_id': 2,
            'item': 'Poori',
            'category': 'Indian-Bread',
            'units': 'pieces'
        },
        {
            'item_id': 3,
            'item': 'MasalaRice',
            'category': 'Rice',
            'units': 'laddles'
        },
        {
            'item_id': 4,
            'item': 'AlooCurry',
            'category': 'Curry',
            'units': 'cups'
        },
        {
            'item_id': 5,
            'item': 'Rice',
            'category': 'Rice',
            'units': 'laddles'
        },
        {
            'item_id': 6,
            'item': 'Dal',
            'category': 'Curry',
            'units': 'cups'
        },
        {
            'item_id': 7,
            'item': 'CabbageCurry',
            'category': 'Curry',
            'units': 'cups'
        },
        {
            'item_id': 8,
            'item': 'Roti',
            'category': 'Indian-Bread',
            'units': 'pieces'
        },
        {
            'item_id': 9,
            'item': 'Rajma',
            'category': 'Curry',
            'units': 'cups'
        },
        {
            'item_id': 10,
            'item': 'Curd',
            'category': 'Curry',
            'units': 'cups'
        }
    ]
    return items_list


@pytest.fixture
def items_and_rating_dtos():
    items_and_rating_dtos_list = [
        ItemAndRatingDto(item_id=1, quality=4, taste=4),
        ItemAndRatingDto(item_id=2, quality=4, taste=4),
        ItemAndRatingDto(item_id=3, quality=3, taste=4)
    ]
    return items_and_rating_dtos_list

@pytest.fixture
def get_rating_dto(items_and_rating_dtos):
    return UserRatingDto(
        items_and_ratings=items_and_rating_dtos,
        description=''
    )

@pytest.fixture
def get_rating_dict():
    rating_dict = {
        "items_and_ratings": [
            {
                "item_id":1,
                "taste":4,
                "quality":4
            },
            {
                "item_id":2,
                "taste":4,
                "quality":4
            },
            {
                "item_id":3,
                "taste":4,
                "quality":3
            }
        ],
        "description": ''
    }
    return rating_dict

@pytest.fixture
def items_and_wastage():
    item_and_wastage_list = [
        ItemAndWastageDto(item_id=1, item='Idly', food_prepared=300, food_wasted=50, base_unit='pieces'),
        ItemAndWastageDto(item_id=2, item='Poori', food_prepared=300, food_wasted=50, base_unit='pieces'),
        ItemAndWastageDto(item_id=3, item='MasalaRice', food_prepared=105, food_wasted=10, base_unit='kg')
    ]
    return item_and_wastage_list

@pytest.fixture
def food_wastage_dto(items_and_wastage):
    return FoodWastageDto(
        food_wasted= 10,
        food_prepared= 45,
        base_unit= 'kg',
        items_and_wastage= items_and_wastage
    )

@pytest.fixture
def food_wastage_dict():
    food_wastage_dict = {
        'food_wasted': 10,
        'food_prepared': 45,
        'items_and_wastage':[
            {
                "item_id":1,
                "item":'Idly',
                "food_prepared": 300,
                "food_wasted": 50,
                'base_unit':'pieces'
            },
            {
                "item_id":2,
                "item":'Poori',
                "food_prepared": 300,
                "food_wasted": 50,
                'base_unit':'pieces'
            },
            {
                "item_id":3,
                "item":'MasalaRice',
                "food_prepared": 105,
                "food_wasted": 10,
                'base_unit':'kg'
            }
        ]
    }
    return food_wastage_dict

@dataclass
class UserDto:
    user_id: int
    username: str
    email: str
    profile_pic: Pattern = re.compile("(https?)://([^/\r\n]+)(/[^\r\n]*)?")


@pytest.fixture
def user_profile_dtos():

    return [
        UserDto(
            user_id=1,
            username='username1',
            profile_pic='https://www.profile_pic1',
            email='username1@gmail.com'
            )
        ]

@pytest.fixture
def expected_user_profile_dtos_response():

    response_dict = {
        'user_id': 1,
        'profile_pic': 'https://www.profile_pic1',
        'username': 'username1',
        'email': 'username1@gmail.com'
    }
    return response_dict