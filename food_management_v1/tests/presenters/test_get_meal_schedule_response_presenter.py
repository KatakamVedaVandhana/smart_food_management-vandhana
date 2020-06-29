from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_meal_schedule_response(meal_schedule_dto, meal_schedule_dict):

    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_response_dict = presenter.get_meal_schedule_response(meal_schedule_dto)
    #Assert
    assert actual_response_dict == meal_schedule_dict