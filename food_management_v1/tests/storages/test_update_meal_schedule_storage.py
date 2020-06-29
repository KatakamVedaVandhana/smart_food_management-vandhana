import pytest
from food_management.models import MealCourse, Meal
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
def test_update_meal_schedule(update_meal_schedule_dtos):

    #Arrange
    meal_storage = MealStorageImplementation()
    meal_type = update_meal_schedule_dtos.meal_type
    date_obj = update_meal_schedule_dtos.date

    #Act
    meal_storage.update_meal_schedule(
        update_meal_schedule_dto=update_meal_schedule_dtos
    )

    #Assert
    meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
    meal_course_objs = MealCourse.objects.filter(meal=meal_obj)