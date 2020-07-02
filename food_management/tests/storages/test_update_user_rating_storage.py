import pytest
from food_management.models import UserRating
from food_management.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_update_user_rating(update_rating_dtos):

    #Arrange
    storage = StorageImplementation()
    user_id = update_rating_dtos.user_id
    meal_id = update_rating_dtos.user_id

    #Act
    storage.update_user_rating(rating_dto=update_rating_dtos)

    #Assert
    userrating_obj = UserRating.objects.filter(user_id=user_id, meal_id=meal_id)
