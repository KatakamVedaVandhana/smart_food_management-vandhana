from abc import ABC
from abc import abstractmethod
from datetime import datetime
from typing import List
from food_management.interactors.storages.dtos import AnnouncementDtos, UserRatingDto
from food_management.dtos.dtos import RatingDto



class StorageInterface(ABC):

    @abstractmethod
    def create_user(self, username: str, password: str):
        pass

    @abstractmethod
    def check_if_user_exists(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_user_details(self, username: str, password: str) -> int:
        pass

    @abstractmethod
    def get_announcements(self, date_obj: datetime) -> List[AnnouncementDtos]:
        pass

    @abstractmethod
    def check_if_user_has_a_rating(self, user_id: int, meal_id: int) -> bool:
        pass

    @abstractmethod
    def update_user_rating(self, rating_dto: RatingDto):
        pass

    @abstractmethod
    def create_user_rating(self, rating_dto: RatingDto):
        pass

    @abstractmethod
    def get_user_rating(self, meal_id: int, user_id: int) -> UserRatingDto:
        pass