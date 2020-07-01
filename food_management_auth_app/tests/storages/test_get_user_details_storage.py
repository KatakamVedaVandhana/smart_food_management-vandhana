import pytest
from food_management_auth_app.models import User
from food_management_auth_app.storages.storage_implementation import \
    StorageImplementation
from food_management_auth_app.exceptions.exceptions import \
    InvalidUsername, InvalidPassword

@pytest.mark.django_db
def test_get_user_details_with_valid_details_returns_user_id(user_objs):

    #Arrange
    username = 'username1'
    password = 'ibhubs-1234'
    storage = StorageImplementation()

    #Act
    user_id, is_admin = storage.get_user_details(
        username=username, password=password
    )

    #Assert
    user_obj = User.objects.get(username=username)
    assert user_obj.id == user_id
    assert user_obj.username == username
    assert user_obj.check_password(password) is True
    assert user_obj.is_superuser == is_admin

@pytest.mark.django_db
def test_get_user_details_with_invalid_user_name_raises_error(user_objs):

    #Arrange
    invalid_username = 'username_1'
    password = 'password1'
    storage = StorageImplementation()

    #Assert
    with pytest.raises(InvalidUsername):
        assert storage.get_user_details(
            username=invalid_username, password=password
        )

@pytest.mark.django_db
def test_get_user_details_with_invalid_password(user_objs):

    #Arrange
    username = 'username1'
    invalid_password = 'password_1'
    storage = StorageImplementation()

    #Assert
    with pytest.raises(InvalidPassword):
        assert storage.get_user_details(
            username=username, password=invalid_password
        )