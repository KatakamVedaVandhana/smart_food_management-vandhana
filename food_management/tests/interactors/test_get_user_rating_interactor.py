import pytest
from freezegun import freeze_time
from datetime import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from food_management.interactors.get_user_rating_interactor import \
    GetUserRatingInteractor
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

@freeze_time('2020-02-12')
def test_get_user_rating_with_valid_details(get_rating_dto, get_rating_dict):

    #Arrange
    meal_id = 1
    meal_type = 'Breakfast'
    date_obj = datetime.now()
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetUserRatingInteractor(
        presenter=presenter,
        storage=storage,
        meal_storage=meal_storage
    )
    user_id = 1
    meal_storage.check_if_date_has_a_meal.return_value = True
    storage.check_if_user_has_a_rating.return_value = True
    meal_storage.get_meal_id.return_value = meal_id
    storage.get_user_rating.return_value = get_rating_dto
    presenter.get_user_rating_response.return_value = get_rating_dict

    #Act
    actual_rating_dict = interactor.get_user_rating(
       meal_type=meal_type, date_obj=date_obj, user_id=user_id
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
         meal_type=meal_type, date_obj=date_obj
    )
    storage.check_if_user_has_a_rating.assert_called_once_with(
        meal_id=meal_id, user_id=user_id
    )
    storage.get_user_rating.assert_called_once_with(
        meal_id=meal_id, user_id=user_id
    )
    presenter.get_user_rating_response.assert_called_once_with(
        user_rating_dto=get_rating_dto
    )
    assert actual_rating_dict == get_rating_dict


@freeze_time('2020-02-12')
def test_get_user_rating_with_invalid_meal_id_raises_error():

    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetUserRatingInteractor(
        presenter=presenter,
        storage=storage,
        meal_storage=meal_storage
    )
    user_id = 1
    meal_type = 'Breakfast'
    date_obj = datetime.now()
    meal_storage.check_if_date_has_a_meal.return_value = False
    presenter.raise_exception_for_invalid_date_for_that_meal.side_effect = NotFound

    #Assert
    with pytest.raises(NotFound):
        assert interactor.get_user_rating(
                meal_type=meal_type, date_obj=date_obj,user_id=user_id
            )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
         meal_type=meal_type, date_obj=date_obj
    )
    presenter.raise_exception_for_invalid_date_for_that_meal.assert_called_once()

