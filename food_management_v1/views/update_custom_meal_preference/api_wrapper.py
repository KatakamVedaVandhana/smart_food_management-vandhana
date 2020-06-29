from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
import json
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
    user_id = kwargs['user'].id
    meal_course = request_data['meal_course']
    meal_type = request_data['meal_type']
    date = request_data['date']
    print(kwargs['request_data'])
    print("\n")
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = UpdateUserCustomMealPreferenceInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    list_of_item_and_quantity_dtos = []
    for item_and_quantity in request_data['items_and_quantities']:
        
        list_of_item_and_quantity_dtos.append(
            ItemAndQuantityDto(
                item_id = item_and_quantity['item_id'],
                quantity = item_and_quantity['quantity']
            )
        )
    custom_meal_update_dtos = CustomeMealUpdateDto(
        user_id=user_id,
        meal_type=meal_type,
        date=date,
        meal_course=meal_course,
        items_and_quantities=list_of_item_and_quantity_dtos
    )
    interactor.update_user_custom_meal_preference(
        custom_meal_preference_dto=custom_meal_update_dtos
    )
    return HttpResponse(status=200)