import pytest
from food_management.interactors.login_interactor import LoginInteractor
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import \
    InvalidUsername, InvalidPassword
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from unittest.mock import create_autospec
from unittest.mock import Mock


def test_login_with_valid_details(
        user_auth_token_dto, login_details_response_dict,
        application_dto, access_token_dto,
        refresh_token_dto):

    #Arrange
    username = 'user1'
    password = 'password1'
    is_admin = False
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    oauth_storage.get_or_create_default_application.return_value = \
        application_dto, True
    oauth_storage.create_access_token.return_value = access_token_dto
    oauth_storage.create_refresh_token.return_value = refresh_token_dto
    storage.validate_username.return_value = None
    storage.validate_password.return_value = True
    storage.get_user_details.return_value = 1, is_admin
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
    oauth_storage.get_or_create_default_application.assert_called_once_with(
        user_id=1
    )
    presenter.login_user_details_response(token_dto=user_auth_token_dto, is_admin=is_admin)


def test_login_with_invalid_username(application_dto, access_token_dto,
        refresh_token_dto):

    #Arrange
    invalid_username = 'user_1'
    password = 'password'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    oauth_storage.get_or_create_default_application.return_value = \
        application_dto, True
    oauth_storage.create_access_token.return_value = access_token_dto
    oauth_storage.create_refresh_token.return_value = refresh_token_dto
    storage.validate_username.side_effect = InvalidUsername
    presenter.raise_exception_for_invalid_username.side_effect = NotFound
    interactor = LoginInteractor(
        storage=storage, presenter=presenter, oauth_storage=oauth_storage
    )

    #Assert
    with pytest.raises(NotFound):
        assert interactor.login(
            username=invalid_username, password=password
        )
    storage.validate_username.assert_called_once_with(
        username=invalid_username
    )
    presenter.raise_exception_for_invalid_username.assert_called_once()


def test_login_with_invalid_password(application_dto, access_token_dto,
        refresh_token_dto):

    #Arrange
    username = 'user1'
    invalid_password = 'password_1'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    oauth_storage.get_or_create_default_application.return_value = \
        application_dto, True
    oauth_storage.create_access_token.return_value = access_token_dto
    oauth_storage.create_refresh_token.return_value = refresh_token_dto
    storage.validate_username.return_value = None
    storage.validate_password.side_effect = InvalidPassword
    presenter.raise_exception_for_invalid_password.side_effect = BadRequest
    interactor = LoginInteractor(
        storage=storage, presenter=presenter, oauth_storage=oauth_storage
    )

    #Assert
    with pytest.raises(BadRequest):
        assert interactor.login(username=username, password=invalid_password)
    storage.validate_username.assert_called_once_with(username=username)
    storage.validate_password.assert_called_once_with(
        username=username, password=invalid_password
    )
    presenter.raise_exception_for_invalid_password.assert_called_once()