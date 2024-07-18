import json

from game_objects.abilities import Ability
import game_objects.abilities as abilities_module
import importlib

class Weapon:
    REQUIRED_FIELDS = ["range","attacks", "balistic_skill","strength","armour_penetration","damage"] # dodaj co chcesz
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
            ability = ability_name.split(" ")
            if ability[1]:
                obj.abilities.append(getattr(abilities_module, ability[0])(int(ability[1])))
            else:                
                obj.abilities.append(getattr(abilities_module, ability_name)())
        return obj

    def to_hit(self, params):
        if isinstance(self.statistics["attacks"],int):
            result = self.statistics["attacks"]
        elif isinstance(self.statistics["attacks"],str):
            result = parse_DX_roll(self.statistics["attacks"])
        
        BS = self.statistics["balistic_skill"]
        match BS:
            case 1:
                base_result = result
            case 2:
                base_result = result*5/6
            case 3:
                base_result = result*2/3
            case 4:
                base_result = result/2
            case 5:
                base_result = result/3
            case 6:
                base_result = result/6
        params["result"] = base_result
        params["base_result"] = base_result
        for ability in self.abilities:
            params = ability.to_hit(params)
        params.pop("base_result")
        return params


if __name__ == '__main__':
    weapon = Weapon.load_from_json("../content/SampleWeapon.json")
    print()

    gauss = Weapon.load_from_json('../content/SampleWeapon.json')

    print(gauss.to_hit()["result"])



def parse_DX_roll(value: str) -> int:
    x = value.split("D")
    const = 0
    if x[0]=='': 
        mult = 1
    else:
        mult = int(x[0])
    y = x[1].split("+")
    if len(y)>1:
        const = int(y[1])
    result = float(y[0])/2 + 0.5
    result = mult*result+const
    return result 


