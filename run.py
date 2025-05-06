# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
#
#
#
#
# remember to uncomment the time.sleep!!!!

# import time
import re
import random
import gspread
from google.oauth2.service_account import Credentials
from events import Predator


"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leaderboard')

board = SHEET.worksheet('highscores')
data = board.get_all_values()
# print(data)
"""


def display_intro():
    """
    This is shown at the start of the game
    """
    try:
        with open("intro_text.txt", "r") as file:
            intro_text = file.read()
            print(intro_text)
    except FileNotFoundError:
        print("Intro not found")


def display_help():
    """
    When the user types 'help' into the terminal,
    this will show the instructions
    """
    try:
        with open("intro_text.txt", "r") as file:
            intro_text = file.read()

            match = re.search(
                r"Instructions:(.*?)(?=\n\s*Hint:|$)", intro_text, re.DOTALL
                )

            if match:
                instructions = match.group(1).strip()
                print("\nInstructions:")
                print(f"{instructions}\n")
            else:
                print("Instructions section not found in the file.")
    except FileNotFoundError:
        print("Intro file not found!")


def name_species():
    """
    Lets the user name their species
    """
    global species_name
    while True:
        species_name = input("Give your species a name \
(max 15 characters): \n")
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

    # time.sleep(2)  # Delay to ensure the next line appears later

    print(f"\nYou have 10 evolutionary points to allocate between \
Strength and Speed \nfor the {species.name}.\n")

    # time.sleep(2)

    while True:
        try:
            # Get user input for strength allocation and check for validity
            while True:
                strength = int(input("Allocate points to Strength (0-10): \n"))
                if strength < 0 or strength > 10:
                    print("Points must be between 0 and 10. Try again.")
                else:
                    break

            # If the user allocates 10 points to strength, skip the speed step
            if strength == 10:
                species.strength = strength
                species.speed = 0
                species.evolutionary_points = 0
                print(f"Strength set to {strength}, Speed set to 0.")
                break

            # Calculate remaining points for speed
            remaining_points = 10 - strength

            # Get user input for speed allocation and check for validity
            while True:
                speed = int(input(f"Allocate points to \
Speed (0-{remaining_points}): \n"))
                if speed < 0 or speed > remaining_points:
                    print(f"Points must be between 0 and {remaining_points}. \
Try again.")
                else:
                    break

            # Allocate the points to the species
            species.strength = strength
            species.speed = speed
            species.evolutionary_points = 10 - (strength + speed)
            break

        except ValueError:
            # Handle case where the input is not an integer
            print("Please enter a valid number.")


def predator_encounter(species):
    """
    When the species encounters a predator,
    this function prompts the user for an action to take
    """
    predator = Predator(strength=15, speed=10)

    print(f"\nThe {species.name} has encountered a predator, \
the {predator.name}!\n")
    print(f"The {species.name} has {species.health} health.\n")

    # Basic game loop to prompt the user
    while species.health > 0:
        action = input("Do you want to 'fight' or 'flee'? \n").strip().lower()

        if "fight" in action or "attack" in action:
            print(f"The {species.name} decided to stand its ground and fight!")
            survived = predator.attack(species)  # Check if species survived
            if not survived:
                print(f"{species.name} has been defeated!")
                return  # Exit the loop if the species is defeated
        elif "flee" in action or "flight" in action:
            survived = predator.flee(species)  # Check if species survived
            if not survived:
                print(f"{species.name} has been defeated!")
                return  # Exit the loop if the species is defeated
        else:
            print("Invalid input. Please enter 'fight' or 'flee'.")
            continue

        # Check if species has been defeated
        if species.health > 0:
            break  # Exit the predator encounter and go back to main options
        else:
            print(f"{species.name} has been defeated. Game over.")
            return  # Exit the main loop if the species is defeated


def get_input(prompt, species):
    """
    This function calls the stats of the species as well as the instruction
    text whenever called upon.
    """
    if "stats" in prompt:
        species.print_stats()
    elif "help" in prompt:
        display_help()
    else:
        print("Invalid input. Please try again.")


def main():
    """
    Main function to start the game
    """
    from species import Species
    # Display the introduction when the game starts
    display_intro()

    # time.sleep(2)
    # Get the species name from the user
    species_name = name_species()

    # Initialize species with default health and user-defined attributes
    species = Species(name=species_name)
    # This one is important! It enables me to use the variable 'species'!

    # Allow the user to allocate points to strength and speed
    allocate_attributes(species)

    # Print species stats to see the output
    species.print_stats()

    # time.sleep(2)

    # Example of initializing a predator
    # later, the values for strength and speed will be randomised, but with
    # a multiplier depending on the progress of the game
    # predator_encounter(species)

    # This is the game loop!
    while species.health > 0:
        print("\nWhat would you like to do?")
        print("1. Gather food")
        print("2. Explore")
        print("3. See the leaderboard")
        print("4. Exit game")

        action = input("Enter your choice (1/2/3/4):\n").strip().lower()

        if "1" in action or "gather" in action or "food" in action:
            if random.random() < 1.1:
                predator_encounter(species)
            else:
                species.gather_food()
        elif "2" in action or "explore" in action:
            species.explore()
            species.evolve()
        elif "3" in action or "leader" in action:
            break  # Break for now, handle leaderboard later
        elif action == "4":
            print("Exiting game...")
            break
        else:
            get_input(action, species)


# Start the game
main()
