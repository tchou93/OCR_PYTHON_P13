from http import HTTPStatus
import pytest
from django.urls import reverse

from apps.profiles.tests.global_var import simu_profiles


@pytest.mark.django_db
class TestProfile:
    def test_index_profile(self, client, simu_create_profiles_db):
        ENDPOINT_PROFILES = reverse('profiles:index')
        result = client.get(ENDPOINT_PROFILES)
        assert result.status_code == HTTPStatus.OK
        assert "Profiles" in result.content.decode()

    def test_profile(self, client, simu_create_profiles_db):
        ENDPOINT_PROFILE = reverse('profiles:profile', kwargs={
            'username': ((simu_profiles[0])["user"])["username"]})
        result = client.get(ENDPOINT_PROFILE)
        assert result.status_code == HTTPStatus.OK
        assert ((simu_profiles[0])["user"])["username"] in result.content.decode()
