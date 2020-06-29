import pytest

from food_management_auth_app.models import User
from food_management_auth_app.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_get_user_ids_returns_user_ids():

    #Arrange
    storage = StorageImplementation()
    expected_user_ids = list(User.objects.all().values_list('id', flat=True))

    #Act
    user_ids = storage.get_user_ids()

    #Assert
    assert user_ids == expected_user_ids
