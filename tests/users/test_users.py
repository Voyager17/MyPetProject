
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User
import requests


res = requests.get(SERVICE_URL)


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)


def test_another():
    assert 1 == 1
