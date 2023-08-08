from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, expecting_status_code):
        if isinstance(expecting_status_code, list):
            assert self.response_status in expecting_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == expecting_status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def get_parsed_object(self):
        return self.parsed_object

    # def __str__(self) -> str:
   #     return (
     #       "Hi there"
    #    )
