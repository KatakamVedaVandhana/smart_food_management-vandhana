from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_food_wastage_response(food_wastage_dict, food_wastage_dto):

    #Arrange
    presenter = PresenterImplementation()

    #Act
    actual_food_wastage_dict = presenter.get_food_wastage_response(
        food_wastage_dto=food_wastage_dto
    )

    #Assert
    assert actual_food_wastage_dict == food_wastage_dict