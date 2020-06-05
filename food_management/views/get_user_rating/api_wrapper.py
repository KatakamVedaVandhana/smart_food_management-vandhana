from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from food_management.constants.exception_messages import (
    INVALID_MEAL_ID, INVALID_DATA
)
from food_management.dtos.dtos import RatingDto, ItemAndRatingDto
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.get_user_rating_interactor import \
    GetUserRatingInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    user_id = request_data['user_id']
    meal_id = request_data['meal_id']
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    meal_storage = MealStorageImplementation()
    interactor = GetUserRatingInteractor(
        presenter=presenter,
        storage=storage,
        meal_storage=meal_storage
    )
    try:
        response = interactor.get_user_rating(
                meal_id=meal_id, user_id=user_id
            )
    except NotFound:
        response = INVALID_MEAL_ID
        json_response = json.dumps(response)
        return HttpResponse(json_response, status=404)
    except BadRequest:
        response = INVALID_DATA
        json_response = json.dumps(response)
        return HttpResponse(json_response, status=400)
    json_response = json.dumps(response)
    return HttpResponse(json_response, status=200)
