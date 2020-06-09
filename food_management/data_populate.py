from django.contrib.auth.hashers import make_password
from food_management.models import *
from food_management.constants.enums import *
from food_management.constants.constants import *
from datetime import date
import requests


def user_objects():
    user_list = [
        {
            "username": "Vandhana", "password": "ibhubs-tap"
        },
        {
            "username": "Chandini", "password": "ibhubs-tap"
        },
        {
            "username": "Devayani", "password": "ibhubs-tap"
        },
        {
            "username": "Namratha", "password": "ibhubs-tap"
        },
        {
            "username": "Naveena", "password": "ibhubs-tap"
        },
        {
            "username": "Prasanna", "password": "ibhubs-tap"
        },
        {
            "username": "Nikhil", "password": "ibhubs-tap"
        },
        {
            "username": "Kavitha", "password": "ibhubs-tap"
        },
        {
            "username": "Srinivasa", "password": "ibhubs-tap"
        },
        {
            "username": "Kalpita", "password": "ibhubs-tap"
        },
        {
            "username": "Vishali", "password": "ibhubs-tap"
        },
        {
            "username": "Likitha", "password": "ibhubs-tap"
        },
        {
            "username": "Avighna", "password": "ibhubs-tap"
        },
        {
            "username": "Roshni", "password": "ibhubs-tap"
        },
        {
            "username": "Harika", "password": "ibhubs-tap"
        }
    ]
    User.objects.bulk_create(
        [
            User(
                username=user['username'],
                password=make_password(user['password'])
            )
            for user in user_list
        ]
    )


def item_objects():

    items_list = [
        {
            "item": "Idly",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Poori",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Aloo Curry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Masala Rice",
            "units": UnitType.laddles.value,
            "category": CategoryType.rice.value
        },
        {
            "item": "Dosa",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Uthapam",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Lemon Rice",
            "units": UnitType.laddles.value,
            "category": CategoryType.rice.value
        },
        {
            "item": "Chutney",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "ALoo Paratha",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Roti",
            "units": UnitType.pieces.value,
            "category": CategoryType.indian_bread.value
        },
        {
            "item": "Paneer Curry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Chole Batura",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Rajma",
            "units": UnitType.pieces.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "FriedRice",
            "units": UnitType.laddles.value,
            "category": CategoryType.rice.value
        },
        {
            "item": "Raitha",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Biryani",
            "units": UnitType.laddles.value,
            "category": CategoryType.rice.value
        },
        {
            "item": "AlooKurma",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Sambar",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Tomato Dal",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Cabbage Fry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Brinjal Curry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "White Rice",
            "units": UnitType.laddles.value,
            "category": CategoryType.rice.value
        },
        {
            "item": "Curd",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Butter milk",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Spinach Dal",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Drumstick Curry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Capsicum Curry",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        },
        {
            "item": "Rasam",
            "units": UnitType.cups.value,
            "category": CategoryType.curry.value
        }
    ]
    Items.objects.bulk_create(
        [
            Items(
                item=item['item'],
                units=item['units'],
                category=item['category']
            )
            for item in items_list
        ]
    )


def meal_objects():

    meal_list = [
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,4)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,4)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,4)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,5)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,5)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,5)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,6)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,6)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,6)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,7)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,7)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,7)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,8)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,8)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,8)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,9)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,9)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,9)
        },
        {
            "meal_type": TypeOfMeal.breakfast.value,
            "from_time_string": BREAKFAST_START_TIME,
            "to_time_string": BREAKFAST_END_TIME,
            "date": date(2020,6,10)
        },
        {
            "meal_type": TypeOfMeal.lunch.value,
            "from_time_string": LUNCH_START_TIME,
            "to_time_string": LUNCH_END_TIME,
            "date": date(2020,6,10)
        },
        {
            "meal_type": TypeOfMeal.dinner.value,
            "from_time_string": DINNER_START_TIME,
            "to_time_string": DINNER_END_TIME,
            "date": date(2020,6,10)
        }
    ]
    Meal.objects.bulk_create(
        [
            Meal(
                meal_type=meal['meal_type'],
                date=meal['date'],
                from_time_string=meal['from_time_string'],
                to_time_string=meal['to_time_string']
            )
        for meal in meal_list
        ]
    )


