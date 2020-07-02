from typing import List
from datetime import datetime
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.models import Meal
from food_management.models import Announcements
from food_management.models.user_rating import UserRating
from food_management.models.user_feedback import UserFeedback
from food_management.exceptions.exceptions import \
    InvalidUsername, InvalidPassword
from food_management.interactors.storages.dtos import AnnouncementDtos, UserRatingDto
from food_management.dtos.dtos import RatingDto, ItemAndRatingDto


class StorageImplementation(StorageInterface):


    def create_user(self, username: str, password: str):
        user_obj = User(username=username)
        user_obj.set_password(password)
        user_obj.save()

    def check_if_user_exists(self, username: str, password: str) -> bool:

        bool_value = User.objects.filter(
            username=username, password=password
        ).exists()
        return bool_value

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

    def get_announcements(self, date_obj: datetime) -> List[AnnouncementDtos]:
        announcement_objs = Announcements.objects.filter(date=date_obj)
        annoncement_dtos = []
        for announcement_obj in announcement_objs:
            annoncement_dtos.append(self._conver_announcement_obj_into_dto(
                announcement_obj
            ))
        return annoncement_dtos

    def _conver_announcement_obj_into_dto(self, announcement_obj):
        return AnnouncementDtos(
            title=announcement_obj.title,
            subtitle=announcement_obj.subtitle,
            description=announcement_obj.description,
            image=announcement_obj.image
        )

    def check_if_user_has_a_rating(self, user_id: int, meal_id: int):
        bool_value = UserRating.objects.filter(user_id=user_id, meal_id=meal_id).exists()
        return bool_value


    def update_user_rating(self, rating_dto: RatingDto):
        meal_type = rating_dto.meal_type
        date_obj = rating_dto.date
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        user_id = rating_dto.user_id
        meal_id = meal_obj.id
        description = rating_dto.description
        items_and_ratings_dtos_list = rating_dto.items_and_ratings
        userrating_objs = UserRating.objects.filter(user_id=user_id, meal_id=meal_id)
        for index in range(len(items_and_ratings_dtos_list)):
            userrating_obj = userrating_objs[index]
            userrating_obj.item_id = items_and_ratings_dtos_list[index].item_id
            userrating_obj.taste = items_and_ratings_dtos_list[index].taste
            userrating_obj.quality = items_and_ratings_dtos_list[index].quality
            userrating_obj.save()
        # UserRating.objects.bulk_update(
        #         userrating_objs,['item_id', 'quality','taste']
        #     )
        print(UserRating.objects.filter(user_id=user_id, meal_id=meal_id).values('taste','quality'))
        UserFeedback.objects.filter(user_id=user_id, meal_id=meal_id).update(description=description)


    def create_user_rating(self, rating_dto: RatingDto):
        meal_type = rating_dto.meal_type
        date_obj = rating_dto.date
        meal_obj = Meal.objects.get(meal_type=meal_type, date=date_obj)
        user_id = rating_dto.user_id
        meal_id = meal_obj.id
        description = rating_dto.description
        items_and_ratings = rating_dto.items_and_ratings
        UserRating.objects.bulk_create([
            UserRating(
                user_id=user_id,
                meal_id=meal_id,
                item_id=item_and_rating.item_id,
                quality=item_and_rating.quality,
                taste=item_and_rating.taste
            )
            for item_and_rating in items_and_ratings
        ])
        UserFeedback.objects.create(
            meal_id=meal_id, user_id=user_id, description=description
        )

    def get_user_rating(self, meal_id: int, user_id: int) -> UserRatingDto:
        user_rating_objs = UserRating.objects.filter(
            meal_id=meal_id, user_id=user_id
        )
        item_and_rating_dto = []
        user_feedback_obj = UserFeedback.objects.filter(meal_id=meal_id,user_id=user_id)[0]
        print(user_feedback_obj)
        for user_rating_obj in user_rating_objs:
            item_and_rating_dto.append(
                self._convert_user_rating_obj_into_rating_dto(
                    user_rating_obj
                )
            )
        return UserRatingDto(
            items_and_ratings=item_and_rating_dto,
            description=user_feedback_obj.description
        )

    def _convert_user_rating_obj_into_rating_dto(self, user_rating_obj):
        return ItemAndRatingDto(
            item_id=user_rating_obj.item_id,
            taste=user_rating_obj.taste,
            quality=user_rating_obj.quality
        )