from typing import List

from food_management.dtos.dtos import UserProfileDto

class AuthService:

    @property
    def interface(self):
        from food_management_auth_app.interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]):

        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)

        user_profile_dtos = [
            UserProfileDto(
                user_id=user_dto.user_id,
                profile_pic=user_dto.profile_pic,
                email=user_dto.email,
                username=user_dto.username
            )
            for user_dto in user_dtos
        ]

        return user_profile_dtos
