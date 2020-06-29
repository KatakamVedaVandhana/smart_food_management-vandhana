import pytest
from datetime import datetime
from freezegun import freeze_time
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import BadRequest
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.interactors.get_home_page_interactor import \
    HomePageInteractor
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

@freeze_time('2020-02-12')
def test_get_home_page_with_valid_details(home_page_dto, home_page_dict):

    #Arrange
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    meal_storage.check_if_date_has_meals.return_value = True
    meal_storage.get_home_page.return_value = home_page_dto
    interactor = HomePageInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    presenter.get_home_page_response.return_value=home_page_dict
    user_id=1
    date_obj = datetime.now()
    #Act
    actual_response_dict = interactor.get_home_page(
        date_obj=date_obj, user_id=user_id
    )

    #Assert
    assert home_page_dict == actual_response_dict
    meal_storage.check_if_date_has_meals.assert_called_once_with(
        date_obj=date_obj
    )
    meal_storage.get_home_page.assert_called_once_with(
        date_obj=date_obj, user_id=user_id)
    presenter.get_home_page_response.assert_called_once_with(
        home_page_dto=home_page_dto
    )


def test_get_home_page_with_invalid_date_time():

    #Arrange
    meal_storage = create_autospec(MealStorageInterface)
    presenter = create_autospec(PresenterInterface)
    meal_storage.check_if_date_has_meals.return_value = False
    presenter.raise_exception_for_invalid_date.side_effect = BadRequest
    interactor = HomePageInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    datetime_string = '2020-02-12'
    user_id=1

    #Assert
    with pytest.raises(BadRequest):
        assert interactor.get_home_page(
            date_obj=datetime_string, user_id=user_id
        )
    presenter.raise_exception_for_invalid_date.assert_called_once()
    meal_storage.check_if_date_has_meals.assert_called_once_with(
        date_obj=datetime_string
    )
