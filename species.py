import random


class Species:
    def __init__(self, name, health=100, speed=0, strength=0, intelligence=0,
                 is_predator=False):
        # Initial traits of the species
        self.name = name
        self.health = health
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence  # Will show up in the Mesozoic Era
        # Above traits are customisable and can evolve!
        self.is_predator = is_predator  # Determine what food to get
        self.individuals = 1
        self.food = 0  # To multiply!

        self.determine_predator = 0  # At a certain amount, become predator

        self.fitness_factors = {
            "hunting": {"health": 0.2, "speed": 0.4, "strength": 0.4,
                        "intelligence": 0.0},
            "gathering": {"health": 0.1, "speed": 0.3, "strength": 0.2,
                          "intelligence": 0.4},
            "predator": {"health": 0.3, "speed": 0.3, "strength": 0.4,
                         "intelligence": 0.0},
            "default": {"health": 0.3, "speed": 0.3, "strength": 0.3,
                        "intelligence": 0.1}
        }

        self.state = "default"

    def calculate_fitness(self):
        """
        Calculate the fitness based on the current state of the species.
        The fitness is a weighted sum of traits, where the weights change
        depending on the species' needs (e.g., hunting, gathering).
        """
        factors = self.fitness_factors[self.state]

        # Calculate fitness by applying the weights to the traits
        fitness = (self.health * factors['health'] +
                   self.speed * factors['speed'] +
                   self.strength * factors['strength'] +
                   self.intelligence * factors['intelligence'])
        return fitness

    def set_state(self, new_state):
        """
        Set the species' state.
        """
        self.state = new_state

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
        fitness = self.calculate_fitness()
        print(f"\nSpecies: {self.name}")

        print(f"Health: {self.health}, Speed: {self.speed}, \
Strength: {self.strength}, Intelligence: {self.intelligence}, \
Individuals: {self.individuals}")

        print(f"Fitness: {fitness}\n")

        if self.is_predator:
            print(f"The {self.name} is a predator!\n")
        else:
            print(f"The {self.name} is not a predator.\n")
