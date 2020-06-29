from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django_swagger_utils.drf_server.exceptions import NotFound
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse
from food_management.constants.exception_messages import INVALID_MEAL_ID
from food_management.interactors.get_meal_preference_interactor import \
    MealInteractor
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    user_id = kwargs['user'].id
    meal_type = request_data['meal_type']
    date = request_data['date']
    meal_storage = MealStorageImplementation()
    presenter = PresenterImplementation()
    interactor = MealInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    response_data = interactor.get_meal_preference(
        meal_type=meal_type, date_obj=date, user_id=user_id
    )
    response = json.dumps(response_data, indent=4)
    return HttpResponse(response, status=200)