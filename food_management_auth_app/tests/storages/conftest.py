import pytest

from django.contrib.auth.hashers import make_password

from food_management_auth_app.models import User
from food_management_auth_app.interactors.storages.dtos import UserDto


@pytest.fixture
def user_objs():

    users_list = [
        {
            'username': 'username1',
            'name': 'name1',
            'profile_pic': 'https://www.profile_pic1.com',
            'password': 'ibhubs-1234',
            'email': 'username1@gmail.com'
        },
        {
            'username': 'username2',
            'name': 'name2',
            'profile_pic': 'https://www.profile_pic2.com',
            'password': 'ibhubs-1234',
            'email': 'username2@gmail.com'
        },
        {
            'username': 'username3',
            'name': 'name3',
            'profile_pic': 'https://www.profile_pic3.com',
            'password': 'ibhubs-1234',
            'email': 'username3@gmail.com'
        },
        {
            'username': 'username4',
            'name': 'name4',
            'profile_pic': 'https://www.profile_pic4.com',
            'password': 'ibhubs-1234',
            'email': 'username4@gmail.com'
        },
        {
            'username': 'username5',
            'name': 'name5',
            'profile_pic': 'https://www.profile_pic5.com',
            'password': 'ibhubs-1234',
            'email': 'username5@gmail.com'
        }
    ]
    User.objects.bulk_create(
        [
            User(
                username=user_list['username'],
                name=user_list['name'],
                profile_pic=user_list['profile_pic'],
                password=make_password(user_list['password']),
                email=user_list['email']
            )
            for user_list in users_list
        ]
    )

@pytest.fixture
def user_dtos(user_objs):

    user_dtos_list = [
        UserDto(
            user_id=1,
            username='username1',
            profile_pic='https://www.profile_pic1.com',
            email='username1@gmail.com'
        ),
        UserDto(
            user_id=2,
            username='username2',
            profile_pic='https://www.profile_pic2.com',
            email='username2@gmail.com'
        ),
        UserDto(
            user_id=3,
            username='username3',
            profile_pic='https://www.profile_pic3.com',
            email='username3@gmail.com'
        )
    ]
    return user_dtos_list