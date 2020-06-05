from django.contrib.auth.hashers import make_password
from datetime import datetime
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.models.user import User
from food_management.models.meal import Meal
from food_management.models.announcements import Announcements
from food_management.models.items import Items
from food_management.models.meal_course import MealCourse
from food_management.dtos.dtos import ItemAndQuantityDto, CustomeMealUpdateDto
from food_management.models.user_meal_status import UserMealStatus
import pytest
from freezegun import freeze_time
from django.utils import timezone
from datetime import time
from food_management.interactors.storages.dtos import (
    HomePageDto, MealCourseDto, ItemDto, MealDto, AnnouncementDtos,
    MealCourseCompleteDetailsDto, SetMealPreferenceDto
)
from food_management.constants.enums import (
    TypeOfMeal, CategoryType, UnitType, CourseType
)

@pytest.fixture
def user_objs():

    user_dict = [
        {'username': 'user1', 'password': 'password1'},
        {'username': 'user2', 'password': 'password2'},
        {'username': 'user3', 'password': 'password3'}
    ]

    User.objects.bulk_create([
        User(username=user['username'], password=make_password(user['password'])
    ) for user in user_dict])

@pytest.fixture
@freeze_time('2020-02-12')
def meal_objs(item_objs):
    datetime_obj = datetime.now()
    meal_dict = [
        {
            'meal_type': TypeOfMeal.breakfast.value,
            'date': datetime_obj,
            'from_time_string': '00:00',
            'to_time_string': '00:00'
        },
        {
            'meal_type': TypeOfMeal.lunch.value,
            'date': datetime_obj,
            'from_time_string': '00:00',
            'to_time_string': '00:00'
        },
        {
            'meal_type': TypeOfMeal.dinner.value,
            'date': datetime_obj,
            'from_time_string': '00:00',
            'to_time_string': '00:00'
        }
    ]

    Meal.objects.bulk_create([
        Meal(
            meal_type=meal['meal_type'], date=meal['date'],
            from_time_string=meal['from_time_string'],
            to_time_string=meal['to_time_string']
        )
        for meal in meal_dict
    ])



@pytest.fixture
@freeze_time('2020-02-12')
def meal_dtos(meal_objs, item_objs):
    meal_dtos_list = [
        MealDto(
            meal_id=1, meal_type=TypeOfMeal.breakfast.value,
            date=datetime.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        ),
        MealDto(
            meal_id=2, meal_type=TypeOfMeal.lunch.value,
            date=datetime.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        ),
        MealDto(
            meal_id=3, meal_type=TypeOfMeal.dinner.value,
            date=datetime.now(), from_time_string=time(0, 0),
            to_time_string=time(0, 0)
        )
        ]
    return meal_dtos_list

@pytest.fixture
def item_objs():
    items_dict = [
        {
            'item': 'Idly', 'category': CategoryType.indian_bread.value,
            'units': UnitType.pieces.value
        },
        {
            'item': 'Poori', 'category': CategoryType.indian_bread.value,
            'units': UnitType.pieces.value
        },
        {
            'item': 'MasalaRice', 'category': CategoryType.rice.value,
            'units': UnitType.laddles.value
        },
        {
            'item': 'WhiteRice', 'category': CategoryType.rice.value,
            'units': UnitType.laddles.value
        },
        {
            'item': 'Dal', 'category': CategoryType.curry.value,
            'units': UnitType.cups.value
        },
        {
            'item': 'PotatoCurry', 'category': CategoryType.curry.value,
            'units': UnitType.cups.value
        },
        {
            'item': 'Curd', 'category': CategoryType.curry.value,
            'units': UnitType.cups.value
        },
        {
            'item': 'Roti', 'category': CategoryType.indian_bread.value,
            'units': UnitType.pieces.value
        },
        {
            'item': 'Rajma', 'category': CategoryType.curry.value,
            'units': UnitType.cups.value
        },
        {
            'item': 'FriedRice', 'category': CategoryType.rice.value,
            'units': UnitType.laddles.value
        }
    ]
    Items.objects.bulk_create([
        Items(
            item=item['item'],
            category=item['category'],
            units=item['units']
        )
    for item in items_dict])

