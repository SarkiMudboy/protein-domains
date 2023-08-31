import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda user: "%s_%s123" % (user.first_name, user.last_name))
    email = factory.LazyAttribute(lambda user: '%s@examplemail.com' %user.username)
    password = factory.django.Password('its-a-secret')


class SuperUserFactory(UserFactory):

    is_superuser = True