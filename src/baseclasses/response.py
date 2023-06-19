from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response.json, list):
            for item in self.response.json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, expecting_status_code):
        if isinstance(expecting_status_code, list):
            assert self.response_status in expecting_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == expecting_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