@pytest.fixture
def item_dtos(item_objs, meal_objs):
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
def meal_course_objs(item_objs, meal_objs):
    meal_course_list = [
        {
            'item_id':1, 'meal_course': 'Half-meal', 'meal_id': 1, 'quantity':2
        },
        {
            'item_id':2, 'meal_course': 'Half-meal', 'meal_id': 1, 'quantity':2
        },
        {
            'item_id':3, 'meal_course': 'Half-meal', 'meal_id': 1, 'quantity':2
        },
        {
            'item_id':4, 'meal_course': 'Half-meal', 'meal_id': 2, 'quantity':2
        },
        {
            'item_id':5, 'meal_course': 'Half-meal', 'meal_id': 2, 'quantity':2
        },
        {
            'item_id':6, 'meal_course': 'Half-meal', 'meal_id': 2, 'quantity':2
        },
        {
            'item_id':7, 'meal_course': 'Half-meal', 'meal_id': 2, 'quantity':2
        },
        {
            'item_id':8, 'meal_course': 'Full-meal', 'meal_id': 3, 'quantity':3
        },
        {
            'item_id':9, 'meal_course': 'Full-meal', 'meal_id': 3, 'quantity':2
        },
        {
            'item_id':10, 'meal_course': 'Full-meal', 'meal_id': 3, 'quantity':3
        },
        {
            'item_id':1, 'meal_course': 'Full-meal', 'meal_id': 1, 'quantity':3
        },
        {
            'item_id':2, 'meal_course': 'Full-meal', 'meal_id': 1, 'quantity':3
        },
        {
            'item_id':3, 'meal_course': 'Full-meal', 'meal_id': 1, 'quantity':3
        }
    ]
    MealCourse.objects.bulk_create([
        MealCourse(
            meal_id=meal_course['meal_id'],
            item_id=meal_course['item_id'],
            meal_course=meal_course['meal_course'],
            quantity=meal_course['quantity']
            )
        for meal_course in meal_course_list
    ])


@pytest.fixture
def user_meal_course_objs(meal_objs, user_objs, meal_course_objs):
    user_meal_course_dict=[
        {
            'user_id': 1, 'meal_course_id': 1,
            'meal_id': 1
        },
        {
            'user_id': 1, 'meal_course_id': 2,
            'meal_id': 1
        },
        {
            'user_id': 1, 'meal_course_id': 3,
            'meal_id': 1
        },
        {
            'user_id': 1, 'meal_course_id': 4,
            'meal_id': 2
        },
        {
            'user_id': 1, 'meal_course_id': 5,
            'meal_id': 2
        },
        {
            'user_id': 1, 'meal_course_id': 6,
            'meal_id': 2
        },
        {
            'user_id': 1, 'meal_course_id': 7,
            'meal_id': 2
        },
        {
            'user_id': 1, 'meal_course_id': 8,
            'meal_id': 3
        },
        {
            'user_id': 1, 'meal_course_id': 9,
            'meal_id': 3
        },
        {
            'user_id': 1, 'meal_course_id': 10,
            'meal_id': 3
        }
        ]
    UserMealStatus.objects.bulk_create([
        UserMealStatus(
            user_id=user_meal['user_id'], meal_course_id=user_meal['meal_course_id'],
            meal_id=user_meal['meal_id']
        )
        for user_meal in user_meal_course_dict
    ])

@pytest.fixture
def meal_course_dtos(user_meal_course_objs):
    meal_course_dtos_list = [
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
            meal_id=1, meal_type=TypeOfMeal.breakfast.value
        ),
        MealCourseDto(
            meal_course=CourseType.half_meal.value,
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
def announcement_objs():
    announcement_list = [
        {
            'title': 'Happy Birthday',
            'subtitle': 'Birthday Special!',
            'description':'Here are the newly added items on the occasion of our \
                         friends birthday',
            'image':'https://www.google.co.in',
            'date': datetime.now()
        }
    ]
    Announcements.objects.bulk_create([
        Announcements(
            title=announcement['title'],
            subtitle=announcement['subtitle'],
            description=announcement['description'],
            image=announcement['image'],
            date=announcement['date']
        )
        for announcement in announcement_list
    ])

@pytest.fixture
def annoncement_dtos(announcement_objs):
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
def meal_items_dtos(item_objs):
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
def meal_course_complete_details_dtos(item_objs, meal_course_objs):
    meal_course_details_list = [
        MealCourseCompleteDetailsDto(
            item_id=1, meal_course=CourseType.half_meal.value, quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=2, meal_course=CourseType.half_meal.value, quantity=2
        ),
        MealCourseCompleteDetailsDto(
            item_id=3, meal_course=CourseType.half_meal.value, quantity=2
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
def item_and_quantity_dtos(item_objs):
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
@freeze_time('2020-02-12')
def custom_meal_upadte_dto(item_and_quantity_dtos, meal_objs):
    datetime_obj = datetime(2020,2,12)
    return CustomeMealUpdateDto(
        user_id=1,
        date=datetime_obj,
        meal_type=TypeOfMeal.breakfast.value,
        items_and_quantities=item_and_quantity_dtos
    )