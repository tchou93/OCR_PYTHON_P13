from http import HTTPStatus
import pytest
from django.urls import reverse
from apps.lettings.models import Letting


@pytest.mark.django_db
class TestLetting:
    def test_index_letting(self, client, simu_create_lettings_db):
        ENDPOINT_PROFILES = reverse('lettings:index')
        result = client.get(ENDPOINT_PROFILES)
        assert result.status_code == HTTPStatus.OK
        assert "Profiles" in result.content.decode()

    def test_letting(self, client, simu_create_lettings_db):
        ENDPOINT_PROFILE = reverse('lettings:letting', kwargs={
            'letting_id': (Letting.objects.all()[0]).id})
        result = client.get(ENDPOINT_PROFILE)
        assert result.status_code == HTTPStatus.OK
        assert "test_street1" in result.content.decode()
        assert "test_city1" in result.content.decode()
        assert "test_state1" in result.content.decode()
        assert "111" in result.content.decode()
