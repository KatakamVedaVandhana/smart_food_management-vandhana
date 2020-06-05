from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.get_meal_schedule_interactor import \
    GetMealScheduleInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    date = request_data['date']
    meal_type = request_data['meal_type']
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = GetMealScheduleInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    response_list = interactor.get_meal_schedule(date_obj=date,meal_type=meal_type)
    json_data = json.dumps(response_list, indent=4)
    return HttpResponse(json_data, status=200)