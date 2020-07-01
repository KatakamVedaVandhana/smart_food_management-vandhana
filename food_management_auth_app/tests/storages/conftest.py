import pytest

from food_management_auth_app.models import User


@pytest.fixture
def user_objs():

    users_list = [
        {
            'username': 'username1',
            'name': 'name1',
            'profile_pic': 'https://www.profile_pic1.com'
        },
        {
            'username': 'username2',
            'name': 'name2',
            'profile_pic': 'https://www.profile_pic2.com'
        },
        {
            'username': 'username3',
            'name': 'name3',
            'profile_pic': 'https://www.profile_pic3.com'
        },
        {
            'username': 'username4',
            'name': 'name4',
            'profile_pic': 'https://www.profile_pic4.com'
        },
        {
            'username': 'username5',
            'name': 'name5',
            'profile_pic': 'https://www.profile_pic5.com'
        }
    ]