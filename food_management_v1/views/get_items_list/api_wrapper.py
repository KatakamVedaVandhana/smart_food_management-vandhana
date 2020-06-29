from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
import json
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.interactors.get_items_list_interactor import \
    GetItemsListInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = GetItemsListInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    response = interactor.get_items_list()
    json_response = json.dumps(response, indent=4)
    return HttpResponse(json_response, status=200)