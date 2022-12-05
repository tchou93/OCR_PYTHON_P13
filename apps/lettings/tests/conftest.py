import pytest
from django.test import Client
from apps.lettings.models import Address, Letting
from apps.lettings.tests.global_var import simu_lettings


@pytest.fixture
def simu_create_lettings_db():
    for simu_letting in simu_lettings:
        address = Address.objects.create(number=(simu_letting["address"])["number"],
                                         street=(simu_letting["address"])["street"],
                                         city=(simu_letting["address"])["city"],
                                         state=(simu_letting["address"])["state"],
                                         zip_code=(simu_letting["address"])["zip_code"],
                                         country_iso_code=(simu_letting["address"])[
                                             "country_iso_code"])

        Letting.objects.create(title=simu_letting["title"],
                               address=address
                               )


@pytest.fixture
def client():
    return Client()
