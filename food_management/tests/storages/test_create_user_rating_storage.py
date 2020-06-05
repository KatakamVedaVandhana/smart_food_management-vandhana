import pytest
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.models import UserRating

@pytest.mark.django_db
def test_create_user_rating(rating_dtos):

    #Arrange
    storage = StorageImplementation()
    user_id = rating_dtos.user_id
    meal_id = rating_dtos.meal_id

    #Assert
    storage.create_user_rating(
        rating_dto=rating_dtos
    )

    #Arrange
    bool_value = UserRating.objects.filter(user_id=user_id, meal_id=meal_id).exists()
    assert bool_value is True