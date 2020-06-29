from django.contrib.auth.hashers import make_password
from datetime import datetime, date
from food_management.constants.constants import (
    DEFAULT_DATE_FORMAT, DEFAULT_TIME_FORMAT, BREAKFAST_START_TIME,
    BREAKFAST_END_TIME, LUNCH_START_TIME, LUNCH_END_TIME,
    DINNER_START_TIME, DINNER_END_TIME
)
from food_management.models.user import User
from food_management.models.meal import Meal
from food_management.models.user_rating import UserRating
from food_management.models.user_feedback import UserFeedback
from food_management.models.announcements import Announcements
from food_management.models.items import Items
from food_management.models.meal_course import MealCourse
from food_management.dtos.dtos import (
    ItemAndQuantityDto, CustomeMealUpdateDto, ItemAndRatingDto,
    RatingDto, UpdateMealScheduleDto, ItemDetailsDto
)
from food_management.models.user_meal_status import UserMealStatus
import pytest
from freezegun import freeze_time
from django.utils import timezone
from datetime import time
from food_management.interactors.storages.dtos import (
    HomePageDto, MealCourseDto, ItemDto, MealDto, AnnouncementDtos,
    MealCourseCompleteDetailsDto, SetMealPreferenceDto, MealScheduleDto
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
            'from_time_string': BREAKFAST_START_TIME,
            'to_time_string': BREAKFAST_END_TIME
        },
        {
            'meal_type': TypeOfMeal.lunch.value,
            'date': datetime_obj,
            'from_time_string': LUNCH_START_TIME,
            'to_time_string': LUNCH_END_TIME
        },
        {
            'meal_type': TypeOfMeal.dinner.value,
            'date': datetime_obj,
            'from_time_string': DINNER_START_TIME,
            'to_time_string': DINNER_END_TIME
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
            date=datetime.now(), from_time_string=BREAKFAST_START_TIME,
            to_time_string=BREAKFAST_END_TIME
        ),
        MealDto(
            meal_id=2, meal_type=TypeOfMeal.lunch.value,
            date=datetime.now(), from_time_string=LUNCH_START_TIME,
            to_time_string=LUNCH_END_TIME
        ),
        MealDto(
            meal_id=3, meal_type=TypeOfMeal.dinner.value,
            date=datetime.now(), from_time_string=DINNER_START_TIME,
            to_time_string=DINNER_END_TIME
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
def list_of_items_dtos(item_objs):

    items_list = [
        ItemDto(item_id=1, item='Idly', category='Indian-Bread', units='pieces', meal_id=None),
        ItemDto(item_id=2, item='Poori', category='Indian-Bread', units='pieces', meal_id=None),
        ItemDto(item_id=3, item='MasalaRice', category='Rice', units='laddles', meal_id=None),
        ItemDto(item_id=4, item='WhiteRice', category='Rice', units='laddles', meal_id=None),
        ItemDto(item_id=5, item='Dal', category='Curry', units='cups', meal_id=None),
        ItemDto(item_id=6, item='PotatoCurry', category='Curry', units='cups', meal_id=None),
        ItemDto(item_id=7, item='Curd', category='Curry', units='cups', meal_id=None),
        ItemDto(item_id=8, item='Roti', category='Indian-Bread', units='pieces', meal_id=None),
        ItemDto(item_id=9, item='Rajma', category='Curry', units='cups', meal_id=None),
        ItemDto(item_id=10, item='FriedRice', category='Rice', units='laddles', meal_id=None)
    ]
    return items_list


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
            'meal_id': 1, 'item_id':1, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 2,
            'meal_id': 1, 'item_id':2, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 3,
            'meal_id': 1, 'item_id':3, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 4,
            'meal_id': 2, 'item_id': 4, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 5,
            'meal_id': 2, 'item_id':5, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 6,
            'meal_id': 2, 'item_id':6, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 7,
            'meal_id': 2, 'item_id':7, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 8,
            'meal_id': 3, 'item_id':8, 'custom_meal_quantity':3
        },
        {
            'user_id': 1, 'meal_course_id': 9,
            'meal_id': 3, 'item_id':9, 'custom_meal_quantity':2
        },
        {
            'user_id': 1, 'meal_course_id': 10,
            'meal_id': 3, 'item_id':10, 'custom_meal_quantity':3
        }
        ]
    UserMealStatus.objects.bulk_create([
        UserMealStatus(
            user_id=user_meal['user_id'], meal_course_id=user_meal['meal_course_id'],
            meal_id=user_meal['meal_id'], item_id=user_meal['item_id'],
            custom_meal_quantity=user_meal['custom_meal_quaa']
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
def custom_meal_objs(item_objs, meal_objs):
    meal_course_list = [
        {
            'item_id':1, 'meal_course': 'Custom-meal', 'meal_id': 1, 'quantity':0
        },
        {
            'item_id':2, 'meal_course': 'Custom-meal', 'meal_id': 1, 'quantity':0
        },
        {
            'item_id':3, 'meal_course': 'Custom-meal', 'meal_id': 1, 'quantity':0
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
def custom_meal_upadte_dto(user_objs, item_and_quantity_dtos, custom_meal_objs):
    return CustomeMealUpdateDto(
        user_id=1,
        meal_id = 1,
        meal_course = 'Custom-meal',
        items_and_quantities=item_and_quantity_dtos
    )

@pytest.fixture
def user_rating_objs(user_objs, meal_objs):
    rating_list = [
        {
            'user_id': 1, 'meal_id': 1, 'item_id': 1, 'taste': 4, 'quality': 3
        },
        {
            'user_id': 1, 'meal_id': 1, 'item_id': 2, 'taste': 4, 'quality': 3
        },
        {
            'user_id': 1, 'meal_id': 1, 'item_id': 3, 'taste': 4, 'quality': 3
        }
    ]
    UserRating.objects.bulk_create([
        UserRating(
            user_id=rating_obj['user_id'],
            meal_id=rating_obj['meal_id'],
            taste=rating_obj['taste'],
            quality=rating_obj['quality'],
            item_id=rating_obj['item_id']
        )
        for rating_obj in rating_list
    ])

@pytest.fixture
def items_and_rating_dtos(item_objs, meal_objs):
    items_and_rating_dtos_list = [
        ItemAndRatingDto(item_id=1, quality=4, taste=4),
        ItemAndRatingDto(item_id=2, quality=4, taste=4),
        ItemAndRatingDto(item_id=3, quality=3, taste=4)
    ]
    return items_and_rating_dtos_list

@pytest.fixture
def rating_dtos(items_and_rating_dtos, user_objs, meal_objs):
    return RatingDto(
        user_id=1,
        meal_id=1,
        description='',
        items_and_ratings=items_and_rating_dtos
    )

@pytest.fixture
def user_feedback(user_objs, meal_objs):
    UserFeedback.objects.create(user_id=1, meal_id=1, description='')

@pytest.fixture
def update_items_and_rating_dtos(item_objs, meal_objs):
    items_and_rating_dtos_list = [
        ItemAndRatingDto(item_id=1, quality=2, taste=2),
        ItemAndRatingDto(item_id=2, quality=2, taste=3),
        ItemAndRatingDto(item_id=3, quality=4, taste=5)
    ]
    return items_and_rating_dtos_list

@pytest.fixture
def update_rating_dtos(
        update_items_and_rating_dtos, user_rating_objs,
        user_objs, meal_objs, user_feedback):
    return RatingDto(
        user_id=1,
        meal_id=1,
        description='',
        items_and_ratings=update_items_and_rating_dtos
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
    return MealDto(
            meal_id=1, meal_type=TypeOfMeal.breakfast.value,
            date=datetime.now(),
            from_time_string=BREAKFAST_START_TIME,
            to_time_string=BREAKFAST_END_TIME
        )

@pytest.fixture
def meal_schedule_dto(breakfast_items, meal_breakfast_dto, meal_course_objs):
    return MealScheduleDto(
        items=breakfast_items,
        meal=meal_breakfast_dto
    )

@pytest.fixture
def items_and_their_meal_course(item_objs):
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


@pytest.fixture
@freeze_time('2020-02-12')
def update_meal_schedule_dtos(items_and_their_meal_course, meal_course_objs):
    return UpdateMealScheduleDto(
        meal_type='Breakfast',
        date=date(2020,2,12),
        items=items_and_their_meal_course
    )

@pytest.fixture
@freeze_time('2020-02-12')
def create_meal_schedule(items_and_their_meal_course):
    return UpdateMealScheduleDto(
        meal_type='Breakfast',
        date=date(2020,2,12),
        items=items_and_their_meal_course
    )