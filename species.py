import random


class Species:
    def __init__(self, name, health=100, speed=0, strength=0, intelligence=0,
                 is_predator=False):
        # Initial traits of the species
        self.name = name
        self.health = health
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence  # Later use?
        # Above traits are customisable and can evolve!
        self.is_predator = is_predator  # Determine what food to get
        self.individuals = 1
        self.food = 0  # To multiply
        self.experience = 0  # To level up and progress in time!
        self.evolutionary_points = 0  # For later use!
        self.num_of_fights = 0  # Determine predominant strategy and fitness
        self.num_of_flee = 0  # Determine predominant strategy and fitness

    def mutate(self):
        """
        Implement random mutation of traits
        """
        # For each trait, generate a random mutation value (-1, 0, or 1)
        self.health += random.choice([-1, 0, 1])
        self.speed += random.choice([-1, 0, 1])
        self.strength += random.choice([-1, 0, 1])
        self.intelligence += random.choice([-1, 0, 1])

        self.health = max(0, self.health)
        self.speed = max(0, self.speed)
        self.strength = max(0, self.strength)
        self.intelligence = max(0, self.intelligence)

    def print_stats(self):
        """
        Print current species stats, including name
        """
        print(f"\nSpecies: {self.name}")

        print(f"Health: {self.health}, Speed: {self.speed}, \
Strength: {self.strength}, Intelligence: {self.intelligence}, \
Individuals: {self.individuals}")

        if self.is_predator:
            print(f"The {self.name} is a predator!\n")
        else:
            print(f"The {self.name} is not a predator.\n")
