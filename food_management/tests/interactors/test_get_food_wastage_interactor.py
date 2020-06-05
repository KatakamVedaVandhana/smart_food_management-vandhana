from unittest.mock import create_autospec
from freezegun import freeze_time
from datetime import datetime
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.get_food_wastage_interactor import \
    GetFoodWastageInteractor

@freeze_time('2020-02-12')
def test_get_food_wastage_with_valid_details_return_dict(
        food_wastage_dto, food_wastage_dict):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = GetFoodWastageInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_type = 'Breakfast'
    date_obj = datetime.now()
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_food_wastage.return_value = food_wastage_dto
    presenter.get_food_wastage_response.return_value = food_wastage_dict

    #Act
    actual_food_wastage_dict = interactor.get_food_wastage(
        meal_type=meal_type, date_obj=date_obj
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    meal_storage.get_food_wastage.assert_called_once_with(
        meal_type=meal_type, date_obj=date_obj
    )
    presenter.get_food_wastage_response.assert_called_once_with(
        food_wastage_dto=food_wastage_dto
    )
    assert actual_food_wastage_dict == food_wastage_dict