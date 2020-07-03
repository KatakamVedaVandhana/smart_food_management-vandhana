import pytest
from freezegun import freeze_time
from django.utils import timezone
from datetime import datetime
from datetime import time
from common.dtos import UserAuthTokensDTO

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
@freeze_time('2020-02-12')
def login_details_response_dict():
    response_dict = {
        "user_id": 1,
        "access_token": '125',
        "refresh_token": '521',
        'expires_in': str(timezone.now()),
        'is_admin': False
    }
    return response_dict
