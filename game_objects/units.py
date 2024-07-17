from abc import ABC, abstractmethod

from game_objects.weapons import Weapon


class UnitBase(ABC):
    NAME = ""
    FACTION = ""
    WEAPONS: list[Weapon]

    def __init__(self):
        pass

    def calculate_to_hit(self):
        return [w.to_hit() for w in self.WEAPONS]

    def calculate_to_wound(self):
        pass

    def calculate_damage(self):
        pass

    def calculate_feel_no_pain(self):
        pass
