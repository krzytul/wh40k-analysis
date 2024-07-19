import json

from abc import ABC, abstractmethod

from game_objects.weapons import Weapon
import game_objects.weapons as weapons_module
from game_objects.abilities import Ability
import game_objects.abilities as abilities_module


class UnitBase(ABC):
    name = ""
    faction = ""
    keywords = []
    melee_weapons = []
    ranged_weapons = []
    statistics: dict[str, int] = {}
    abilities: list[Ability] = []

    @classmethod
    def load_from_json(cls, file_name: str):
        with open(file_name, "r") as json_file:
            contents = json.load(json_file)

        obj = cls()
        obj.name = contents["name"]
        obj.faction = contents["faction"]
        obj.keywords = contents["keywords"]
        obj.statistics = contents["statistics"]
        obj.melee_weapons = contents["melee_weapons"]
        obj.ranged_weapons = contents["ranged_weapons"]
        for ability_name in contents["abilities"]:
            ability = ability_name.split(" ")
            if ability[1]:
                obj.abilities.append(getattr(abilities_module, ability[0])(int(ability[1])))
            else:                
                obj.abilities.append(getattr(abilities_module, ability_name)())
    def __init__(self):
        pass

    def calculate_to_hit(self):
        return [w.to_hit() for w in self.WEAPONS]

    def calculate_to_wound(self):
        pass

    def calculate_damage(self):
        pass

    def calculate_feel_no_pain(self): # wrzucić do calculate_damage
        pass
