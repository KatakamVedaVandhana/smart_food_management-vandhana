import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from food_manfood_management_auth_appagement.presenters.presenter_implementation import \
    PresenterImplementation
from food_management_auth_app.constants.exception_messages import INVALID_PASSWORD

def test_raise_exception_for_invalid_password():

    #Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD
    #Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_invalid_password()
    #Assert
    assert exception.value.message == exception_message