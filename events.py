# This module will handle random events, which will be called
# from the run.py file and can be re-used.

import random


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
