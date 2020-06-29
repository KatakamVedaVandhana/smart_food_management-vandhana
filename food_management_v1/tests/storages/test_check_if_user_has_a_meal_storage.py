import pytest
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_check_if_user_has_a_meal_returns_true_if_it_has_a_meal(
        user_meal_course_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    user_id = 1
    meal_id = 1
    #Act
    bool_value = meal_storage.check_if_user_has_a_meal(
        user_id=user_id, meal_id=meal_id
    )
    
    #Assert
    assert bool_value == True

@pytest.mark.django_db
def test_check_if_user_has_a_meal_returns_false_if_it_has_a_meal(
        user_meal_course_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    user_id = 2
    meal_id = 1
    #Act
    bool_value = meal_storage.check_if_user_has_a_meal(
        user_id=user_id, meal_id=meal_id
    )
    
    #Assert
    assert bool_value == False