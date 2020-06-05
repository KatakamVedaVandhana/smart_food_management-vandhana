import pytest
from django.utils import timezone
from datetime import datetime
from food_management.models.user import User
from common.dtos import (
    UserAuthTokensDTO, Application, AccessTokenDTO, RefreshTokenDTO
)
from freezegun import freeze_time
from django.contrib.auth.hashers import make_password
from food_management.interactors.storages.dtos import (
    UserDto, ItemDto, MealCourseDto, MealDto, HomePageDto, MealScheduleDto,
    AnnouncementDtos, MealCourseCompleteDetailsDto, SetMealPreferenceDto,
    ItemsCountDto, MealCourseCountDto,
    HeadCountDto, UserRatingDto, FoodWastageDto, ItemAndWastageDto
)
from food_management.dtos.dtos import (
    ItemAndQuantityDto, CustomeMealUpdateDto, RatingDto, ItemAndRatingDto,
    UpdateMealScheduleDto, ItemDetailsDto
)
from food_management.constants.enums import (
    CategoryType, TypeOfMeal, UnitType, CourseType
)
from food_management.constants.constants import (
    DEFAULT_TIME_FORMAT, DEFAULT_DATE_FORMAT
)


@pytest.fixture
def user_dtos():

    user_dtos = [
        UserDto(user_id=1, username='user1', password='password1'),
        UserDto(user_id=2, username='user2', password='password2'),
        UserDto(user_id=3, username='user3', password='password3')
    ]
    return user_dtos

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
def login_details_response_dict():
    response_dict = {
        "user_id": 1,
        "access_token": '125',
        "refresh_token": '521',
        'expires_in': '2020-02-12'
    }
    return response_dict

@pytest.fixture
def application_dto():
    application_dto = Application(application_id=1)
    return application_dto

@pytest.fixture
@freeze_time('2020-02-12')
def access_token_dto():
    access_token_dto = AccessTokenDTO(
        access_token_id=1,
        token='125',
        expires=timezone.now()
    )
    return access_token_dto

@pytest.fixture
@freeze_time('2020-02-12')
def refresh_token_dto():
    refresh_token = RefreshTokenDTO(
        token='521',
        access_token='125',
        user_id=1,
        revoked=timezone.now()
    )
    return refresh_token


@pytest.fixture
@freeze_time('2020-02-12')
def meal_dtos():
    datetime_obj = datetime(20,2,12)
    meal_dtos = [
        MealDto(
            meal_id=1, meal_type=TypeOfMeal.breakfast.value,
            date=datetime_obj.strftime(DEFAULT_DATE_FORMAT),
            from_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            to_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        ),
        MealDto(
            meal_id=2, meal_type=TypeOfMeal.lunch.value,
            date=datetime_obj.strftime(DEFAULT_DATE_FORMAT),
            from_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            to_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        ),
        MealDto(
            meal_id=3, meal_type=TypeOfMeal.dinner.value,
            date=datetime_obj.strftime(DEFAULT_DATE_FORMAT),
            from_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            to_time_string=datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        )
    ]

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
def meal_schedule_dto(items_dto, meal_breakfast_dto):
    return MealScheduleDto(
        items=items_dto,
        meal=meal_dtos
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
@freeze_time('2020-02-12')
def home_page_dict():
    datetime_obj = datetime(2020,2,12)
    home_page_dict = [
        {
            'meal_type': TypeOfMeal.breakfast.value,
            'items':[
                {
                    "item_id": 1,
                    "meal_item": "Idly",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 2,
                    "meal_item": "Poori",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 3,
                    "meal_item": "MasalaRice",
                    "units": UnitType.laddles.value
                }
            ],
            "meal_course": CourseType.half_meal.value,
            "from_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            "to_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        },
        {
            'meal_type': TypeOfMeal.lunch.value,
            'items':[
                {
                    "item_id": 1,
                    "meal_item": "Idly",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 2,
                    "meal_item": "Poori",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 3,
                    "meal_item": "MasalaRice",
                    "units": UnitType.laddles.value
                }
            ],
            "meal_course": CourseType.half_meal.value,
            "from_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            "to_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        },
        {
            'meal_type': TypeOfMeal.dinner.value,
            'items':[
                {
                    "item_id": 1,
                    "meal_item": "Idly",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 2,
                    "meal_item": "Poori",
                    "units": UnitType.pieces.value
                },
                {
                    "item_id": 3,
                    "meal_item": "MasalaRice",
                    "units": UnitType.laddles.value
                }
            ],
            "meal_course": CourseType.half_meal.value,
            "from_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT),
            "to_time_string": datetime_obj.strftime(DEFAULT_TIME_FORMAT)
        }
    ]


@pytest.fixture
def meal_course_dtos():
    meal_course_dtos = [
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
            meal_id=1, meal_type = TypeOfMeal.breakfast.value
        ),
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
            meal_id=1, meal_type = TypeOfMeal.lunch.value
        ),
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
            meal_id=1, meal_type = TypeOfMeal.dinner.value
        )
    ]

