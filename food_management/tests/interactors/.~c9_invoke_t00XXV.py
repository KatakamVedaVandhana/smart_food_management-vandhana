import pytest
from food_management.interactors.login_interactor import LoginInteractor
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import InvalidUsername
from django_swagger_utils.drf_server.exceptions import NotFound
from common.oauth2_storage import OAuth2SQLStorage
from unittest.mock import create_autospec

@pytest.mark.django_db
def test_login_with_valid_details(
        user_auth_token_dto, login_details_response_dict, user_objs):

    #Arrange
    username = 'user1'
    password = 'password1'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    storage.validate_username.return_value = None
    storage.validate_password.return_value = True
    storage.get_user_details.return_value = 1
    interactor = LoginInteractor(
        storage=storage, presenter=presenter, oauth_storage=oauth_storage
    )
    expected_dict = login_details_response_dict
    presenter.login_user_details_response.return_value = expected_dict

    #Act
    response_dict = interactor.login(username=username, password=password)

    #Assert
    assert response_dict == expected_dict
    storage.validate_username.assert_called_once_with(username=username)
    storage.validate_password.assert_called_once_with(
        username=username, password=password
    )
    storage.get_user_details.assert_called_once_with(
        username=username, password=password
    )
    presenter.login_user_details_response(token_dto=user_auth_token_dto)

@pytest.mark.django_db
def test_login_with_invalid_username(
        user_objs):

    #Arrange
    username = 'user_1'
    password = 'password'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    storage.validate_username.side_effect = InvalidUsername
    presenter.raise_exception_for_invalid_username.side_effect = NotFound
    interactor = LoginInteractor(
        storage=storage, presenter=presenter, oauth_storage=oauth_storage
    )

    #Assert
    with pytest.raises(InvalidUsername):
        interactor.login(username=username, password=password)
    storage.validate_username.assert_called_once_with(username=username)
    