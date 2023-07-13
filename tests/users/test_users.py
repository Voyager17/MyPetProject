import pytest

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User
import requests


res = requests.get(SERVICE_URL)


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[BUG 1223] Missing data')
def test_another():
    assert 1 == 1

# pytest -s -v -k development  tests/users/test_users.py #run tests only with mark @development
# pytest -s -v --durations=0 -vv  tests/users/test_users.py # shows time of running


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
                         (1, 2, 3),
                         (-1, -2, -3),
                         (-1, 2, 1),
                         ("b", -2, None),
                         ("b", "b", None)
                         ])
def test_calculation(first_value, second_value, result, get_calculate):
    assert get_calculate(first_value, second_value) == result