@pytest.fixture
def home_page_dto(meal_dtos, meal_course_dtos, items_dto):
    home_page_dtos = HomePageDto(
        meal=meal_dtos, meal_course=meal_course_dtos,
        items=items_dto
    )

@pytest.fixture
def announcement_dtos():
    announcement_dtos_list = [
        AnnouncementDtos(
            title='Happy Birthday',
            subtitle='Birthday Special!',
            description='Here are the newly added items on the occasion of our \
                         friends birthday',
            image='https://www.google.co.in'
        )
        ]
    return announcement_dtos_list

@pytest.fixture
def announcement_resoponse_dict():
    announcement_resoponse_dict = [
        {
            'title': 'Happy Birthday',
            'subtitle': 'Birthday Special!',
            'description':'Here are the newly added items on the occasion of our \
                           friends birthday' ,
            'image': 'https://www.google.co.in'
        }
    ]

@pytest.fixture
def meal_course_list_dto():
    meal_course_dtos = [
        MealCourseCompleteDetailsDto(
           item_id=1, meal_course=CourseType.half_meal.value,
            quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=2, meal_course=CourseType.half_meal.value,
            quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=3, meal_course=CourseType.half_meal.value,
            quantity=1
        ),
        MealCourseCompleteDetailsDto(
            item_id=1, meal_course=CourseType.full_meal.value,
            quantity=3
        ),
        MealCourseCompleteDetailsDto(
            item_id=2, meal_course=CourseType.full_meal.value,
            quantity=3
        ),
        MealCourseCompleteDetailsDto(
            item_id=3, meal_course=CourseType.full_meal.value,
            quantity=1
        )
    ]


@pytest.fixture
def set_meal_preference_dtos(items_dto, meal_course_list_dto):
    set_meal_preference_dto = SetMealPreferenceDto(
        items=items_dto,
        meal_course=meal_course_list_dto
    )


@pytest.fixture
def items_dto():
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


@pytest.fixture
def set_meal_preference_list():
    set_meal_preference_list = [
        {
            'item_id': 1,
            'item': 'Idly',
            'category': CategoryType.indian_bread.value,
            'units': UnitType.pieces.value,
            'meal_courses': [
                {
                    'meal_course': CourseType.half_meal.value,
                    'quantity': 2
                },
                {
                    'meal_course': CourseType.full_meal.value,
                    'quantity': 3
                }
            ]
        },
        {
            'item_id': 2,
            'item': 'Poori',
            'category': CategoryType.indian_bread.value,
            'units': UnitType.pieces.value,
            'meal_courses': [
                {
                    'meal_course': CourseType.half_meal.value,
                    'quantity': 2
                },
                {
                    'meal_course': CourseType.full_meal.value,
                    'quantity': 3
                }
            ]
        },
        {
            'item_id': 3,
            'item': 'MasalaRice',
            'category': CategoryType.rice.value,
            'units': UnitType.pieces.value,
            'meal_courses': [
                {
                    'meal_course': CourseType.half_meal.value,
                    'quantity': 1
                },
                {
                    'meal_course': CourseType.full_meal.value,
                    'quantity': 2
                }
            ]
        }
    ]

@pytest.fixture
def item_and_quantity_dtos():
    list_of_items = [
        ItemAndQuantityDto(
            item_id=1, quantity=2,
        ),
        ItemAndQuantityDto(
            item_id=2, quantity=1,
        ),
        ItemAndQuantityDto(
            item_id=3, quantity=1,
        )
    ]
    return list_of_items

@pytest.fixture
def custom_meal_upadte_dto(item_and_quantity_dtos):
    return CustomeMealUpdateDto(
        user_id=1,
        meal_id=1,
        meal_course='Custom-meal',
        items_and_quantities=item_and_quantity_dtos
    )

