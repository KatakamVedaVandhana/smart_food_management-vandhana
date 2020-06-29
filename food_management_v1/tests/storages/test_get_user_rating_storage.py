import pytest
from food_management.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_get_user_rating_with_valid_details(user_rating_dto):

    #Arrange
    storage = StorageImplementation()
    meal_id=1
    user_id=1

    #Act
    actual_user_rating_dto = storage.get_user_rating(meal_id=meal_id, user_id=user_id)

    #Assert
    assert actual_user_rating_dto == user_rating_dto