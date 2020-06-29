from typing import List
from collections import defaultdict
from food_management.constants.constants import DEFAULT_TIME_FORMAT
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest
from django_swagger_utils.drf_server.exceptions import NotFound
from food_management.constants.exception_messages import (
    INVALID_USERNAME, INVALID_ITEM_ID, INVALID_MEAL_ID, INVALID_PASSWORD,
    USER_ALREADY_EXISTS, INVALID_DATA, INVALID_QUANTITY
)

from food_management.constants.exception_messages import \
    INVALID_DATE, INVALID_MEAL_TYPE, INVALID_MEAL_COURSE
from common.dtos import UserAuthTokensDTO
from food_management.interactors.storages.dtos import (
    HomePageDto, AnnouncementDtos, SetMealPreferenceDto, MealScheduleDto,
    ItemDto, HeadCountDto, UserRatingDto, FoodWastageDto
)


class PresenterImplementation(PresenterInterface):

    def raise_exception_if_user_exists(self):
        raise BadRequest(USER_ALREADY_EXISTS)

    def raise_exception_for_invalid_username(self):
        raise NotFound(INVALID_USERNAME)

    def raise_exception_for_invalid_password(self):
        raise BadRequest(INVALID_PASSWORD)

    def raise_exception_for_invalid_meal_id(self):
        raise NotFound(INVALID_MEAL_ID)

    def raise_exception_for_invalid_date(self):
        raise BadRequest(INVALID_DATE)

    def raise_exception_for_invalid_quantity(self):
        raise BadRequest(INVALID_QUANTITY)

    def raise_exception_for_invalid_meal_type(self):
        raise BadRequest(INVALID_MEAL_TYPE)

    def raise_exception_for_invalid_course_type(self):
        raise BadRequest(INVALID_MEAL_COURSE)

    def raise_exception_for_invalid_item_id(self):
        raise NotFound(INVALID_ITEM_ID)

    def raise_exception_for_invalid_date_for_that_meal(self):
        raise NotFound(INVALID_DATA)

    def login_user_details_response(self, token_dto: UserAuthTokensDTO, is_admin:bool):
        response_dict = {
            "user_id": token_dto.user_id,
            "access_token": token_dto.access_token,
            "refresh_token": token_dto.refresh_token,
            "expires_in": str(token_dto.expires_in),
            "is_admin": is_admin
        }
        return response_dict

    def get_home_page_response(self, home_page_dto: HomePageDto):
        meal_list = []
        meal_course_dtos = home_page_dto.meal_course
        meal_items = self._map_items_object(home_page_dto.items)
        meal_dtos = home_page_dto.meal
        for meal_dto in meal_dtos:
            meal_dict = self._get_meal_details_as_dict(meal_dto, meal_items)
            meal_list.append(meal_dict)
        meal_complete_details = self._map_meal_course_object(
            meal_list, meal_course_dtos
        )
        return meal_complete_details

    def get_announcements_response(self, announcement_dtos: List[AnnouncementDtos]):
        announcement_list = []
        for announcement_dto in announcement_dtos:
            announcement_list.append(self._convert_announcement_dto_to_dict(
                announcement_dto)
            )
        return announcement_list

    def get_meal_schedule_response(self, meal_schedule_dto: MealScheduleDto):
        meal_dto = meal_schedule_dto.meal
        items = meal_schedule_dto.items
        meal_items = defaultdict(list)
        for item in items:
            meal_items[meal_dto.meal_id].append(self._convert_item_dto_as_dict(item))
        meal_dict = self._convert_meal_dto_into_dict(meal_dto, meal_items)
        return meal_dict

    def get_items_list_response(self, items_list_dto: List[ItemDto]):
        items_list = []
        for item_dto in items_list_dto:
            items_list.append(self._convert_item_dto_as_dict(item_dto))
        return items_list

    def _convert_meal_dto_into_dict(self, meal_dto, meal_items):
        meal_dict = {}
        meal_dict['meal_type'] = meal_dto.meal_type
        meal_dict['meal_id'] = meal_dto.meal_id
        meal_dict['date'] = meal_dto.date
        meal_dict['items_list'] = meal_items[meal_dto.meal_id]
        return meal_dict

    def _map_items_object(self, item_dtos):
        meal_dict = defaultdict(list)
        for item_dto in item_dtos:
            meal_dict[item_dto.meal_id].append(
                self._convert_item_dto_as_dict(item_dto)
            )
        return meal_dict

    def _convert_item_dto_as_dict(self, item_dto):
        item_dict = {
            "item_id": item_dto.item_id,
            "item": item_dto.item,
            "units": item_dto.units,
            "category": item_dto.category
        }
        return item_dict

    def _get_meal_details_as_dict(self, meal_dto, meal_items):
        meal_dict = {}
        meal_dict['meal_id'] = meal_dto.meal_id
        meal_dict['meal_type'] = meal_dto.meal_type
        meal_dict['items'] = meal_items[meal_dto.meal_id]
        meal_dict['from_time_string'] = meal_dto.from_time_string.strftime(DEFAULT_TIME_FORMAT)
        meal_dict['to_time_string'] = meal_dto.to_time_string.strftime(DEFAULT_TIME_FORMAT)
        return meal_dict

    def _map_meal_course_object(self,meal_list, meal_course_dtos):
        for meal in meal_list:
            for meal_course in meal_course_dtos:
                if meal_course.meal_type is meal['meal_type']:
                    meal['meal_course'] = meal_course.meal_course
        return meal_list

    def _convert_announcement_dto_to_dict(self, announcement_dto):
        announcement_dict = {
            'title': announcement_dto.title,
            'subtitle': announcement_dto.subtitle,
            'description': announcement_dto.description,
            'image': announcement_dto.image
        }
        return announcement_dict

    def get_meal_preference_response(self, meal_data_dto: SetMealPreferenceDto):
        meal_course_dtos = meal_data_dto.meal_course
        meal_data = []
        meal_complete_course_details_dict = \
            self._map_meal_complete_course_details_to_items(meal_course_dtos)
        item_dtos_list = meal_data_dto.items
        for item_dto in item_dtos_list:
            items_dict = self._convert_comeplete_details_of_item_dto_into_dict(
                item_dto
            )
            items_dict['meal_courses'] = meal_complete_course_details_dict[item_dto.item_id]
            meal_data.append(items_dict)
        return meal_data


    def get_meal_head_count_response(self, head_count_dto: HeadCountDto):
        pass


    def _convert_comeplete_details_of_item_dto_into_dict(self, item_dto):
        item_dict = {
            'item_id': item_dto.item_id,
            'item': item_dto.item,
            'units': item_dto.units,
            'category': item_dto.category,
        }
        return item_dict

    def _map_meal_complete_course_details_to_items(self, meal_course_dtos):
        meal_complete_course_details_dict = defaultdict(list)
        for meal_dto in meal_course_dtos:
            meal_complete_course_details_dict[meal_dto.item_id].append(
                self._convert_meal_complete_course_details_dto_into_dict
                (meal_dto)
            )
        return meal_complete_course_details_dict

    def _convert_meal_complete_course_details_dto_into_dict(self, meal_dto):
        meal_dict = {
            'meal_course': meal_dto.meal_course,
            'quantity': meal_dto.quantity
        }
        return meal_dict

    def get_user_rating_response(self, user_rating_dto: UserRatingDto):
        items_and_ratings = user_rating_dto.items_and_ratings
        items_and_ratings_list = []
        for item_and_rating in items_and_ratings:
            items_and_ratings_list.append(
                self._convert_item_rating_dto_as_dict(item_and_rating)
            )
        items_and_ratings_dict = {
            "items_and_ratings": items_and_ratings_list,
            "description": user_rating_dto.description
        }
        return items_and_ratings_dict

    def _convert_item_rating_dto_as_dict(self, item_and_rating):
        item_and_rating_dict = {
            "item_id": item_and_rating.item_id,
            "taste": item_and_rating.taste,
            "quality": item_and_rating.quality
        }
        return item_and_rating_dict

    def get_food_wastage_response(self, food_wastage_dto: FoodWastageDto):
        items_and_wastage = food_wastage_dto.items_and_wastage
        items_and_wastage_list = []
        for item_and_wastage in items_and_wastage:
            items_and_wastage_list.append(
                self._convert_items_and_wastage_dto_into_dict(
                    item_and_wastage
                )
            )
        food_wastage_dict = {
            "food_prepared": food_wastage_dto.food_prepared,
            "food_wasted": food_wastage_dto.food_wasted,
            "items_and_wastage": items_and_wastage_list
        }
        return food_wastage_dict

    def _convert_items_and_wastage_dto_into_dict(self, item_and_wastage):
        item_and_wastage_dict = {
            "item_id": item_and_wastage.item_id,
            "item": item_and_wastage.item,
            "food_prepared": item_and_wastage.food_prepared,
            "food_wasted": item_and_wastage.food_wasted,
            "base_unit": item_and_wastage.base_unit
        }
        return item_and_wastage_dict