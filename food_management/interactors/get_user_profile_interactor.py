from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.adapters.service_adapter import get_service_adapter

class GetUserProfileInteractor:

    def __init__(self):
        pass

    def get_user_profile_wrapper(self, presenter: PresenterInterface, user_id: int):
        user_dto = self.get_user_profile(user_id=user_id)
        return presenter.get_user_dtos_response(user_dto=user_dto)

    def get_user_profile(self, user_id: int):

        #TODO get user details from service adapter
        service_adapter = get_service_adapter()
        user_dto = service_adapter.auth_service.get_user_dtos(user_ids=[user_id])
        print(user_dto)
        return user_dto[0]
