from http import HTTPStatus
import pytest
from django.urls import reverse

from apps.profiles.models import Profile
from apps.profiles.tests.global_var import simu_profiles


@pytest.mark.django_db
class TestProfile:
    def test_index_profile(self, client, simu_create_profiles_db):
        ENDPOINT_PROFILES = reverse('profiles:index')
        result = client.get(ENDPOINT_PROFILES)
        assert result.status_code == HTTPStatus.OK
        assert "<h1>Profiles</h1>" in result.content.decode()

    def test_profile(self, client, simu_create_profiles_db):
        ENDPOINT_PROFILE = reverse('profiles:profile', kwargs={
            'username': (Profile.objects.all()[0]).user.username})
        result = client.get(ENDPOINT_PROFILE)
        assert result.status_code == HTTPStatus.OK
        assert f"<h1>{((simu_profiles[0])['user'])['username']}</h1>" in result.content.decode()
        assert ((simu_profiles[0])['user'])['firstname'] in result.content.decode()
        assert ((simu_profiles[0])['user'])['lastname'] in result.content.decode()
        assert ((simu_profiles[0])['user'])['email'] in result.content.decode()
        assert (simu_profiles[0])['favorite_city'] in result.content.decode()
        assert (simu_profiles[0])['favorite_city'] in result.content.decode()
