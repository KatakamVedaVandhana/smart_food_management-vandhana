from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_user_dtos_response_returns_dict(
        expected_user_profile_dtos_response, user_profile_dtos):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_response = presenter.get_user_dtos_response(user_dto=user_profile_dtos)

    #Assert
    assert actual_response == expected_user_profile_dtos_response