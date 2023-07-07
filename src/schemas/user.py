from pydantic import BaseModel, validator
from src.enums.global_enums import GlobalErrorMessages
from src.enums.user_enums import (
    Genders,
    Statuses
)


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator("email")
    def check_email(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(GlobalErrorMessages.WRONG_EMAIL.value)
