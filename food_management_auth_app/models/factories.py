import factory
import factory.django

from food_management_auth_app.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'username_{n+1}')
    password = factory.LazyAttribute(lambda obj: obj.username)
