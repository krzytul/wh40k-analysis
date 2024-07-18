
import json

from game_objects.abilities import Ability
from game_objects.weapons import Weapon
import game_objects.abilities as abilities_module
import importlib

if __name__ == '__main__':
    params = {}
    gauss = Weapon.load_from_json('./content/SampleWeapon.json')

    print(gauss.to_hit(params)["result"])