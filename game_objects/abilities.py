from abc import ABC, abstractmethod
from typing import Any

from game_objects.keywords import Keywords


class Ability(ABC):
    def __init__(self):
        pass

    def to_hit(self, params: dict) -> dict:
        return params

    def to_wound(self, params: dict) -> dict:
        return params

    def damage(self, params: dict) -> dict:
        return params

    def feel_no_pain(self, params: dict) -> dict:
        return params


class SampleAbility(Ability):
    def to_hit(self, params: dict) -> dict:
        if Keywords.Vehicle in params["enemy_keywords"]:
            params["to_hit"] *= 2
        return params
