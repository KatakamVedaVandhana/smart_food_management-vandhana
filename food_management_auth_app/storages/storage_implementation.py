from typing import List

from food_management_auth_app.interactors.storages.storage_interface import \
    StorageInterface
from food_management_auth_app.interactors.storages.dtos import UserDto
from food_management_auth_app.models import User
from food_management_auth_app.exceptions.exceptions import InvalidUsername, InvalidPassword

class StorageImplementation(StorageInterface):

    def get_user_ids(self):
        user_ids = list(User.objects.all().values_list('id',flat=True))
        return user_ids

    def get_user_dtos(self, user_ids: List[int]):
        user_objs = User.objects.filter(id__in=user_ids)
        user_dtos = [
            self._convert_user_obj_into_user_dto(user_obj)
            for user_obj in user_objs
        ]
        return user_dtos

    def _convert_user_obj_into_user_dto(self, user_obj):
        return UserDto(
            user_id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            profile_pic=user_obj.profile_pic
        )

    def get_user_details(self, username: str, password: str):

        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername

        is_valid_password = user_obj.check_password(password)
        not_a_valid_password = not is_valid_password

        if not_a_valid_password:
            raise InvalidPassword

        return user_obj.id, user_obj.is_superuser

    def validate_username(self, username: str):

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername
        return

    def validate_password(self, username: str, password: str):

        user_obj = User.objects.get(username=username)

        is_valid_password = user_obj.check_password(password)
        not_a_valid_password = not is_valid_password

        if not_a_valid_password:
            raise InvalidPassword
