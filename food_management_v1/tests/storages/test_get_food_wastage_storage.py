import pytest
from freezegun import freeze_time
from datetime import datetime
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation


@pytest.fixture
@freeze_time('2020-02-12')
def test_get_food_wastage(food_wastage_dto):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = 'Breakfast'
    date_obj = datetime.now()

    #Act
    food_wastage_dto = meal_storage.get_food_wastage(meal_type=meal_type, date_obj=date_obj)

    #Assert