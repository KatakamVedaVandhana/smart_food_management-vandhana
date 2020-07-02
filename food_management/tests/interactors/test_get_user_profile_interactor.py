from unittest.mock import create_autospec
from unittest.mock import patch

from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.get_user_profile_interactor import \
    GetUserProfileInteractor
from food_management.adapters.auth_service import AuthService


@patch.object(AuthService, 'interface')
def test_get_user_profile_return_user_dtos(
        auth_service, expected_user_profile_dtos_response, user_profile_dtos):

    #Arrange
    user_id = 1
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserProfileInteractor()
    presenter.get_user_dtos_response.return_value = \
        expected_user_profile_dtos_response
    auth_service.get_user_dtos.return_value = user_profile_dtos

    #Act
    actual_response = interactor.get_user_profile_wrapper(
        user_id=user_id, presenter=presenter
    )

    #Assert
    auth_service.get_user_dtos.assert_called_once_with(user_ids=[user_id])
    assert actual_response == expected_user_profile_dtos_response