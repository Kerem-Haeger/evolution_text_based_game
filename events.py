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
        print(f"\nThe {self.name} attacks the {species.name}!")

        species_chance = species.strength / (species.strength + self.strength)
        outcome = random.random()

        if outcome < species_chance:
            print(f"\nThe {species.name} manages to fend off the attack!")
            damage = round(self.strength * random.uniform(0.1, 0.3))
            species.health -= damage
            species.determine_predator += 1

            print(f"\nThe {species.name} takes {damage} damage but survives \
the attack!\nThe {species.name} now has {species.health} health.")
        else:
            print(f"\nThe {self.name} overpowers the {species.name}!")
            damage = round(self.strength * random.uniform(0.5, 1.5))
            species.health -= damage
            print(f"\nThe {species.name}'s health is now {species.health}.")

        # Return a boolean to indicate if the species survived the encounter
        if species.health <= 0:
            print(f"\nThe {species.name} has been defeated!")
            return False  # Species is defeated
        return True  # Species survived the attack

    def flee(self, species):
        adjusted_species_speed = species.speed / (
            1 + 0.1 * (species.individuals - 1))

        print(f"\nThe {species.name} is attempting to flee from \
the {self.name}!")

        if adjusted_species_speed > self.speed:
            print(f"\nThe {species.name} successfully flees from \
the {self.name}!")
            damage = round(self.strength * random.uniform(0.1, 0.3))
            species.health -= damage
            print(f"\nThe {species.name} takes {damage} damage but \
survives the encounter!\nThe {species.name} now has {species.health} health.")
            return True  # Successfully flees, continue the game
        else:
            print(f"\nThe {self.name} catches up to the {species.name}!")

            if species.individuals > 1:
                outcome = random.choice(["individuals"])

                if outcome == "individuals":
                    lost_individuals = random.randint(
                        1, species.individuals // 2)
                    species.individuals -= lost_individuals
                    print(f"\nThe {species.name} loses {lost_individuals} \
individuals! The remaining individuals: {species.individuals}.")

            # Attack after failing to flee
            survived = self.attack(species)
            return survived  # Return whether the species survived the attack


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