@pytest.fixture
def custom_meal_dto_with_invalid_quantity():
    item_and_quantity = [
        ItemAndQuantityDto(
            item_id=2, quantity=-1
        )
    ]
    return CustomeMealUpdateDto(
        user_id=1,
        meal_id=1,
        meal_course='Custom-meal',
        items_and_quantities=item_and_quantity
    )



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
        "items_and_rating": [
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

@pytest.fixture
def rating_dtos(items_and_rating_dtos):
    return RatingDto(
        user_id=1,
        meal_id=1,
        description='',
        items_and_ratings=items_and_rating_dtos
    )

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
            'item': 'AlooCurry',
            'category': 'Curry',
            'units': 'cups'
        },
        {
            'item_id': 4,
            'item': 'MasalaRice',
            'category': 'Rice',
            'units': 'laddles'
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
def items_and_their_meal_course():
    items_and_meal_course_list = [
        ItemDetailsDto(
            item_id=1,meal_course='Half-meal',quantity=2
        ),
        ItemDetailsDto(
            item_id=2,meal_course='Half-meal',quantity=2
        ),
        ItemDetailsDto(
            item_id=3,meal_course='Half-meal',quantity=1
        ),
        ItemDetailsDto(
            item_id=1,meal_course='Full-meal',quantity=3
        ),
        ItemDetailsDto(
            item_id=2,meal_course='Full-meal',quantity=3
        ),
        ItemDetailsDto(
            item_id=3,meal_course='Full-meal',quantity=2
        )
    ]
    return items_and_meal_course_list

@freeze_time('2020-02-12')
@pytest.fixture
def update_meal_schedule_dtos(items_and_their_meal_course):
    return UpdateMealScheduleDto(
        meal_type='Breakfast',
        date=datetime.now(),
        items=items_and_their_meal_course
    )

@pytest.fixture
def meal_course_count():
    meal_count_list = [
        MealCourseCountDto(
            meal_course='Half-meal',
            meal_course_count = 6
        ),
         MealCourseCountDto(
            meal_course='Full-meal',
            meal_course_count = 8
        ),
         MealCourseCountDto(
            meal_course='Skip-meal',
            meal_course_count = 8
        ),
         MealCourseCountDto(
            meal_course='Custom-meal',
            meal_course_count = 10
        )
    ]
    return meal_count_list

@pytest.fixture
def items_count():
    items_count = [
        ItemsCountDto(
            item_id=1, item='Idly',item_count=8
        ),
        ItemsCountDto(
            item_id=2, item='Poori',item_count=8
        ),
        ItemsCountDto(
            item_id=3, item='MasalaRice',item_count=10
        )
    ]
    return items_count

@pytest.fixture
def head_count_dto(meal_course_count, items_count):
    return HeadCountDto(
        meal_course_count=meal_course_count,
        items_count=items_count,
        total_meal_head_count=12,
        completed_meal_head_count=8
    )

@pytest.fixture
def head_count_dict():
    head_count_dict = {
          "items_count": [
                {
                  "item_id": 1,
                  "item": "Idly",
                  "item_count": 8
                },
                {
                  "item_id": 2,
                  "item": "Poori",
                  "item_count": 8
                },
                {
                  "item_id": 1,
                  "item": "MasalaRice",
                  "item_count": 10
                }
          ],
          "meal_course_counts": [
                {
                  "meal_course": "Half-meal",
                  "meal_course_count": 6
                },
                {
                  "meal_course": "Full-meal",
                  "meal_course_count": 8
                },
                {
                  "meal_course": "Skip-meal",
                  "meal_course_count": 8
                },
                {
                  "meal_course": "Custom-meal",
                  "meal_course_count": 10
                }
          ],
          "total_meal_head_count": 12,
          "completed_meal_head_count": 8
    }
    return head_count_dict

@pytest.fixture
def items_and_wastage():
    item_and_wastage_list = [
        ItemAndWastageDto(item_id=1, item='Idly', food_prepared=300, food_wasted=50, base_unit='pieces'),
        ItemAndWastageDto(item_id=2, item='Poori', food_prepared=300, food_wasted=50, base_unit='pieces'),
        ItemAndWastageDto(item_id=3, item='MasalaRice', food_prepared=105, food_wasted=10, base_unit='kg')
    ]

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
                'base_unit':'pieces'
            }
        ]
    }
    return food_wastage_dict