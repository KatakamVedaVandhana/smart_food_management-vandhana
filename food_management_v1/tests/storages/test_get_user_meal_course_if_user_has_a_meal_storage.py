import pytest
from food_management.exceptions.exceptions import UserHasNoMealCourse
from food_management.models import UserMealStatus
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_get_user_meal_course_if_user_has_a_meal(user_meal_course_objs):

    #Arrange
    user_id = 1
    meal_id = 1
    expected_meal_course = 'Half-meal'
    meal_storage = MealStorageImplementation()
    #Act
    actual_meal_course = meal_storage.get_user_meal_course_if_user_has_a_meal(
        meal_id=meal_id, user_id=user_id
    )
    #Assert
    assert actual_meal_course == expected_meal_course
    usermealstatus_obj = UserMealStatus.objects.filter(meal_id=meal_id, user_id=1)[0]
    assert usermealstatus_obj.meal_course.meal_course == expected_meal_course

@pytest.mark.django_db
def test_get_user_meal_course_if_user_has_a_mealraises_error_if_has_no_meal(
        user_meal_course_objs):

    #Arrange
    user_id = 2
    meal_id = 1
    meal_storage = MealStorageImplementation()
    #Acssert
    with pytest.raises(UserHasNoMealCourse):
        assert meal_storage.get_user_meal_course_if_user_has_a_meal(
            meal_id=meal_id, user_id=user_id
        )