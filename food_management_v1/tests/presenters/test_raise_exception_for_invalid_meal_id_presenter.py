import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.constants.exception_messages import INVALID_MEAL_ID
from food_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_raise_exception_for_invalid_meal_id():

    #Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_MEAL_ID

    #Assert
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_invalid_meal_id()
    assert exception.value.message == exception_messages