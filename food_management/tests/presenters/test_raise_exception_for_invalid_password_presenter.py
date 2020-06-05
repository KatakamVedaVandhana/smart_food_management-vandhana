import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.constants.exception_messages import INVALID_PASSWORD

def test_raise_exception_for_invalid_password():

    #Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD
    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_password()
    #Assert
    assert exception.value.message == exception_message