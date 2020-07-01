import pytest

from django.contrib.auth.hashers import make_password

from food_management_auth_app.models import User


@pytest.fixture
def user_objs():

    users_list = [
        {
            'username': 'username1',
            'name': 'name1',
            'profile_pic': 'https://www.profile_pic1.com',
            'password': 'ibhubs-1234'
        },
        {
            'username': 'username2',
            'name': 'name2',
            'profile_pic': 'https://www.profile_pic2.com',
            'password': 'ibhubs-1234'
        },
        {
            'username': 'username3',
            'name': 'name3',
            'profile_pic': 'https://www.profile_pic3.com',
            'password': 'ibhubs-1234'
        },
        {
            'username': 'username4',
            'name': 'name4',
            'profile_pic': 'https://www.profile_pic4.com',
            'password': 'ibhubs-1234'
        },
        {
            'username': 'username5',
            'name': 'name5',
            'profile_pic': 'https://www.profile_pic5.com',
            'password': 'ibhubs-1234'
        }
    ]
    User.objects.bulk_create(
        [
            User(
                username=user_list['username'],
                name=user_list['name'],
                profile_pic=user_list['profile_pic'],
                password=make_password(user_list['password'])
            )
            for user_list in users_list
        ]
    )