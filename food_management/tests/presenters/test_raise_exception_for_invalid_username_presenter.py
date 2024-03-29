import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.constants.exception_messages import INVALID_USERNAME

def test_raise_exception_for_invalid_username():

    #Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_USERNAME
    #Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_invalid_username()
    #Assert
    assert exception.value.message == exception_message