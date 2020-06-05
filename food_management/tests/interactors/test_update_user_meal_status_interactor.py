import pytest
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.exceptions.exceptions import UserHasNoMealCourse
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.update_user_meal_preference_interactor import \
    UpdateUserMealPreferenceInteractor

@freeze_time('2020-02-12')
def test_update_user_meal_preference_if_user_already_has_a_meal():

    #Arrange
    old_meal_course_type = 'Full-meal'
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_meal_id.return_value = 1
    meal_storage.get_user_meal_course_if_user_has_a_meal.return_value = old_meal_course_type
    meal_storage.update_user_meal_status.return_value = None
    interactor = UpdateUserMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = 1
    user_id = 1
    meal_type = 'Breakfast'
    date_obj = datetime.now()
    new_meal_course_type = 'Half-meal'

    #Act
    interactor.update_user_meal_preference(
        meal_type=meal_type, user_id=user_id, meal_course=new_meal_course_type,
        date_obj=date_obj
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
         meal_type=meal_type, date_obj=date_obj
    )
    meal_storage.get_user_meal_course_if_user_has_a_meal.assert_called_once_with(
        meal_id=meal_id, user_id=user_id
    )
    meal_storage.update_user_meal_status.assert_called_once_with(
        user_id=user_id, meal_id=meal_id, meal_course=new_meal_course_type
    )
    meal_storage.get_meal_id.assert_called_once_with(meal_type=meal_type, date_obj=date_obj)

@freeze_time('2020-02-12')
def test_update_user_meal_preference_if_user_does_not_have_a_meal():

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_user_meal_course_if_user_has_a_meal.side_effect = UserHasNoMealCourse
    meal_storage.get_meal_id.return_value = 1
    meal_storage.create_user_meal_status.return_value = None
    interactor = UpdateUserMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = 1
    user_id = 1
    meal_type = 'Breakfast'
    date_obj = datetime.now()
    new_meal_course_type = 'Half-meal'

    #Act
    interactor.update_user_meal_preference(
        meal_type=meal_type, date_obj=date_obj,
        user_id=user_id, meal_course=new_meal_course_type
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
         meal_type=meal_type, date_obj=date_obj
    )
    meal_storage.get_user_meal_course_if_user_has_a_meal.assert_called_once_with(
        meal_id=meal_id, user_id=user_id
    )
    meal_storage.create_user_meal_status.assert_called_once_with(
        user_id=user_id, meal_id=meal_id, meal_course=new_meal_course_type
    )
    meal_storage.get_meal_id.assert_called_once_with(meal_type=meal_type, date_obj=date_obj)

def test_update_user_meal_preference_if_its_invalid_meal_id():

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_date_has_a_meal.return_value = False
    presenter.raise_exception_for_invalid_date_for_that_meal.side_effect = NotFound
    interactor = UpdateUserMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    user_id = 1
    new_meal_course_type = 'Half-meal'
    meal_type = 'Breakfast'
    date_obj = datetime.now()

    #Assert
    with pytest.raises(NotFound):
        assert interactor.update_user_meal_preference(
                meal_type=meal_type, user_id=user_id, meal_course=new_meal_course_type,
                date_obj=date_obj
            )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
