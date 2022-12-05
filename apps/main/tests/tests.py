from http import HTTPStatus
from django.urls import reverse


class TestIndex:
    def test_index(self, client):
        ENDPOINT_INDEX = reverse('main:index')
        result = client.get(ENDPOINT_INDEX)
        assert result.status_code == HTTPStatus.OK
        assert "Welcome to Holiday Homes" in result.content.decode()
