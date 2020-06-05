import pytest
from freezegun import freeze_time
from datetime import datetime
from food_management.models import Meal, UserMealStatus
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation


@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_create_user_custom_meal_status(
        item_and_quantity_dtos, user_objs, user_meal_course_objs, meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = 'Breakfast'
    user_id = 1
    date_as_string = '2020-02-12'
    datetime_obj = datetime.strptime(date_as_string, DEFAULT_DATE_FORMAT)

    #Act
    meal_storage.create_user_custom_meal_status(
        meal_type=meal_type, user_id=user_id,
        date_obj=datetime_obj,
        meal_items_and_quantities=item_and_quantity_dtos
    )
    #Assert
    meal_obj = Meal.objects.get(meal_type=meal_type, date=datetime_obj)
    usermealstatus_obj = UserMealStatus.objects.filter(
        meal=meal_obj, user_id=user_id
    )
    usermealstatus_obj[0].meal_course == 'Course-meal'