# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Species:
    def __init__(self, name, health=100, speed=0, strength=0, intelligence=0,
                 is_predator=False):
        # Initial traits of the species
        self.name = name
        self.health = health
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.is_predator = is_predator
        self.individuals = 1
        self.evolutionary_points = 0  # For later use!

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
            print(f"The {self.name} is a predator!")
        else:
            print(f"The {self.name} is not a predator.")


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

    species_name = species_name.upper()
    return species_name


def allocate_attributes(species):
    """
    Let the user allocate attributes to the species
    """
    print(f"\nTime to customise the {species.name}! In the Proterozoic Era, \
the {species.name} is a \nmulticellular organism, eager to evolve!")
    print(f"\nYou have 10 evolutionary points to allocate between \
Strength and Speed \nfor the {species.name}.")

    # Allocate 10 points between strength and speed
    while True:
        try:
            # Get user input for strength allocation and check for validity
            strength = int(input("Allocate points to Strength (0-10): "))
            if strength < 0 or strength > 10:
                print("Points must be between 0 and 10. Try again.")
                continue

            # If the user allocates 10 points to strength, skip the speed step
            if strength == 10:
                species.strength = strength
                species.speed = 0
                species.evolutionary_points = 0
                print(f"Strength set to {strength}, Speed set to 0.")
                break

            # If not 10, get user input for speed and check for validity
            speed = int(input("Allocate points to Speed (0-10): "))
            if speed < 0 or speed > 10:
                print("Points must be between 0 and 10. Try again.")
                continue

            # Check that the total allocation does not exceed 10 points
            if strength + speed > 10:
                print("Total allocation exceeds 10 points. Try again.")
                continue

            # If all inputs are valid, allocate the points to the species
            species.strength = strength
            species.speed = speed
            species.evolutionary_points = 10 - (strength + speed)
            break

        except ValueError:
            # Handle case where the input is not an integer
            print("Please enter valid numbers for strength and speed.")


def main():
    """
    Main function to start the game
    """
    # Display the introduction when the game starts
    display_intro()

    # Get the species name from the user
    species_name = name_species()

    # Initialize species with default health and user-defined attributes
    species = Species(name=species_name)
    # This one is important! It enables me to use the variable 'species'!

    # Allow the user to allocate points to strength and speed
    allocate_attributes(species)

    # Print species stats to see the output
    species.print_stats()
    print(species.evolutionary_points)  # Only for me to check!


# Start the game
main()
