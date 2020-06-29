from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_items_list_response(list_of_items, list_of_items_dtos):

    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_response = presenter.get_items_list_response(
        items_list_dto=list_of_items_dtos
    )
    #Assert
    assert actual_response == list_of_items