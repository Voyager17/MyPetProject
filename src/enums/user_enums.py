from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(PyEnum):
    inactive = "inactive"
    active = "active"


print(Statuses.list())
