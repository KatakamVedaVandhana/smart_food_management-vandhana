import pytest
from datetime import datetime
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.models import UserRating, Meal

@pytest.mark.django_db
def test_create_user_rating(rating_dtos):

    #Arrange
    storage = StorageImplementation()
    user_id = rating_dtos.user_id
    meal_type = rating_dtos.meal_type
    date_obj = rating_dtos.date

    #Assert
    storage.create_user_rating(
        rating_dto=rating_dtos
    )

    #Arrange
    meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
    bool_value = UserRating.objects.filter(user_id=user_id, meal_id=meal_obj.id).exists()
    assert bool_value is True