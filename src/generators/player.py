from src.enums.user_enums import Statuses
from src.generators.player_localisation import PlayerLocalisation


class Player:

    def __init__(self) -> None:
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://google.com/'):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalisation('en_US').build(),
            "ru": PlayerLocalisation('ru_RU').build()
        }
        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {"en": generator.build()}
        return self

    def build(self):
        return self.result