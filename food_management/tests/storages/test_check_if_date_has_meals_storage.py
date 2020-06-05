import pytest
from datetime import datetime
from freezegun import freeze_time
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation


@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_check_if_date_has_meals_return_true_if_has_a_meal(meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    date_obj = datetime.now()

    #Act
    actual_bool_value = meal_storage.check_if_date_has_meals(
        date_obj=date_obj
    )

    #Assert
    assert actual_bool_value is True


@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_check_if_date_has_meals_return_false_if_it_does_not_have_meal():

    #Arrange
    meal_storage = MealStorageImplementation()
    date_obj = datetime.now()

    #Act
    actual_bool_value = meal_storage.check_if_date_has_meals(
        date_obj=date_obj
    )

    #Assert
    assert actual_bool_value is False
