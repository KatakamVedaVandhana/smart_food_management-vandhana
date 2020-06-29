import pytest
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation


@pytest.mark.django_db
def test_check_if_its_valid_meal_id(meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_id = 1

    #Act
    bool_value = meal_storage.check_if_its_valid_meal_id(
            meal_id=meal_id
        )

    #Assert
    assert bool_value is True

@pytest.mark.django_db
def test_check_if_its_valid_meal_id_returns_false_if_its_invalid(meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    invalid_meal_id = -1

    #Act
    bool_value = meal_storage.check_if_its_valid_meal_id(
            meal_id=invalid_meal_id
        )

    #Assert
    assert bool_value is False