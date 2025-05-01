# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Species:
    def __init__(self, name, health, speed, strength, intelligence):
        # Initial traits of the species
        self.name = name
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

    def print_stats(self):
        # Print current species stats including the species name
        print(f"Species: {self.name}")
        print(f"Health={self.health}, Speed={self.speed}, \
Strength={self.strength}, Intelligence={self.intelligence}, \
Individuals={self.individuals}")


def display_intro():
    print("************************************************")
    print("*           Welcome to EVOLUTION!             *")
    print("*        A text-based evolution game.         *")
    print("************************************************")
    print("\n")
    print("In this game, you will guide a species through its evolutionary\n\
journey.")
    print("You will need to manage the traits of your species, adapt to\n\
changing environments, and face various challenges.")
    print("Survival depends on how well you adapt, evolve, and make\n\
decisions.")
    print("\n")

    # Add your instructions here
    print("Instructions: ")
    print("1. Allocate points to different traits of your species.")
    print("2. Evolve your species over multiple generations.")
    print("3. Face threats and challenges that will test your species'\n\
abilities.")
    print("4. Adapt, survive, and see how your species thrives!")
    print("\n")
    print("Let's begin!")
    print("************************************************")


def name_species():
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
        intelligence=0
        )

    # Print species stats to see the output
    species.print_stats()

    # Continue with game logic after the introduction
    # You can add more gameplay steps here


# Start the game
main()
