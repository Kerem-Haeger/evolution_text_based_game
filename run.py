# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Species:
    def __init__(self, health, speed, strength, intelligence):
        # Initial traits of the species
        self.health = health
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.individuals = 1

    def mutate(self):
        """
        Implement random mutation of traits
        """
        import random
        mutation_strength = random.uniform(-0.5, 0.5)
        self.health += mutation_strength
        self.speed += mutation_strength
        self.strength += mutation_strength
        self.intelligence += mutation_strength
