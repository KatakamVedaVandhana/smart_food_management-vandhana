from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django_swagger_utils.drf_server.exceptions import BadRequest
from django.http import HttpResponse
import json
from .validator_class import ValidatorClass
from food_management.constants.exception_messages import INVALID_DATA
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.interactors.get_home_page_interactor import \
    HomePageInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print(kwargs['user'].__dict__)
    u
    request_data = kwargs['request_data']
    meal_storage = MealStorageImplementation()
    presenter = PresenterImplementation()
    interactor = HomePageInteractor(meal_storage=meal_storage, presenter=presenter)
    try:
        response_dict = \
        interactor.get_home_page(
            date_obj=request_data['date'], user_id=request_data['user_id']
        )
    except BadRequest:
        response_dict = INVALID_DATA
        response = json.dumps(response_dict, indent=4)
        return HttpResponse(response, status=400)

    # except NotFound:
    #     response_dict = INVALID_USER
    #     response = json.dumps(response_dict)
    response = json.dumps(response_dict, indent=4)
    return HttpResponse(response, status=200)