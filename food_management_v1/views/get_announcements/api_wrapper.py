from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
import json
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from food_management.interactors.get_announcements_interactor import \
    GetAnnouncementsInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    date = kwargs['request_query_params'].__dict__['date']
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    interactor = GetAnnouncementsInteractor(presenter=presenter, storage=storage)
    announcements_list = interactor.get_announcements(date_obj=date)
    json_response = json.dumps(announcements_list, indent=4)
    return HttpResponse(json_response, status=200)