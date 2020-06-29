from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django_swagger_utils.drf_server.exceptions import BadRequest
import json
from django.http import HttpResponse
from food_management.constants.exception_messages import INVALID_MEAL_ID
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.update_user_meal_preference_interactor import \
    UpdateUserMealPreferenceInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs['user'].id
    request_data = kwargs['request_data']
    meal_type = request_data['meal_type']
    date = request_data['date']
    meal_course = request_data['meal_course']
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = UpdateUserMealPreferenceInteractor(
        presenter=presenter, meal_storage=meal_storage
    )
    interactor.update_user_meal_preference(
        meal_type=meal_type, user_id=user_id, meal_course=meal_course,
        date_obj=date
    )
    return HttpResponse(status=200)
