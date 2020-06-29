import pytest
from datetime import datetime
from freezegun import freeze_time
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_get_meal_head_count(meal_objs, head_count_dto):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = 'Breakfast'
    date_obj = datetime.now()

    #Act
    meal_count_dto = meal_storage.get_meal_head_count(meal_type=meal_type, date_obj=date_obj)

    #Assert
    assert meal_count_dto == head_count_dto