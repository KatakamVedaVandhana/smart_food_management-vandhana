from datetime import datetime
import pytest
from freezegun import freeze_time
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_meal_preference_return_dto(meal_data_dtos, meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    date_in_string = '2020-02-12'
    datetime_obj = datetime.strptime(date_in_string, DEFAULT_DATE_FORMAT)
    meal_id = 1
    #Act
    actual_meal_preference_dtos = meal_storage.get_meal_preference(
        meal_id=meal_id
    )
    #Assert
    assert actual_meal_preference_dtos == meal_data_dtos