import pytest
from food_management.constants.exception_messages import INVALID_MEAL_COURSE
from django_swagger_utils.drf_server.exceptions import BadRequest
from food_management.presenters.presenter_implementation import \
    PresenterImplementation

def test_raise_exception_for_invalid_course_type():

    #Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_MEAL_COURSE

    #Assert
    with pytest.raises(BadRequest) as exception:
        assert presenter.raise_exception_for_invalid_course_type()
    assert exception.value.message == exception_messages