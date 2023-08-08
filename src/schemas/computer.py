from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPvAnyAddress
from pydantic.color import Color


from examples.examples import computer
from src.enums.user_enums import Statuses


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPvAnyAddress
    host_v6: IPvAnyAddress
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp.schema_json())
