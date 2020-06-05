from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from food_management.interactors.storages.dtos import (
    HomePageDto, AnnouncementDtos, SetMealPreferenceDto, MealScheduleDto,
    ItemDto, HeadCountDto, FoodWastageDto
)

class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_if_user_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def login_user_details_response(self, token_dto: UserAuthTokensDTO, is_admin):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date(self):
        pass

    @abstractmethod
    def get_home_page_response(self, home_page_dto: HomePageDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_meal_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date_for_that_meal(self):
        pass

    @abstractmethod
    def get_announcements_response(self, announcement_dtos: List[AnnouncementDtos]):
        pass

    @abstractmethod
    def get_meal_preference_response(self, meal_data_dto: SetMealPreferenceDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_course_type(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_id(self):
        pass

    @abstractmethod
    def get_meal_schedule_response(self, meal_schedule_dto: MealScheduleDto):
        pass

    @abstractmethod
    def get_items_list_response(self, items_list_dto: List[ItemDto]):
        pass

    @abstractmethod
    def get_meal_head_count_response(self, head_count_dto: HeadCountDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_quantity(self):
        pass

    @abstractmethod
    def get_user_rating_response(self, user_rating_dto: int):
        pass

    @abstractmethod
    def get_food_wastage_response(self, food_wastage_dto: FoodWastageDto):
        pass
