import json
import os
from character import Character

BASE_PATH = os.path.dirname(os.path.abspath(__file__))   # string type
DB_PATH = f"{BASE_PATH}/mnt/data/barcode_char_db.json"

class CharacterDatabase:

    def __init__(self):
        if os.path.exists(DB_PATH):
            with open(DB_PATH, "r") as f:
                self.db = json.load(f)
        else:
            self.db = {}

    def get_or_create(self, character: "Character"):
        cid = character.character_id
        if cid in self.db:
            return self.db[cid]
        self.db[cid] = character.to_dict()
        self._save()
        return self.db[cid]

    def _save(self):
        # print(DB_PATH)
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH, "w") as f:
            json.dump(self.db, f, indent=2)
