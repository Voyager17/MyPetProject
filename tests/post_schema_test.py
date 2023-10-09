"""This test is an example of incorrect using of validation."""
import requests

from jsonschema import validate
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 6, GlobalErrorMessages.WRONG_STATUS_CODE.value
    for item in received_posts:
        # You can stay just validate(received_posts, POST_SCHEMA) if it is not a list
        # I mean u can remove the cycle
        validate(received_posts, POST_SCHEMA)


# {'page': 1, 'per_page': 6, 'total': 12, 'total_pages': 2,

# 'data':
# [{'id': 1, 'email': 'george.bluth@reqres.in',
# 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'},
# {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'},  # noqa: E501
# {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'},  # noqa: E501
# {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'},  # noqa: E501
# {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'},  # noqa: E501
#  {'id': 6, 'email': 'tracey.ramos@reqres.in', 'first_name': 'Tracey', 'last_name': 'Ramos', 'avatar': 'https://reqres.in/img/faces/6-image.jpg'}]  # noqa: E501

# , 'support': {'url': 'https://reqres.in/#support-heading', 'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'}}  # noqa: E501
