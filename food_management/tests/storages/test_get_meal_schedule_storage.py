import pytest
from freezegun import freeze_time
from datetime import datetime
from freezegun import freeze_time
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_get_meal_schedule_returns_schedule_for_that_date(meal_schedule_dto):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = 'Breakfast'

    #Act
    actual_meal_schedule = meal_storage.get_meal_schedule(
        date_obj=datetime.now(), meal_type=meal_type
    )

    #Assert
    assert actual_meal_schedule == meal_schedule_dto