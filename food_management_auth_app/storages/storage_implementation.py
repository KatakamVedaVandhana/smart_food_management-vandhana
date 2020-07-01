from typing import List

from food_management_auth_app.interactors.storages.storage_interface import \
    StorageInterface
from food_management_auth_app.interactors.storages.dtos import UserDetailsDto
from food_management_auth_app.models import User

class StorageImplementation(StorageInterface):

    def get_user_ids(self):
        user_ids = list(User.objects.all().values_list('id',flat=True))
        return user_ids

    def get_user_dtos(self, user_ids: List[int]):
        user_objs = User.objects.filte(id__in=user_ids)
        user_dtos = [
            self._convert_user_obj_into_user_dto(user_obj)
            for user_obj in user_objs
        ]
        return user_dtos

    def _convert_user_obj_into_user_dto(self, user_obj):
        return UserDetailsDto(
            user_id=user_obj.id,
            username=user_obj.username,
            name=user_obj.name,
            profile_pic=user_obj.profile_pic
        )
