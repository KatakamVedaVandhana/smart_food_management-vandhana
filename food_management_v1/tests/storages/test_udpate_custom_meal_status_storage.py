import pytest
from food_management.models import UserMealStatus, MealCourse
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_upadte_custom_meal_status(
        item_and_quantity_dtos, meal_course_objs,
        user_meal_course_objs, custom_meal_objs):

    #Arrange
    meal_storage = MealStorageImplementation()
    user_id = 1
    meal_id = 1
    meal_course = 'Custom-meal'
    print(user_meal_course_objs)
    items_and_quantities = item_and_quantity_dtos
    print(MealCourse.objects.filter(meal_id=meal_id, meal_course=meal_course))
    #Act
    meal_storage.udpate_custom_meal_status(
        user_id=user_id, meal_id=meal_id, meal_course=meal_course,
        items_and_quantities=items_and_quantities
    )
    #Assert
    usermeal_obj = UserMealStatus.objects.filter(meal_id=meal_id, user_id=user_id)[0]
    assert usermeal_obj.id == 1
