import json

from game_objects.abilities import Ability
import game_objects.abilities as abilities_module
import importlib

class Weapon:
    REQUIRED_FIELDS = ["to_hit", "damage"] # dodaj co chcesz
    statistics: dict[str, int] = {}
    abilities: list[Ability] = []

    @classmethod
    def load_from_json(cls, file_name: str):
        with open(file_name, "r") as json_file:
            contents = json.load(json_file)

        obj = cls()
        # unpack json
        if set(cls.REQUIRED_FIELDS) != set(contents["statistics"].keys()):
            raise ValueError("Missing required fields")

        obj.statistics = contents["statistics"]
        for ability_name in contents["abilities"]:
            obj.abilities.append(getattr(abilities_module, ability_name)())

        return obj

    def get_base_to_hit(self, params: dict) -> dict:
        return {"to_hit": self.statistics["to_hit"]} | params

    def to_hit(self, params):
        result = self.get_base_to_hit(params)
        for ability in self.abilities:
            result = ability.to_hit(result)
        return result


if __name__ == '__main__':
    weapon = Weapon.load_from_json("../content/SampleWeapon.json")
    print()