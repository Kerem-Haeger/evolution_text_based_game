# This module will handle random events, which will be called
# from the run.py file and can be re-used.

import random


class Predator:
    def __init__(self, strength, speed):
        self.names = [
            "Vraxil", "Sivrok", "Zalgaroth", "Khethar", "Drathok",
            "Veylor", "Rulgar", "Marnak", "Traskir", "Yshara",
            "Vornash", "Gorthar", "Blaykoth", "Kryzaar", "Draxum",
            "Zirran", "Xarvok", "Krivanth", "Heshir", "Yzool",
            "Thrakar", "Vortha", "Zhanok", "Klarth", "Rendarr",
            "Fylzhar", "Thallor", "Xylar", "Drakar", "Mornak",
            "Galdoth", "Wrogar", "Kynthar", "Jhulak", "Fornash",
            "Vornak", "Xharnok", "Zylar", "Brastok", "Vayzon",
            "Rithar", "Vrekshar", "Jorlan", "Torvok", "Khoran",
            "Trystar", "Vishnar", "Vorhax", "Rakshor", "Zolrith"
            ]

        self.name = random.choice(self.names)
        self.strength = strength
        self.speed = speed

    def attack(self, species):
        print(f"The {self.name} attacks {species.name}!")

        species_chance = species.strength / (species.strength + self.strength)

        outcome = random.random()

        if outcome < species_chance:
            print(f"{species.name} manages to fend off the attack!")

            damage = round(self.strength * random.uniform(0.1, 0.5))
            species.health -= damage
            print(f"{species.name} takes {damage} damage but survives \
the attack!")
        else:
            print(f"The {self.name} overpowers {species.name}!")
            damage = round(self.strength * random.uniform(0.5, 1.5))
            species.health -= damage
            print(f"{species.name}'s health is now {species.health}.")

        if species.health <= 0:
            print(f"{species.name} has been defeated!")
            # Here I need to call a 'game ends' function at some point!
        elif self.health <= 0:
            print(f"{self.name} has been defeated!")


def ice_age(species):
    return "ice age"


def volcano_eruption(species):
    return "volcanic eruption"


def drought(species):
    return "drought"


def flood(species):
    return "flood"


def predator_attack(species):
    return "predator"


events = [ice_age, volcano_eruption, drought, flood, predator_attack]


def trigger_random_event(species):
    event = random.choice(events)
    return event(species)
