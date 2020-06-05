import pytest
from food_management.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_check_if_user_has_a_rating_return_false_if_user_has_no_rating(
        user_objs, meal_objs):

    #Arrange
    storage = StorageImplementation()
    meal_id = 1
    user_id = 1

    #Assert
    actual_bool_value = storage.check_if_user_has_a_rating(
        user_id=user_id, meal_id=meal_id
    )

    #Act
    assert actual_bool_value is False

@pytest.mark.django_db
def test_check_if_user_has_a_rating_return_true_if_user_has_no_rating(
        user_rating_objs):

    #Arrange
    storage = StorageImplementation()
    meal_id = 1
    user_id = 1

    #Assert
    actual_bool_value = storage.check_if_user_has_a_rating(
        user_id=user_id, meal_id=meal_id
    )

    #Act
    assert actual_bool_value is True