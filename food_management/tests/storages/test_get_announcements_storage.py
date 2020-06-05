import pytest
from datetime import datetime
from food_management.constants.constants import DEFAULT_DATE_FORMAT
from freezegun import freeze_time
from food_management.storages.storage_implementation import \
    StorageImplementation


@pytest.mark.django_db
@freeze_time('2020-02-12')
def test_get_announcements_returns_annoncement_dtos(annoncement_dtos):

    #Arrange
    storage = StorageImplementation()
    date_in_string = '2020-02-12'
    datetime_obj = datetime.strptime(date_in_string, DEFAULT_DATE_FORMAT)
    #Act
    actual_announcement_dtos = storage.get_announcements(date_obj=datetime_obj)
    #Assert
    assert actual_announcement_dtos == annoncement_dtos