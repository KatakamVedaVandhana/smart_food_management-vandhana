import pytest
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_check_if_item_exits_return_true_for_valid_items(item_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    valid_items_ids = [1,2,3]

    #Act
    bool_value = meal_storage.check_if_item_exits(item_ids=valid_items_ids)

    #Assert
    assert bool_value is True

@pytest.mark.django_db
def test_check_if_item_exits_return_false_for_invalid_items(item_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    valid_items_ids = [-10,11,12]

    #Act
    bool_value = meal_storage.check_if_item_exits(item_ids=valid_items_ids)

    #Assert
    assert bool_value is False