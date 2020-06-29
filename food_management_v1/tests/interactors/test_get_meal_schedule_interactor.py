from freezegun import freeze_time
from unittest.mock import create_autospec
from datetime import datetime
from food_management.constants.constants import (
    BREAKFAST_START_TIME, BREAKFAST_END_TIME, LUNCH_END_TIME,
    LUNCH_START_TIME, DINNER_START_TIME, DINNER_END_TIME
)
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.get_meal_schedule_interactor import \
    GetMealScheduleInteractor

@freeze_time('2020-02-12')
def test_get_meal_schedule(meal_schedule_dto, meal_schedule_dict):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = GetMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.get_meal_schedule.return_value = meal_schedule_dto
    presenter.get_meal_schedule_response.return_value = meal_schedule_dict
    meal_type = 'Breakfast'

    #Arrange
    actual_schedule_dict = interactor.get_meal_schedule(
        date_obj=datetime.now(), meal_type='Breakfast'
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        date_obj=datetime.now(), meal_type=meal_type
    )
    meal_storage.get_meal_schedule.assert_called_once_with(
        meal_type=meal_type, date_obj=datetime.now()
    )
    presenter.get_meal_schedule_response.assert_called_once_with(
        meal_schedule_dto=meal_schedule_dto)
    assert actual_schedule_dict == meal_schedule_dict


@freeze_time('2020-02-12')
def test_get_meal_schedule_creates_a_new_meal_if_it_has_no_meal():

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = GetMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = False
    meal_type = 'Breakfast'

    #Act
    actual_response_list = interactor.get_meal_schedule(
        meal_type=meal_type, date_obj=datetime.now()
    )

    #Assert
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        date_obj=datetime.now(), meal_type=meal_type
    )
    actual_response_list == []