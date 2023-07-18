from faker import Faker

fake = Faker()


class PlayerLocalisation:

    def __init__(self, lang) -> None:
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        self.result["number"] = number
        return self

    def build(self):
        return self.result
