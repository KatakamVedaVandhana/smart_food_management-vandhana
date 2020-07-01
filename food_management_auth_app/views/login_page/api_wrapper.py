import json

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse

from food_management_auth_app.interactors.login_interactor import \
    LoginInteractor
from food_management_auth_app.storages.storage_implementation import \
    StorageImplementation
from food_management_auth_app.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    presenter = PresenterImplementation()
    storage = StorageImplementation()
    oauth_storage = OAuth2SQLStorage()

    interactor = LoginInteractor(
        presenter=presenter, oauth_storage=oauth_storage, storage=storage
    )

    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    response = interactor.login(username=username, password=password)
    json_response = json.dumps(response)

    return HttpResponse(json_response, status=200)
