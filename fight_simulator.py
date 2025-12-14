"""
fight_simulator.py
Battle simulation module for Barcode Fighter game.
This module is standalone and can be imported by any main engine.
"""

from typing import Tuple, List


class Character:
    """
    Minimal Character placeholder.
    Your main engine should override this with the real Character class.
    This is only here to avoid import errors.
    """
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense


# ------------------------- Battle system -------------------------
def battle_simulator(char1: Character, char2: Character, verbose=True) -> Tuple[str, List[str]]:
    """
    Full battle simulator based on original conversation-based code.
    Runs turn-based combat until one HP <= 0 or 200 turns max.

    Returns:
        winner_name: str
        logs: List[str]
    """

    # clone HP so original unchanged
    hp1 = char1.hp
    hp2 = char2.hp
    logs = []
    turn = 1

    attacker, defender = (char1, char2)
    hp_att, hp_def = (hp1, hp2)

    # ------------- Main battle turns -------------
    while hp_att > 0 and hp_def > 0 and turn <= 200:

        if attacker.attack > defender.defense:
            damage = attacker.attack - defender.defense
            hp_def -= damage
            logs.append(
                f"Turn {turn}: {attacker.name} ({attacker.attack}) hits "
                f"{defender.name} ({defender.defense}) for {damage} damage. "
                f"Defender HP -> {max(0, hp_def)}"
            )
        else:
            logs.append(
                f"Turn {turn}: {attacker.name} ({attacker.attack}) failed to penetrate "
                f"{defender.name} ({defender.defense}). No damage."
            )

        # swap attacker & defender
        attacker, defender = defender, attacker
        hp_att, hp_def = hp_def, hp_att
        turn += 1

        if hp_def <= 0 or hp_att <= 0:
            break

    # ------------- Winner determination requires re-sim -------------
    hp1 = char1.hp
    hp2 = char2.hp
    turn = 1
    final_logs = []

    while hp1 > 0 and hp2 > 0 and turn <= 200:

        # char1 attacks
        if char1.attack > char2.defense:
            dmg = char1.attack - char2.defense
            hp2 -= dmg
            final_logs.append(f"T{turn}: {char1.name} deals {dmg} -> {max(0,hp2)}")
            if hp2 <= 0:
                break
        else:
            final_logs.append(f"T{turn}: {char1.name} failed to penetrate {char2.name}")

        # char2 attacks
        if char2.attack > char1.defense:
            dmg = char2.attack - char1.defense
            hp1 -= dmg
            final_logs.append(f"T{turn}: {char2.name} deals {dmg} -> {max(0,hp1)}")
            if hp1 <= 0:
                break
        else:
            final_logs.append(f"T{turn}: {char2.name} failed to penetrate {char1.name}")

        turn += 1

    # ------------- Winner -------------
    if hp1 <= 0 and hp2 <= 0:
        winner = "Draw"
    elif hp1 <= 0:
        winner = char2.name
    else:
        winner = char1.name

    return winner, (final_logs if verbose else [])


# ------------- Local module test -------------
if __name__ == "__main__":
    # quick test
    c1 = Character("Alpha", hp=5000, attack=1500, defense=700)
    c2 = Character("Beta", hp=4800, attack=1200, defense=900)

    winner, logs = battle_simulator(c1, c2, verbose=True)
    print("Winner:", winner)
    print("\n".join(logs))
