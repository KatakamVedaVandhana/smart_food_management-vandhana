import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from django.http import HttpResponse
from .validator_class import ValidatorClass
from food_management.storages.storage_implementation import \
    StorageImplementation
from food_management.interactors.login_interactor import LoginInteractor
from food_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from food_management.constants.exception_messages import \
    INVALID_USERNAME, INVALID_PASSWORD


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print(kwargs['user'].__dict__)
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = LoginInteractor(
        storage=storage, presenter=presenter, oauth_storage=oauth_storage
    )
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    try:
        response_dict = interactor.login(username=username, password=password)
    except NotFound:
        response_dict = INVALID_USERNAME
        response = json.dumps(response_dict)
        return HttpResponse(response, status=404)
    except BadRequest:
        response_dict = INVALID_PASSWORD
        response = json.dumps(response_dict)
        return HttpResponse(response, status=400)
    json_response = json.dumps(response_dict)
    return HttpResponse(json_response, status=201)