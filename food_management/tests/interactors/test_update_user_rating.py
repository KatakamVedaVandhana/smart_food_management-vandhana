import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from unittest.mock import create_autospec
from food_management.interactors.update_user_rating_interactor import \
    UpdateUserRatingInteractor
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface

def test_get_user_rating_interactor_if_user_has_a_rating(rating_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = UpdateUserRatingInteractor(
        meal_storage=meal_storage, presenter=presenter,
        storage=storage
    )
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = True
    storage.check_if_user_has_a_rating.return_value = True
    storage.update_user_rating.return_value = None
    meal_id = rating_dtos.meal_id
    user_id = rating_dtos.user_id
    items_and_ratings = rating_dtos.items_and_ratings
    items_ids = [item.item_id for item in items_and_ratings]

    #Act
    interactor.update_user_rating(rating_dto=rating_dtos)

    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(meal_id=meal_id)
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.\
        assert_called_once_with(items_ids=items_ids, meal_id=meal_id)
    storage.check_if_user_has_a_rating.assert_called_once_with(
        user_id=user_id, meal_id=meal_id
    )
    storage.update_user_rating.assert_called_once_with(rating_dto=rating_dtos)

def test_get_user_rating_interactor_if_user_does_not_have_a_rating(rating_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = UpdateUserRatingInteractor(
        meal_storage=meal_storage, presenter=presenter,
        storage=storage
    )
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = True
    storage.check_if_user_has_a_rating.return_value = False
    storage.create_user_rating.return_value = None
    meal_id = rating_dtos.meal_id
    user_id = rating_dtos.user_id
    items_and_ratings = rating_dtos.items_and_ratings
    items_ids = [item.item_id for item in items_and_ratings]

    #Act
    interactor.update_user_rating(rating_dto=rating_dtos)

    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(meal_id=meal_id)
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.\
        assert_called_once_with(items_ids=items_ids, meal_id=meal_id)
    storage.check_if_user_has_a_rating.assert_called_once_with(
        user_id=user_id, meal_id=meal_id
    )
    storage.create_user_rating.assert_called_once_with(rating_dto=rating_dtos)


def test_get_user_rating_interactor_if_its_invalid_meal_id(rating_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = UpdateUserRatingInteractor(
        meal_storage=meal_storage, presenter=presenter,
        storage=storage
    )
    meal_id = rating_dtos.meal_id
    meal_storage.check_if_its_valid_meal_id.return_value = False
    presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        assert interactor.update_user_rating(rating_dto=rating_dtos)
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(meal_id=meal_id)

def test_get_user_rating_interactor_if_it_has_invalid_item_ids(rating_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    storage = create_autospec(StorageInterface)
    interactor = UpdateUserRatingInteractor(
        meal_storage=meal_storage, presenter=presenter,
        storage=storage
    )
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = False
    presenter.raise_exception_for_invalid_item_id.side_effect = BadRequest
    meal_id = rating_dtos.meal_id
    items_and_ratings = rating_dtos.items_and_ratings
    items_ids = [item.item_id for item in items_and_ratings]

    #Act
    with pytest.raises(BadRequest):
        assert interactor.update_user_rating(rating_dto=rating_dtos)

    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(meal_id=meal_id)
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.\
        assert_called_once_with(items_ids=items_ids, meal_id=meal_id)