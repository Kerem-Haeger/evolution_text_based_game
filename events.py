# This module will handle random events, which will be called
# from the run.py file and can be re-used.

import random


def ice_age(species):
    pass


def volcano_eruption(species):
    pass


def drought(species):
    pass


def flood(species):
    pass


def predator_attack(species):
    pass


events = [ice_age, volcano_eruption, drought, flood, predator_attack]


def trigger_random_event(species):
    event = random.choice(events)
    event(species)
