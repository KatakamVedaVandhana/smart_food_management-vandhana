from unittest.mock import create_autospec
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.get_items_list_interactor import \
    GetItemsListInteractor

def test_get_items_list(list_of_items_dtos, list_of_items):
    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    meal_storage.get_items_list.return_value = list_of_items_dtos
    presenter.get_items_list_response.return_value = list_of_items
    interactor = GetItemsListInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    #Act
    actual_items_list = interactor.get_items_list()
    ##Assert
    assert actual_items_list == list_of_items
    meal_storage.get_items_list.assert_called_once()
    presenter.get_items_list_response.assert_called_once_with(
        items_list_dto=list_of_items_dtos
    )