# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Species:
    def __init__(self, name, health, speed, strength, intelligence,
                 is_predator):
        # Initial traits of the species
        self.name = name
        self.health = health
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.is_predator = is_predator
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

    def print_stats(self):
        """
        Print current species stats, including name
        """
        print(f"\nSpecies: {self.name}")
        print(f"Health: {self.health}, Speed: {self.speed}, \
Strength: {self.strength}, Intelligence: {self.intelligence}, \
Individuals: {self.individuals}")
        if self.is_predator:
            print(f"{self.name} is a predator!")
        else:
            print(f"{self.name} is not a predator.")


def display_intro():
    intro_text = """
************************************************
*           Welcome to EVOLUTION!             *
*        A text-based evolution game.         *
************************************************

In this game, you will guide a species through its evolutionary journey.
You will need to manage the traits of your species, adapt to changing
environments, and face various challenges.
Survival depends on how well you adapt, evolve, and make decisions.

Instructions:
1. Allocate points to different traits of your species.
2. Evolve your species over multiple generations.
3. Face threats and challenges that will test your species' abilities.
4. Adapt, survive, and see how your species thrives!

Let's begin!
************************************************
"""
    print(intro_text)


def name_species():
    """
    Lets the user name their species
    """
    global species_name
    while True:
        species_name = input("Give your species a name (max 15 characters): ")
        if len(species_name) > 15:
            print("Name is too long! Please enter a name with 15 characters \
or less.")
        else:
            break

    return species_name


def main():
    # Display the introduction when the game starts
    display_intro()

    # Get the species name from the user
    species_name = name_species()

    # Initialize species or game state here with the name provided
    species = Species(
        name=species_name,
        health=100,
        speed=5,
        strength=5,
        intelligence=0,
        is_predator=False
        )

    # Print species stats to see the output
    species.print_stats()


"""
User needs to set stats themselves!
"""

# Start the game
main()
