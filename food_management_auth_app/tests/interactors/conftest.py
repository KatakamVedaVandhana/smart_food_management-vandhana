import pytest
from freezegun import freeze_time
from django.utils import timezone
from datetime import datetime
from common.dtos import (
    UserAuthTokensDTO, Application, AccessTokenDTO, RefreshTokenDTO
)
from food_management_auth_app.interactors.storages.dtos import (
    UserDto
)

@pytest.fixture
def user_dtos():

    user_dtos = [
        UserDto(
            user_id=1, username='user1', email='user1@gmail.com',
            profile_pic='https://www.profile_pic_1.com/'
        ),
        UserDto(
            user_id=2, username='user2', email='user2@gmail.com',
            profile_pic='https://www.profile_pic_2.com/'
        ),
        UserDto(
            user_id=3, username='user3', email='user3@gmail.com',
            profile_pic='https://www.profile_pic_3.com/')
    ]
    return user_dtos

@pytest.fixture
@freeze_time('2020-02-12')
def user_auth_token_dto():
    user_id = 1
    access_token = '125'
    refresh_token = '521'
    expires_in = str(timezone.now())
    user_auth_token_dto = UserAuthTokensDTO(
        user_id=user_id, access_token=access_token,
        refresh_token=refresh_token, expires_in=expires_in
    )
    return user_auth_token_dto


@pytest.fixture
def login_details_response_dict():
    response_dict = {
        "user_id": 1,
        "access_token": '125',
        "refresh_token": '521',
        'expires_in': '2020-02-12'
    }
    return response_dict

@pytest.fixture
def application_dto():
    application_dto = Application(application_id=1)
    return application_dto

@pytest.fixture
@freeze_time('2020-02-12')
def access_token_dto():
    access_token_dto = AccessTokenDTO(
        access_token_id=1,
        token='125',
        expires=timezone.now()
    )
    return access_token_dto

@pytest.fixture
@freeze_time('2020-02-12')
def refresh_token_dto():
    refresh_token = RefreshTokenDTO(
        token='521',
        access_token='125',
        user_id=1,
        revoked=timezone.now()
    )
    return refresh_token
