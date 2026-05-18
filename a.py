import random
import time
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Item:
    name: str
    power: int
    value: int

    def describe(self) -> str:
        return f"{self.name} | Power: {self.power} | Value: {self.value}"


@dataclass
class Character:
    name: str
    hp: int
    attack: int
    defense: int
    gold: int = 0
    inventory: List[Item] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> int:
        reduced = max(amount - self.defense, 0)
        self.hp -= reduced
        return reduced

    def add_item(self, item: Item) -> None:
        self.inventory.append(item)

    def show_inventory(self) -> None:
        print(f"\n{self.name}'s Inventory:")
        if not self.inventory:
            print("  Empty")
            return

        for index, item in enumerate(self.inventory, start=1):
            print(f"  {index}. {item.describe()}")

    def strongest_item(self) -> Optional[Item]:
        if not self.inventory:
            return None
        return max(self.inventory, key=lambda item: item.power)


class BattleArena:
    def __init__(self, hero: Character):
        self.hero = hero
        self.enemies = self.generate_enemies()

    def generate_enemies(self) -> List[Character]:
        names = [
            "Goblin",
            "Skeleton",
            "Bandit",
            "Dark Mage",
            "Wolf",
            "Orc",
        ]

        enemies = []

        for _ in range(6):
            enemy = Character(
                name=random.choice(names),
                hp=random.randint(30, 70),
                attack=random.randint(5, 14),
                defense=random.randint(1, 5),
                gold=random.randint(10, 50),
            )
            enemies.append(enemy)

        return enemies

    def battle(self, enemy: Character) -> bool:
        print(f"\nA wild {enemy.name} appears!")
        print("-" * 40)

        round_number = 1

        while self.hero.is_alive() and enemy.is_alive():
            print(f"\nRound {round_number}")

            hero_attack = self.hero.attack + random.randint(0, 6)
            dealt = enemy.take_damage(hero_attack)

            print(
                f"{self.hero.name} attacks "
                f"{enemy.name} for {dealt} damage."
            )

            if not enemy.is_alive():
                print(f"{enemy.name} has been defeated!")
                self.hero.gold += enemy.gold
                print(f"Looted {enemy.gold} gold.")
                return True

            enemy_attack = enemy.attack + random.randint(0, 4)
            received = self.hero.take_damage(enemy_attack)

            print(
                f"{enemy.name} attacks "
                f"{self.hero.name} for {received} damage."
            )

            print(
                f"{self.hero.name} HP: {self.hero.hp} | "
                f"{enemy.name} HP: {enemy.hp}"
            )

            round_number += 1
            time.sleep(0.3)

        return self.hero.is_alive()

    def reward_player(self) -> None:
        possible_items = [
            Item("Iron Sword", 5, 40),
            Item("Silver Shield", 3, 35),
            Item("Magic Ring", 7, 60),
            Item("Healing Potion", 1, 20),
            Item("Dragon Helm", 9, 100),
        ]

        item = random.choice(possible_items)

        print(f"\nReward found: {item.describe()}")
        self.hero.add_item(item)

        if item.power > 5:
            self.hero.attack += 2
            print("Your attack increased!")

    def start(self) -> None:
        print("=" * 50)
        print("        WELCOME TO THE BATTLE ARENA")
        print("=" * 50)

        for enemy in self.enemies:
            survived = self.battle(enemy)

            if not survived:
                print("\nYou have fallen in battle.")
                return

            self.reward_player()

            print(f"\nCurrent Gold: {self.hero.gold}")
            print("-" * 50)

        print("\nCongratulations!")
        print(f"{self.hero.name} defeated all enemies!")

        self.hero.show_inventory()

        best = self.hero.strongest_item()

        if best:
            print(f"\nStrongest Item: {best.name}")


def create_hero() -> Character:
    names = ["Arin", "Luna", "Kael", "Nyra"]

    hero = Character(
        name=random.choice(names),
        hp=120,
        attack=12,
        defense=4,
        gold=25,
    )

    starter_item = Item("Starter Blade", 2, 10)
    hero.add_item(starter_item)

    return hero


def game_intro() -> None:
    lines = [
        "In a forgotten kingdom...",
        "Warriors fight for glory.",
        "Only one survives the arena.",
    ]

    for line in lines:
        print(line)
        time.sleep(0.6)

    print()


def main() -> None:
    random.seed()

    game_intro()

    hero = create_hero()

    print(f"Hero created: {hero.name}")
    print(f"HP: {hero.hp}")
    print(f"Attack: {hero.attack}")
    print(f"Defense: {hero.defense}")

    arena = BattleArena(hero)
    arena.start()

    print("\nGame Over")


if __name__ == "__main__":
    main()