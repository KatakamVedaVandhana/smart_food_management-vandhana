import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import create_autospec
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.get_meal_head_count_interactor import \
    GetMealHeadCountInteractor

@freeze_time('2020-02-12')
def test_get_meal_head_count_with_valid_details(
        head_count_dto, head_count_dict):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = GetMealHeadCountInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_meal_head_count.return_value = head_count_dto
    presenter.get_meal_head_count_response.return_value = head_count_dict
    meal_type = 'Breakfast'
    date_obj = datetime.now()

    #Act
    actual_head_count_dict = interactor.get_meal_head_count(
        meal_type=meal_type, date_obj=date_obj
    )

    #Assert
    assert actual_head_count_dict == head_count_dict
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    meal_storage.get_meal_head_count.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    presenter.get_meal_head_count_response.assert_called_once_with(
        head_count_dto=head_count_dto
    )

@freeze_time('2020-02-12')
def test_get_meal_head_count_with_invalid_details(
        head_count_dto, head_count_dict):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = GetMealHeadCountInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = False
    presenter.raise_exception_for_invalid_date_for_that_meal.side_effect = NotFound
    meal_type = 'Breakfast'
    date_obj = datetime.now()

    #Assert
    with pytest.raises(NotFound):
        assert interactor.get_meal_head_count(
            meal_type=meal_type, date_obj=date_obj
        )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    presenter.raise_exception_for_invalid_date_for_that_meal.assert_called_once()
