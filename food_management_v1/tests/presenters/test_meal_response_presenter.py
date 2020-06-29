from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_meal_response(meal_data_dtos, meal_data_response_dict):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_response_list = presenter.get_meal_preference_response(
        meal_data_dto=meal_data_dtos
    )

    #Assert
    assert actual_response_list == meal_data_response_dict
