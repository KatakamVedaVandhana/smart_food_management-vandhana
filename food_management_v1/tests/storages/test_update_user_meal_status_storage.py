import pytest
from food_management.models import MealCourse, UserMealStatus
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_update_user_meal_status(user_meal_course_objs):

    #Arrange
    user_id = 1
    meal_id = 1
    meal_course = 'Half-meal'
    meal_storage = MealStorageImplementation()

    #Act
    meal_storage.update_user_meal_status(
        user_id=user_id, meal_id=meal_id, meal_course=meal_course
    )

    #Assert
    meal_objs = MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)
    user_objs = UserMealStatus.objects.filter(user_id=user_id, meal_id=meal_id)
    #assert meal_objs[0].id == user_objs[0]._id