import pytest
from freezegun import freeze_time
from datetime import datetime
from food_management.constants.constants import (
    BREAKFAST_START_TIME, BREAKFAST_END_TIME
)
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from unittest.mock import create_autospec
from food_management.dtos.dtos import UpdateMealScheduleDto
from food_management.interactors.update_meal_schedule_interactor import \
    UpdateMealScheduleInteractor
from food_management.interactors.storages.meal_storage_interface import \
    MealStorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface

@freeze_time('2020-02-12')
def test_update_meal_schedule_with_valid_details(
        update_meal_schedule_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = UpdateMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = True
    meal_storage.check_if_item_exits.return_value = True
    meal_storage.update_meal_schedule.return_value = None
    meal_type = update_meal_schedule_dtos.meal_type
    items = update_meal_schedule_dtos.items
    item_ids = {1,2,3}

    #Act
    interactor.update_meal_schedule(
        update_meal_schedule_dto=update_meal_schedule_dtos
    )

    #Assert
    meal_storage.check_if_item_exits.assert_called_once_with(
        item_ids=item_ids
    )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=update_meal_schedule_dtos.date
    )
    meal_storage.update_meal_schedule.assert_called_once_with(
        update_meal_schedule_dto=update_meal_schedule_dtos
    )

@freeze_time('2020-02-12')
def test_update_meal_schedule_with_valid_details_if_it_has_no_meal_create_meal(
        update_meal_schedule_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = UpdateMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_date_has_a_meal.return_value = False
    meal_storage.create_meal_schedule.return_value = None
    meal_storage.check_if_item_exits.return_value = True
    meal_type = update_meal_schedule_dtos.meal_type
    items = update_meal_schedule_dtos.items
    item_ids = {1,2,3}
    from_time_string = BREAKFAST_START_TIME
    to_time_string = BREAKFAST_END_TIME

    #Act
    interactor.update_meal_schedule(
        update_meal_schedule_dto=update_meal_schedule_dtos
    )

    #Assert
    meal_storage.check_if_item_exits.assert_called_once_with(
        item_ids=item_ids
    )
    meal_storage.check_if_date_has_a_meal.assert_called_once_with(
        meal_type=meal_type, date_obj=update_meal_schedule_dtos.date
    )
    meal_storage.create_meal_schedule.assert_called_once_with(
        from_time_string=from_time_string,
        to_time_string=to_time_string,
        update_meal_schedule_dto=update_meal_schedule_dtos
    )

@freeze_time('2020-02-12')
def test_update_meal_schedule_with_invalid_item_ids(update_meal_schedule_dtos):

    #Arrange
    presenter = create_autospec(PresenterInterface)
    meal_storage = create_autospec(MealStorageInterface)
    interactor = UpdateMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    meal_storage.check_if_item_exits.return_value = False
    presenter.raise_exception_for_invalid_item_id.side_effect = NotFound
    item_ids = update_meal_schedule_dtos.items
    meal_type = update_meal_schedule_dtos.meal_type
    invalid_item_ids = {1,2,3}

    #Assert
    with pytest.raises(NotFound):
        interactor.update_meal_schedule(
            update_meal_schedule_dto=update_meal_schedule_dtos
        )
    meal_storage.check_if_item_exits.assert_called_once_with(item_ids=invalid_item_ids)
    presenter.raise_exception_for_invalid_item_id.assert_called_once()
