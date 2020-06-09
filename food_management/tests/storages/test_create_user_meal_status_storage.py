import pytest
from food_management.models import (
    UserMealStatus, MealCourse
)
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_create_user_meal_status(user_meal_course_objs):

    #Arrange
    user_id=2
    meal_course = 'Half-meal'
    meal_id = 1
    meal_storage = MealStorageImplementation()
    #Aact
    meal_storage.create_user_meal_status(
        user_id=user_id, meal_course=meal_course, meal_id=meal_id
    )
    #Act
    meal_course_obj = MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course)[0]
    usermealcourse_obj = UserMealStatus.objects.filter(meal_id=meal_id, user_id=user_id)[0]
    assert usermealcourse_obj.meal_course == meal_course_obj
