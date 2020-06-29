from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.constants.exception_messages import INVALID_DATA
from food_management.presenters.presenter_implementation import \
    PresenterImplementation


def raise_exception_for_invalid_date_for_that_meal():

    #Ararnge
    presenter = PresenterImplementation()
    exception_message = INVALID_DATA

    #Act
    #with pytest.raises()
    
    #Assert