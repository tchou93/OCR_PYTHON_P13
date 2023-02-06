from http import HTTPStatus
import pytest
from django.urls import reverse
from apps.lettings.models import Letting
from apps.lettings.tests.global_var import simu_lettings


@pytest.mark.django_db
class TestLetting:
    def test_index_letting(self, client, simu_create_lettings_db):
        ENDPOINT_PROFILES = reverse('lettings:index')
        result = client.get(ENDPOINT_PROFILES)
        assert result.status_code == HTTPStatus.OK
        assert "<h1>Lettings</h1>" in result.content.decode()

    def test_letting(self, client, simu_create_lettings_db):
        ENDPOINT_PROFILE = reverse('lettings:letting', kwargs={
            'letting_id': (Letting.objects.all()[0]).id})
        result = client.get(ENDPOINT_PROFILE)
        assert result.status_code == HTTPStatus.OK
        assert (simu_lettings[0])["title"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["number"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["street"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["city"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["state"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["zip_code"] in result.content.decode()
        assert ((simu_lettings[0])["address"])["country_iso_code"] in result.content.decode()
