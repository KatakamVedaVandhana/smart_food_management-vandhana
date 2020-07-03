import pytest

from food_management_auth_app.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_get_user_dtos_return_user_details(user_dtos):

    #Arrange
    storage = StorageImplementation()

    #Act
    actual_user_dtos = storage.get_user_dtos(user_ids=[1,2,3])

    #Assert
    assert actual_user_dtos == user_dtos