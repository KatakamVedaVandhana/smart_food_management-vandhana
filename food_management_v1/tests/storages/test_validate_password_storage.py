import pytest
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.exceptions.exceptions import InvalidPassword
from food_management.models.user import User


@pytest.mark.django_db
def test_validate_password_with_valid_password(user_objs):

    #Arrange
    username= 'user1'
    password = 'password1'
    storage = StorageImplementation()

    #Act
    storage.validate_password(
        username=username, password=password
    )

    #Assert
    user_obj = User.objects.get(username=username)
    assert user_obj.username == username
    assert user_obj.check_password(password) == True

@pytest.mark.django_db
def test_validate_password_with_invalid_password_raises_error(user_objs):

    #Arrange
    username = 'user1'
    invalid_password = 'password_1'
    storage = StorageImplementation()

    #Act
    with pytest.raises(InvalidPassword):
        assert storage.validate_password(
            username=username, password=invalid_password
        )
