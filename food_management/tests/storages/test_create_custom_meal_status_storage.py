import pytest
from food_management.models import UserMealStatus, MealCourse, Meal
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_create_custom_meal_status(
        custom_meal_upadte_dto):

    #Arrange

    meal_id = 1
    meal_storage = MealStorageImplementation()
    user_id = custom_meal_upadte_dto.user_id
    meal_type = custom_meal_upadte_dto.meal_type
    date_obj = custom_meal_upadte_dto.date
    meal_course = custom_meal_upadte_dto.meal_course
    items_and_quantities = custom_meal_upadte_dto.items_and_quantities
    #Act
    meal_storage.create_custom_meal_status(
        user_id=user_id, meal_id=meal_id, meal_course=meal_course,
        items_and_quantities=items_and_quantities
    )
    #Assert
    meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
    usermeal_obj = UserMealStatus.objects.filter(
        meal_id=meal_obj.id, user_id=user_id)[0]
    usermeal_obj.id == 1

