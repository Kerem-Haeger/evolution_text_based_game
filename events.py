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
