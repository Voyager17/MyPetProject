import pytest
import requests

from configuration import SERVICE_URL
from random import randrange


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    return a + b


@pytest.fixture
def get_calculate():
    return _calculate


@pytest.fixture
def make_number():
    print('Getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'number at home {number}')
