import pytest
from datetime import date
from freezegun import freeze_time
from food_management.models import Meal
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.constants.constants import (
    BREAKFAST_END_TIME, BREAKFAST_START_TIME,
    LUNCH_START_TIME, LUNCH_END_TIME,
    DINNER_END_TIME, DINNER_START_TIME
)


@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_create_meal_schedule_for_breakfast(create_meal_schedule):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = create_meal_schedule.meal_type
    date_obj = create_meal_schedule.date
    from_time_string = BREAKFAST_START_TIME
    to_time_string = BREAKFAST_END_TIME

    #Act
    meal_storage.create_meal_schedule(
        update_meal_schedule_dto=create_meal_schedule,
        from_time_string=from_time_string, to_time_string=to_time_string
    )

    #Assert
    meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
    assert meal_obj.id == 1
    assert meal_obj.meal_type == meal_type
    assert meal_obj.from_time_string == from_time_string
    assert meal_obj.to_time_string == to_time_string
    assert meal_obj.date == date_obj