from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management_auth_app.models.user import User
from food_management_auth_app.exceptions.exceptions import InvalidUsername
import pytest

@pytest.mark.django_db
def test_validate_username_with_valid_username(user_objs):

    #Arrange
    username = 'user1'
    storage = StorageImplementation()

    #Act
    storage.validate_username(username=username)

    #Assert
    user_obj = User.objects.get(username=username)
    assert user_obj.username == username

@pytest.mark.django_db
def test_validate_username_with_invalid_username_raises_error(user_objs):

    #Arrange
    invalid_username = 'user_1'
    storage = StorageImplementation()

    #Assert
    with pytest.raises(InvalidUsername):
        assert storage.validate_username(username=invalid_username)
