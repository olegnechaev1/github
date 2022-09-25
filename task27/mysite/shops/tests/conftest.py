import pytest
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from shops.factories import BrandFactory
from .contstants import DEFAULT_BRAND_COUNT


@pytest.fixture
def create_brands():
    for i in range(DEFAULT_BRAND_COUNT):
        BrandFactory()
    

@pytest.fixture
def user(db):
    return User.objects.create(username='test')


@pytest.fixture
def client(user):
    
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client
