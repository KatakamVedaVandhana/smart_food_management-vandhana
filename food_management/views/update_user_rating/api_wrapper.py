from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from food_management.constants.exception_messages import (
    INVALID_ITEM_ID, INVALID_MEAL_ID
)
from food_management.dtos.dtos import RatingDto, ItemAndRatingDto
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.update_user_rating_interactor import \
    UpdateUserRatingInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user'].id
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    meal_storage = MealStorageImplementation()
    request_data = kwargs['request_data']
    user_id = request_data['user_id']
    meal_id = request_data['meal_id']
    description = request_data['description']
    items_and_ratings = request_data['items_and_ratings']
    items_and_ratings_dtos = []
    for item_and_rating in items_and_ratings:
        items_and_ratings_dtos.append(
            ItemAndRatingDto(
                item_id=item_and_rating['item_id'],
                quality=item_and_rating['quality'],
                taste=item_and_rating['taste']
            )
        )
    rating_dto = RatingDto(
        meal_id=meal_id,
        user_id=user_id,
        items_and_ratings=items_and_ratings_dtos,
        description=description
    )
    interactor = UpdateUserRatingInteractor(
        storage=storage, presenter=presenter,
        meal_storage=meal_storage
    )
    try:
        interactor.update_user_rating(rating_dto=rating_dto)
    except BadRequest:
        response = INVALID_ITEM_ID
        json_response = json.dumps(response)
        return HttpResponse(json_response, status=400)
    except NotFound:
        response = INVALID_MEAL_ID
        json_response = json.dumps(response)
        return HttpResponse(json_response, status=404)
    return HttpResponse(status=200)