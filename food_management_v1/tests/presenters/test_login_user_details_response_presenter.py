from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_login_user_details_response_with_valid_dtos_return_dict(
        login_details_response_dict,
        user_auth_token_dto):

    #Arrange
    presenter = PresenterImplementation()
    expected_dict = login_details_response_dict
    is_admin = False

    #Act
    actual_dict = presenter.login_user_details_response(user_auth_token_dto, is_admin=is_admin)

    #Assert
    assert actual_dict['access_token'] == expected_dict['access_token']
    assert actual_dict['user_id'] == expected_dict['user_id']
    assert actual_dict['refresh_token'] == expected_dict['refresh_token']
    assert actual_dict['expires_in'] == expected_dict['expires_in']
    assert actual_dict['is_admin'] == expected_dict['is_admin']