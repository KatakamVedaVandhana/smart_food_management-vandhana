import pytest

from unittest.mock import create_autospec

from food_management_auth_app.interactors.storages.storage_interface import \
    StorageInterface
from food_management_auth_app.interactors.get_user_dtos import \
    GetUserDtosInteractor
from food_management_auth_app.exceptions.exceptions import InvalidUserIds
from food_management_auth_app.interactors.storages.dtos import UserDetailsDto

def test_get_user_dtos_with_invalid_user_ids_raise_exception():

    #Arrange
    invalid_user_ids = [1,2,6]
    storage = create_autospec(StorageInterface)
    interactor = GetUserDtosInteractor(storage=storage)
    storage.get_user_ids.return_value = [1,2,3,4,5]

    #Act
    with pytest.raises(Exception) as exception:
        interactor.get_user_dtos(user_ids=invalid_user_ids)

    #Assert
    storage.get_user_ids.assert_called_once()


def test_get_user_dtos_with_valid_details_return_user_dtos(user_dtos):

    #Arrange
    user_ids = [1,2]
    storage = create_autospec(StorageInterface)
    interactor = GetUserDtosInteractor(storage=storage)
    storage.get_user_ids.return_value = [1,2,3,4,5]
    storage.get_user_dtos.return_value = user_dtos

    #Act
    actual_user_dtos = interactor.get_user_dtos(user_ids=user_ids)

    #Assert
    storage.get_user_ids.assert_called_once()
    storage.get_user_dtos.assert_called_once_with(user_ids=user_ids)
    assert actual_user_dtos == user_dtos
