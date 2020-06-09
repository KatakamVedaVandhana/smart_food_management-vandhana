import pytest
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_check_if_it_has_valid_item_ids_for_that_meal_return_true_for_valid_item_ids(
        meal_course_objs, item_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_id = 1
    items_ids = [1,2,3]

    #act
    bool_value = meal_storage.check_if_it_has_valid_item_ids_for_that_meal(
        items_ids=items_ids, meal_id=meal_id
    )

    #Assert
    assert bool_value is True

@pytest.mark.django_db
def test_check_if_it_has_valid_item_ids_for_that_meal_returns_false_for_valid_item_ids(
        meal_course_objs, item_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_id = 3
    items_ids = [1,2,-3]

    #act
    bool_value = meal_storage.check_if_it_has_valid_item_ids_for_that_meal(
        items_ids=items_ids, meal_id=meal_id
    )

    #Assert
    assert bool_value is False