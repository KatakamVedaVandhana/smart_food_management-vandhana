from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from food_management.storages.meal_storage_implementation import \
    MealStorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.update_meal_schedule_interactor import \
    UpdateMealScheduleInteractor
from food_management.dtos.dtos import UpdateMealScheduleDto, ItemDetailsDto

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    presenter = PresenterImplementation()
    meal_storage = MealStorageImplementation()
    interactor = UpdateMealScheduleInteractor(
        meal_storage=meal_storage, presenter=presenter
    )
    request_data = kwargs['request_data']
    meal_type = request_data['meal_type']
    date = request_data['date']
    items_list = request_data['items_list']
    item_details_dto = [
        ItemDetailsDto(
            item_id=item_details['item_id'],
            meal_course=item_details['meal_course'],
            quantity=item_details['quantity']
        )
            for item_details in items_list
    ]
    update_meal_schedule_dto = UpdateMealScheduleDto(
        meal_type=meal_type,
        date=date,
        items=item_details_dto
    )
    interactor.update_meal_schedule(
        update_meal_schedule_dto=update_meal_schedule_dto)
    return HttpResponse(status=200)
