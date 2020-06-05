import pytest
from unittest.mock import create_autospec
from datetime import datetime
from freezegun import freeze_time
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.constants.enums import TypeOfMeal
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.get_meal_preference_interactor import \
    MealInteractor

@freeze_time('2020-02-12')
def test_set_meal_preference_type_with_valid_details(
        set_meal_preference_dtos, set_meal_preference_list):

    #Arrange
    meal_id = 1
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_meal_id.return_value = meal_id
    meal_storage.get_meal_preference.return_value = set_meal_preference_dtos
    presenter.get_meal_preference_response.return_value = \
        set_meal_preference_list
    interactor = MealInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    meal_type = 'Breakfast'
    date_obj = datetime
    #Act
    actual_response_list = interactor.get_meal_preference(
        meal_type=meal_type, date_obj=date_obj
    )
    #Assert
    assert actual_response_list == set_meal_preference_list
    meal_storage.get_meal_id.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    meal_storage.get_meal_preference.assert_called_once_with(
        meal_id=meal_id
    )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    presenter.get_meal_preference_response(
        meal_data_dto=set_meal_preference_dtos
    )


@freeze_time('2020-02-12')
def test_set_meal_preference_type_with_invalid_meal_id():

    #Arrange
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    meal_storage.check_if_date_has_a_meal.return_value = False
    presenter.raise_exception_for_invalid_date_for_that_meal.side_effect = NotFound
    interactor = MealInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    meal_type = 'Breakfast'
    date_obj = '2020-02-12'
    #Assert
    with pytest.raises(NotFound):
        assert  interactor.get_meal_preference(
            meal_type=meal_type, date_obj=date_obj
        )
    presenter.raise_exception_for_invalid_date_for_that_meal.assert_called_once()
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
