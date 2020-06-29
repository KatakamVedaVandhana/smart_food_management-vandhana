from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_user_rating_response_return_dict(
        get_rating_dict, get_rating_dto):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_response_dict = presenter.get_user_rating_response(
        user_rating_dto=get_rating_dto
    )

    #Assert
    assert actual_response_dict == get_rating_dict