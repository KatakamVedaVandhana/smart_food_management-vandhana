from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_announcement_response(
        announcement_dtos, announcement_response_list):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_response_list = presenter.get_announcements_response(
        announcement_dtos=announcement_dtos
    )

    #Assert
    assert actual_response_list == announcement_response_list