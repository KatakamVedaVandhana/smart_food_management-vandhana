from food_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_home_page_response(home_page_dto, home_page_response_dict):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_response_dict = presenter.get_home_page_response(
        home_page_dto=home_page_dto
    )

    #Assert
    assert actual_response_dict == home_page_response_dict