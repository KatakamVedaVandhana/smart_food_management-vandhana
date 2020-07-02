import pytest
from freezegun import freeze_time
from datetime import datetime
from food_management.interactors.storages.dtos import HomePageDto
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation

@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_get_home_page_return_the_details_of_the_page(home_page_dto, item_objs):

    #Arrange
    storage = MealStorageImplementation()
    user_id=1

    #Act
    actual_home_page_dto = storage.get_home_page(
        date_obj=datetime.now(), user_id=user_id
    )

    #Assert
    assert actual_home_page_dto == home_page_dto

@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_get_home_page_return_empty_list_of_no_details():

    #Arrange
    storage = MealStorageImplementation()
    user_id=1
    home_page_dto = HomePageDto(
        meal_course=[],
        items=[],
        meal=[]
    )

    #Act
    actual_home_page_dto = storage.get_home_page(
        date_obj=datetime.now(), user_id=user_id
    )

    #Assert
    assert actual_home_page_dto == home_page_dto