import pytest
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_get_items_list(list_of_items_dtos):
    #Arrange
    meal_storage = MealStorageImplementation()
    #Act
    actual_items_list_dto = meal_storage.get_items_list()
    #Assert
    assert actual_items_list_dto == list_of_items_dtos