def meal_course_objs():
    meal_course_list = [
        {
            "meal_id":1, "item_id":1, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":1, "item_id":1, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":1, "item_id":1, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":1, "item_id":1, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":1, "item_id":2, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":1, "item_id":2, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":1, "item_id":2, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":1, "item_id":2, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":1, "item_id":3, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":1, "item_id":3, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":1, "item_id":3, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":1, "item_id":3, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":1, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":1, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":1, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":1, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":2, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":2, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":4
        },
        {
            "meal_id":2, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":2, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":2, "item_id":18, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":2, "item_id":18, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":2, "item_id":18, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":2, "item_id":18, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":2, "item_id":20, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":2, "item_id":20, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":2, "item_id":20, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":2, "item_id":20, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":2, "item_id":23, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":2, "item_id":23, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":2, "item_id":23, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":2, "item_id":23, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":3, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":3, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":3, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":3, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":3, "item_id":11, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":3, "item_id":11, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":3, "item_id":11, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":3, "item_id":11, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":3, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":3, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":3, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":3, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":3, "item_id":15, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":3, "item_id":15, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":3, "item_id":15, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":3, "item_id":15, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":4, "item_id":5, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":4, "item_id":5, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":4, "item_id":5, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":4, "item_id":5, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":4, "item_id":6, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":4, "item_id":6, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":4, "item_id":6, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":4, "item_id":6, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":4, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":4, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":4, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":4, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":4, "item_id":4, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":4, "item_id":4, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":4, "item_id":4, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":4, "item_id":4, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":5, "item_id":19, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":5, "item_id":19, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":5, "item_id":19, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":5, "item_id":19, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":5, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":5, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":5, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":5, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":5, "item_id":28, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":5, "item_id":28, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":5, "item_id":28, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":5, "item_id":28, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":5, "item_id":24, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":5, "item_id":24, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":5, "item_id":24, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":5, "item_id":24, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":6, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":6, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":6, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":6, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":6, "item_id":12, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":6, "item_id":12, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":6, "item_id":12, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":6, "item_id":12, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":6, "item_id":16, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":6, "item_id":16, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":6, "item_id":16, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":6, "item_id":16, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":6, "item_id":17, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":6, "item_id":17, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":6, "item_id":17, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":6, "item_id":17, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

        {
            "meal_id":7, "item_id":1, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":7, "item_id":1, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":7, "item_id":1, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":7, "item_id":1, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":7, "item_id":9, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":7, "item_id":9, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":7, "item_id":9, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":7, "item_id":9, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":7, "item_id":7, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":7, "item_id":7, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":7, "item_id":7, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":7, "item_id":7, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":7, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":7, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":7, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":7, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":8, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":8, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":4
        },
        {
            "meal_id":8, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":8, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":8, "item_id":25, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":8, "item_id":25, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":8, "item_id":25, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":8, "item_id":25, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":8, "item_id":26, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":8, "item_id":26, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":8, "item_id":26, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":8, "item_id":26, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":8, "item_id":23, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":8, "item_id":23, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":8, "item_id":23, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":8, "item_id":23, "meal_course":CourseType.custom_meal.value , "quantity":0
        },



        {
            "meal_id":9, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":9, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":9, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":9, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":9, "item_id":13, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":9, "item_id":13, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":9, "item_id":13, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":9, "item_id":13, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":9, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":9, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":9, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":9, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":9, "item_id":17, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":9, "item_id":17, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":9, "item_id":17, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":9, "item_id":17, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":10, "item_id":5, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":10, "item_id":5, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":10, "item_id":5, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":10, "item_id":5, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":10, "item_id":1, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":10, "item_id":1, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":10, "item_id":1, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":10, "item_id":1, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":10, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":10, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":10, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":10, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":10, "item_id":4, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":10, "item_id":4, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":10, "item_id":4, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":10, "item_id":4, "meal_course":CourseType.custom_meal.value , "quantity":0
        },



        {
            "meal_id":11, "item_id":16, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":11, "item_id":16, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":11, "item_id":16, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":11, "item_id":16, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":11, "item_id":17, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":11, "item_id":17, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":11, "item_id":17, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":11, "item_id":17, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":11, "item_id":18, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":11, "item_id":18, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":11, "item_id":18, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":11, "item_id":18, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":11, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":11, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":11, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":11, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":12, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":12, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":12, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":12, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":12, "item_id":11, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":12, "item_id":11, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":12, "item_id":11, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":12, "item_id":11, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":12, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":12, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":12, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":12, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":12, "item_id":15, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":12, "item_id":15, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":12, "item_id":15, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":12, "item_id":15, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":13, "item_id":2, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":13, "item_id":2, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":13, "item_id":2, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":13, "item_id":2, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":13, "item_id":3, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":13, "item_id":3, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":13, "item_id":3, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":13, "item_id":3, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":13, "item_id":7, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":13, "item_id":7, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":13, "item_id":7, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":13, "item_id":7, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":13, "item_id":4, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":13, "item_id":4, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":13, "item_id":4, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":13, "item_id":4, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":14, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":14, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":4
        },
        {
            "meal_id":14, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":14, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":14, "item_id":27, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":14, "item_id":27, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":14, "item_id":27, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":14, "item_id":27, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":14, "item_id":28, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":14, "item_id":28, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":14, "item_id":28, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":14, "item_id":28, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":14, "item_id":23, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":14, "item_id":23, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":14, "item_id":23, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":14, "item_id":23, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":15, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":15, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":15, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":15, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":15, "item_id":11, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":15, "item_id":11, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":15, "item_id":11, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":15, "item_id":11, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":15, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":15, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":15, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":15, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":15, "item_id":13, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":15, "item_id":13, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":15, "item_id":13, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":15, "item_id":13, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":16, "item_id":9, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":16, "item_id":9, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":16, "item_id":9, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":16, "item_id":9, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":16, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":16, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":16, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":16, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":16, "item_id":3, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":16, "item_id":3, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":16, "item_id":3, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":16, "item_id":3, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":16, "item_id":4, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":16, "item_id":4, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":16, "item_id":4, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":16, "item_id":4, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":17, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":17, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":4
        },
        {
            "meal_id":17, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":17, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":17, "item_id":24, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":17, "item_id":24, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":17, "item_id":24, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":17, "item_id":24, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":17, "item_id":18, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":17, "item_id":18, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":17, "item_id":18, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":17, "item_id":18, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":17, "item_id":25, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":17, "item_id":25, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":17, "item_id":25, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":17, "item_id":25, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":18, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":18, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":18, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":18, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":18, "item_id":12, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":18, "item_id":12, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":18, "item_id":12, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":18, "item_id":12, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":18, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":18, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":18, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":18, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":18, "item_id":15, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":18, "item_id":15, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":18, "item_id":15, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":18, "item_id":15, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":19, "item_id":1, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":19, "item_id":1, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":19, "item_id":1, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":19, "item_id":1, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":19, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":19, "item_id":5, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":19, "item_id":5, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":19, "item_id":5, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":19, "item_id":5, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":19, "item_id":8, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":19, "item_id":8, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":20, "item_id":22, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":20, "item_id":22, "meal_course":CourseType.full_meal.value , "quantity":4
        },
        {
            "meal_id":20, "item_id":22, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":20, "item_id":22, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":20, "item_id":26, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":20, "item_id":26, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":20, "item_id":26, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":20, "item_id":26, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":20, "item_id":27, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":20, "item_id":27, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":20, "item_id":27, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":20, "item_id":27, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":20, "item_id":23, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":20, "item_id":23, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":20, "item_id":23, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":20, "item_id":23, "meal_course":CourseType.custom_meal.value , "quantity":0
        },


        {
            "meal_id":21, "item_id":10, "meal_course":CourseType.half_meal.value , "quantity":3
        },
        {
            "meal_id":21, "item_id":10, "meal_course":CourseType.full_meal.value , "quantity":5
        },
        {
            "meal_id":21, "item_id":10, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":21, "item_id":10, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":21, "item_id":11, "meal_course":CourseType.half_meal.value , "quantity":2
        },
        {
            "meal_id":21, "item_id":11, "meal_course":CourseType.full_meal.value , "quantity":3
        },
        {
            "meal_id":21, "item_id":11, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":21, "item_id":11, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":21, "item_id":14, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":21, "item_id":14, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":21, "item_id":14, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":21, "item_id":14, "meal_course":CourseType.custom_meal.value , "quantity":0
        },
        {
            "meal_id":21, "item_id":13, "meal_course":CourseType.half_meal.value , "quantity":1
        },
        {
            "meal_id":21, "item_id":13, "meal_course":CourseType.full_meal.value , "quantity":2
        },
        {
            "meal_id":21, "item_id":13, "meal_course": CourseType.skip_meal.value, "quantity":0
        },
        {
            "meal_id":21, "item_id":13, "meal_course":CourseType.custom_meal.value , "quantity":0
        },

    ] 
    MealCourse.objects.bulk_create(
        [
        MealCourse(
                meal_course= meal_course['meal_course'],
                meal_id=meal_course['meal_id'],
                item_id=meal_course['item_id'],
                quantity= meal_course['quantity']
            )
        for meal_course in meal_course_list
        ]
    )

#user-login
def user_login():
    data = {
        "username":"Vandhana",
        "password":"ibhubs-tap"
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/signin/v1/',
        json=data
    )
    return response

#home-page
def home_page():
    data = {
        "date": "2020-06-06",
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/home/v1/',
        headers={"Authorization":"Bearer Ldk98VtSBIHCkaHeZ85shbCC59JcYW"},
        json=data
    )
    return response

#get-meal-preference
def get_meal_preference():
    data = {
        "meal_type": "Breakfast",
        "date": "2020-06-04"
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/meal/preference/v1/',
        headers={"Authorization":"Bearer Ldk98VtSBIHCkaHeZ85shbCC59JcYW"},
        json=data
    )
    return response

#custom-meal-update
def custom_meal_update():
    data = {
        "meal_type":"Breakfast",
        "date":"2020-06-04",
        "meal_course": "Custom-meal",
        "items_and_quantities":[
            {
                "item_id":1,"quantity":2
            },
            {
                "item_id":2,"quantity":1
            },
            {
                "item_id":3, "quantity":3
            },
            {
                "item_id":8,"quantity":0
            }
        ]
    }
    response = requests.put(
        url='http://127.0.0.1:8080/api/food_management/meal/custom_meal/update/v1/',
        headers={"Authorization":"Bearer Ldk98VtSBIHCkaHeZ85shbCC59JcYW"},
        json=data
    )
    return response

#update-meal-preference
def update_meal_preference():
    data = {
        "meal_type":"Breakfast",
        "date": "2020-06-06",
        "meal_course":"Half-meal"
    }
    response = requests.put(
        url='http://127.0.0.1:8080/api/food_management/meal/preference/update/v1/',
        headers={"Authorization":"Bearer "},
        json=data
    )
    return response

#get_rating
def get_rating():
    data = {
        "meal_type": "Breakfast",
        "date":"2020-06-04"
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/rating/v1/',
        headers={"Authorization":"Bearer "},
        json=data
    )
    return response

#update_rating
def update_rating():
    data = {
        "meal_type":"Breakfast",
        "date":"2020-06-04",
        "items_and_ratings":[
            {
                "item_id": 1,
                "taste": 3,
                "quality": 5
            },
            {
                "item_id": 2,
                "taste": 3,
                "quality": 3
            },
            {
                "item_id": 3,
                "taste": 3,
                "quality": 3
            },
            {
                "item_id": 8,
                "taste": 3,
                "quality": 3
            }
        ],
        "description": ''
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/rating/update/v1/',
        headers={"Authorization":"Bearer "},
        json=data
    )
    return response

#admin-schedule
def admin_schedule():

    data = {
        "meal_type": "Breakfast",
        "date":"2020-06-06"
    }
    response = requests.post(
        url='http://127.0.0.1:8080/api/food_management/admin/schedule_menu/v1/',
        headers={"Authorization":"Bearer ibhubs125"},
        json=data
    )
    return response



#writing models
