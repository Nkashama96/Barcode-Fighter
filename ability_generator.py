import hashlib
import random

class AbilityGenerator:

    RARITY_TABLE = [
        ("normal",        0.45),
        ("rare",          0.20),
        ("super_rare",    0.15),
        ("ultra_rare",    0.13),
        ("legendary",     0.065),
        ("ultra_legend",  0.0044),
        ("unique",        0.0001)
    ]

    RARITY_RANGES = {
        "normal":        (300,   3000,   300,   1500,   300,   1500),
        "rare":          (3000,  8000,   1500,  5000,   1500,  5000),
        "super_rare":    (8000,  30000,  5000,  15000,  5000,  15000),
        "ultra_rare":    (30000, 50000,  15000, 30000,  15000, 30000),
        "legendary":     (50000, 80000,  30000, 50000,  30000, 50000),
        "ultra_legend":  (50000, 80000,  30000, 50000,  30000, 50000),
        "unique":        (80000, 99999,  80000, 99999,  80000, 99999)
    }

    SPECIAL_CHANCE = 0.0005  # = 0.05%

    @staticmethod
    def _rand_from_hash(hash_hex: str, start: int, length: int) -> int:
        sub = hash_hex[start:start+length]
        return int(sub, 16)

    @staticmethod
    def pick_rarity(seed: float):
        acc = 0
        for rarity, percentage in AbilityGenerator.RARITY_TABLE:
            acc += percentage
            if seed < acc:
                return rarity
        return "normal"

    @staticmethod
    def generate_abilities(hash_hex: str):
        # Deterministic random seed from hash
        seed_val = int(hash_hex[:16], 16)
        rng = random.Random(seed_val)

        # Pick rarity
        rarity_seed = (seed_val % 1000000) / 1000000.0
        rarity = AbilityGenerator.pick_rarity(rarity_seed)

        hp_min, hp_max, atk_min, atk_max, def_min, def_max = AbilityGenerator.RARITY_RANGES[rarity]

        hp = rng.randint(hp_min, hp_max)
        atk = rng.randint(atk_min, atk_max)
        defense = rng.randint(def_min, def_max)

        # Special 0.05% boost
        if rng.random() < AbilityGenerator.SPECIAL_CHANCE:
            rarity = rarity + "_special"
            boost = rng.randint(5000, 15000)
            hp += boost
            atk += boost // 2
            defense += boost // 3

        hp = min(hp, 99999)
        atk = min(atk, 99999)
        defense = min(defense, 99999)

        return rarity, hp, atk, defense
