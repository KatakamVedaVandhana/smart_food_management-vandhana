import pytest

from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from food_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from food_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management_auth.interactors.get_user_dtos import GetUserDtosInteractor

def test_get_user_dtos_with_invalid_user_ids_raise_exception():

    #Arrange
    invalid_user_ids = [1,2,3]
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetUserDtosInteractor(storage=storage)
    storage.validate_user_ids.return_value = False
    presenter.raise_exception_for_invalid_user_ids.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_user_dtos_wrapper(presenter=presenter, user_ids=invalid_user_ids)

    #Assert
    storage.validate_user_ids.assert_called_once_with(user_ids=invalid_user_ids)
    presenter.raise_exception_for_invalid_user_ids.assert_called_once()