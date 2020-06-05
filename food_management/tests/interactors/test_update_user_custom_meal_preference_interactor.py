import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.update_custom_meal_preference_interactor import \
    UpdateUserCustomMealPreferenceInteractor

def test_update_user_custom_meal_preference(custom_meal_upadte_dto):
    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_user_has_a_meal.return_value = True
    meal_storage.udpate_custom_meal_status.return_value = None
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = True
    interactor = UpdateUserCustomMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = custom_meal_upadte_dto.meal_id
    user_id = custom_meal_upadte_dto.user_id
    meal_course = custom_meal_upadte_dto.meal_course
    items_and_quantities = custom_meal_upadte_dto.items_and_quantities
    items_ids = [item.item_id for item in items_and_quantities]
    #Act
    interactor.update_user_custom_meal_preference(
        custom_meal_preference_dto=custom_meal_upadte_dto
        )
    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    meal_storage.check_if_user_has_a_meal.assert_called_once_with(
        user_id=user_id, meal_id=meal_id
    )
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.assert_called_once_with(
        items_ids=items_ids, meal_id=meal_id
    )
    meal_storage.udpate_custom_meal_status.assert_called_once_with(
        user_id=user_id, meal_id=meal_id, meal_course=meal_course,
        items_and_quantities=items_and_quantities
    )

def test_update_user_custom_meal_preference_if_user_has_no_meal(custom_meal_upadte_dto):
    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_user_has_a_meal.return_value = False
    meal_storage.create_custom_meal_status.return_value = None
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = True
    interactor = UpdateUserCustomMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = custom_meal_upadte_dto.meal_id
    user_id = custom_meal_upadte_dto.user_id
    meal_course = custom_meal_upadte_dto.meal_course
    items_and_quantities = custom_meal_upadte_dto.items_and_quantities
    items_ids = [item.item_id for item in items_and_quantities]
    #Act
    interactor.update_user_custom_meal_preference(
        custom_meal_preference_dto=custom_meal_upadte_dto
        )
    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    meal_storage.check_if_user_has_a_meal.assert_called_once_with(
        user_id=user_id, meal_id=meal_id
    )
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.assert_called_once_with(
        items_ids=items_ids, meal_id=meal_id
    )
    meal_storage.create_custom_meal_status.assert_called_once_with(
        user_id=user_id, meal_id=meal_id, meal_course=meal_course,
        items_and_quantities=items_and_quantities
    )


def test_update_user_custom_meal_preference_if_invalid_item_given_raises_error(
        custom_meal_upadte_dto):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = False
    presenter.raise_exception_for_invalid_item_id.side_effect = BadRequest
    interactor = UpdateUserCustomMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = custom_meal_upadte_dto.meal_id
    items_and_quantities = custom_meal_upadte_dto.items_and_quantities
    items_ids = [item.item_id for item in items_and_quantities]
    #Act
    with pytest.raises(BadRequest):
        interactor.update_user_custom_meal_preference(
            custom_meal_preference_dto=custom_meal_upadte_dto
            )
    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.assert_called_once_with(
        items_ids=items_ids, meal_id=meal_id
    )

def test_update_user_custom_meal_preference_with_invalid_meal_ids_raises_error(
        custom_meal_upadte_dto):
    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_its_valid_meal_id.return_value = False
    presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound
    interactor = UpdateUserCustomMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    invalid_meal_id = 1
    with pytest.raises(NotFound):
        interactor.update_user_custom_meal_preference(
            custom_meal_preference_dto=custom_meal_upadte_dto
            )
    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=invalid_meal_id
    )

def test_update_user_custom_meal_preference_with_invalid_quantites_raises_error(
        custom_meal_dto_with_invalid_quantity):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.check_if_its_valid_meal_id.return_value = True
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.return_value = True
    presenter.raise_exception_for_invalid_quantity.side_effect = BadRequest
    interactor = UpdateUserCustomMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_id = custom_meal_dto_with_invalid_quantity.meal_id
    items_and_quantities = custom_meal_dto_with_invalid_quantity.items_and_quantities
    items_ids = [item.item_id for item in items_and_quantities]

    #Act
    with pytest.raises(BadRequest):
        interactor.update_user_custom_meal_preference(
            custom_meal_preference_dto=custom_meal_dto_with_invalid_quantity
        )

    #Assert
    meal_storage.check_if_its_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    meal_storage.check_if_it_has_valid_item_ids_for_that_meal.assert_called_once_with(
        items_ids=items_ids, meal_id=meal_id
    )
    presenter.raise_exception_for_invalid_quantity.assert_called_once()