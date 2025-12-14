import hashlib
import json
import random
from faker import Faker

from ability_generator import AbilityGenerator

ELEMENTS = ["fire", "water", "ground", "light", "dark", "gold"]

# MYTH_NAMES = [
#     "Zeus","Hera","Ares","Athena","Hermes","Apollo","Artemis",
#     "Poseidon","Hades","Perseus","Achilles","Heracles"
# ]
fake = Faker()

class Character:

    def __init__(self, original_input, normalized_hash):
        self.original_input = original_input
        self.normalized_hash = normalized_hash
        
        rarity, hp, atk, defense = AbilityGenerator.generate_abilities(normalized_hash)
        self.rarity = rarity
        self.hp = hp
        self.atk = atk
        self.defense = defense

        seed = int(normalized_hash[0:8], 16)
        rng = random.Random(seed)
        self.element = rng.choice(ELEMENTS)
        # self.name = rng.choice(MYTH_NAMES)
        self.name = fake.first_name()

        self.character_id = self.generate_character_id()

    def generate_character_id(self):
        payload = {
            "src": self.original_input,
            "hash": self.normalized_hash,
            "rarity": self.rarity,
            "hp": self.hp,
            "atk": self.atk,
            "def": self.defense,
            "element": self.element,
            "name": ' '#self.name
        }
        raw = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha3_512(raw).hexdigest()

    def to_dict(self):
        return {
            "id": self.character_id,
            "original": self.original_input,
            "hash": self.normalized_hash,
            "rarity": self.rarity,
            "hp": self.hp,
            "atk": self.atk,
            "def": self.defense,
            "element": self.element,
            "name": self.name
        }
