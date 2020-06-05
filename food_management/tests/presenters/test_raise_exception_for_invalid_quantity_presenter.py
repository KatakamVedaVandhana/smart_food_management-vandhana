import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from food_management.constants.exception_messages import INVALID_QUANTITY
from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_raise_exception_for_invalid_quantity():

    #Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_QUANTITY

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_quantity()

    #Assert
    assert exception.value.message == exception_messages