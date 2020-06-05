import pytest
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

def test_get_user_rating_with_valid_details(get_rating_dto, get_rating_dict):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetUserRatingInteractor(
        presenter=presenter,
        storage=storage,
        meal_storage=meal_storage
    )
    user_id = 1
    meal_id = 1
    meal_storage.check_if_its_valid_meal_id.return_value = True
    storage.check_if_user_has_a_rating.return_value = True
    storage.get_user_rating.return_value = get_rating_dto
    presenter.get_user_rating_response.return_value = get_rating_dict

    #Act
    actual_rating_dict = interactor.get_user_rating(
        meal_id=meal_id, user_id=user_id
    )

    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
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
    invalid_meal_id = 1
    meal_storage.check_if_its_valid_meal_id.return_value = False
    presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound

    #Assert
    with pytest.raises(NotFound):
        assert interactor.get_user_rating(
                meal_id=invalid_meal_id, user_id=user_id
            )
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=invalid_meal_id
    )
    presenter.raise_exception_for_invalid_meal_id.assert_called_once()

