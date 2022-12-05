import pytest
from django.contrib.auth.models import User
from django.test import Client

from apps.profiles.models import Profile
from apps.profiles.tests.global_var import simu_profiles


@pytest.fixture
@pytest.mark.django_db
def simu_create_profiles_db():
    for simu_profile in simu_profiles:
        user = User.objects.create(username=(simu_profile["user"])["username"],
                                   first_name=(simu_profile["user"])["firstname"],
                                   last_name=(simu_profile["user"])["lastname"],
                                   email=(simu_profile["user"])["email"],
                                   password=(simu_profile["user"])["password"])
        Profile.objects.create(user=user, favorite_city=simu_profile["favorite_city"])


@pytest.fixture
def client():
    return Client()
