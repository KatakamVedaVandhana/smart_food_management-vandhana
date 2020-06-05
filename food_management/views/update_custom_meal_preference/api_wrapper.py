from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django.http import HttpResponse
import json
from food_management.constants.exception_messages import INVALID_ITEM_ID, INVALID_MEAL_ID
from food_management.interactors.update_custom_meal_preference_interactor import \
    UpdateUserCustomMealPreferenceInteractor
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.dtos.dtos import CustomeMealUpdateDto, ItemAndQuantityDto

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    user_id = request_data['user_id']
    meal_course = request_data['meal_course']
    meal_id = request_data['meal_id']
    print(kwargs['request_data'])
    print("\n")
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = UpdateUserCustomMealPreferenceInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    list_of_item_and_quantity_dtos = []
    for item_and_quantity in request_data['items_and_quantities']:
        print(item_and_quantity)
        print("\n"*5)
        list_of_item_and_quantity_dtos.append(
            ItemAndQuantityDto(
                item_id = item_and_quantity['item_id'],
                quantity = item_and_quantity['quantity']
            )
        )
    custom_meal_update_dtos = CustomeMealUpdateDto(
        user_id=user_id,
        meal_id=meal_id,
        meal_course=meal_course,
        items_and_quantities=list_of_item_and_quantity_dtos
    )
    try:
        interactor.update_user_custom_meal_preference(
            custom_meal_preference_dto=custom_meal_update_dtos
        )
    except NotFound:
        response = INVALID_MEAL_ID
        json_response = json.dumps(response)
        return HttpResponse(json_response, status=404)
    except BadRequest:
        response = INVALID_ITEM_ID
        json_data = json.dumps(response)
        return HttpResponse(json_data, status=400)
    return HttpResponse(status=200)