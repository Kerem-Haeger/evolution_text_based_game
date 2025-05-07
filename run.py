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
from rich.console import Console
from rich.prompt import Prompt
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from rich import print
# import gspread
# from google.oauth2.service_account import Credentials
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
    """ This is shown at the start of the game """
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
                print(f"\nInstructions:\n{instructions}\n")
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
        species_name = input("""
Give your species a name (max 15 characters):\n
""")
        if len(species_name) > 15:
            print("""
Name is too long! Please enter a name with 15 characters or less.
                """)
        else:
            break

    species_name = species_name.upper()
    return species_name


def allocate_attributes(species):
    """
    Let the user allocate attributes to the species
    """
    print(f"""
\nTime to customise the {species.name}! In the Proterozoic Era,
the {species.name} is a multicellular organism, eager to evolve!
    """)

    # time.sleep(2)  # Delay to ensure the next line appears later

    print(f"""
You have 10 evolutionary points to allocate between Strength and Speed
for the {species.name}.\n
    """)

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
                speed = int(input(f"""
Allocate points to Speed (0-{remaining_points}):
"""))
                if speed < 0 or speed > remaining_points:
                    print(f"""
Points must be between 0 and {remaining_points}. Try again.
""")
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

    print(f"""
\nThe {species.name} has encountered a predator, the {predator.name}!\n
    """)
    print(f"The {species.name} has {species.health} health.\n")

    # Basic game loop to prompt the user
    while species.health > 0:
        # Use prompt_toolkit for handling the input to support key bindings
        action = prompt("Do you want to 'fight' or 'flee'? [Fight/Flee]\n").strip().lower()

        if "fight" in action or "attack" in action:
            print(f"The {species.name} decided to stand its ground and fight!")
            survived = predator.attack(species)  # Check if species survived
            if not survived:
                print(f"{species.name} has been defeated!")
                return "The species was defeated by the predator!"  # Return the result of the encounter
        elif "flee" in action or "flight" in action:
            survived = predator.flee(species)  # Check if species survived
            if not survived:
                print(f"{species.name} has been defeated!")
                return "The species failed to flee and was defeated!"
        else:
            print("Invalid input. Please enter 'fight' or 'flee'.")
            continue

        # Check if species has been defeated
        if species.health > 0:
            break  # Exit the predator encounter and go back to main options
        else:
            print(f"{species.name} has been defeated. Game over.")
            return "The species was defeated in combat."

    return "The species survived the encounter."


def get_input(user_input, species):
    """
    This function calls the stats of the species as well as the instruction
    text whenever called upon.
    """
    if "stats" in user_input:
        species.print_stats()
    elif "help" in user_input:
        display_help()
    else:
        print("Invalid input. Please try again.")


def display_menu(options, selected_index, species, action_feedback=""):
    """
    Display the menu with the currently selected option
    highlighted and keep the species stats visible.
    Optionally show action feedback (what just happened).
    """
    console = Console()
    console.clear()  # Clear the terminal

    # Display species stats (above the menu)
    species.print_stats()

    # Display action feedback (e.g., what the species just did)
    if action_feedback:
        print(f"[bold yellow]{action_feedback}[/bold yellow]")

    # Display the prompt (below the species stats and action feedback)
    print(f"\n[bold green]Choose an action:[/bold green]\n")

    # Display options with the selected one highlighted
    for i, option in enumerate(options):
        if i == selected_index:
            # Highlight the selected option: black text on white background
            print(f"> [black on white]{option}[/black on white] <")
        else:
            # Display non-selected options normally
            print(f"  {option}")


def main():
    """
    Main function to start the game with simpler inputs
    """
    from species import Species
    console = Console()  # Initialize Rich console for output

    # Display the introduction when the game starts
    display_intro()

    # Get the species name from the user
    species_name = name_species()

    # Initialize species with default health and user-defined attributes
    species = Species(name=species_name)

    # Allow the user to allocate points to strength and speed
    allocate_attributes(species)

    # Print species stats to see the output
    species.print_stats()

    # Create a list of options for the menu
    options = [
        "Gather food",
        "Explore",
        "See the leaderboard",
        "Exit game"
    ]

    # Initialize selected index
    selected_index = 0

    # Set up a flag to control the game loop
    running = True

    # Key bindings to navigate through the menu
    kb = KeyBindings()

    @kb.add('up')
    def up(event):
        nonlocal selected_index
        # Move up through the menu, wrap around to the bottom
        selected_index = (selected_index - 1) % len(options)
        display_menu(options, selected_index, species)

    @kb.add('down')
    def down(event):
        nonlocal selected_index
        # Move down through the menu, wrap around to the top
        selected_index = (selected_index + 1) % len(options)
        display_menu(options, selected_index, species)

    @kb.add('enter')
    def enter(event):
        nonlocal running
        action_feedback = ""
        # When enter is pressed, execute the selected option
        selected_action = options[selected_index]
        if selected_action == "Gather food":
            if random.random() < 0.1:
                predator_encounter(species)
                action_feedback = f"The {species.name} encountered a predator!"
            else:
                outcome = species.gather_food()
                action_feedback = f"The {species.name} attempted to gather food. Outcome: {outcome}"
        elif selected_action == "Explore":
            # species.explore()
            action_feedback = f"The {species.name} explored the surroundings."
        elif selected_action == "See the leaderboard":
            action_feedback = "Leaderboard is not implemented yet."
        elif selected_action == "Exit game":
            print("Exiting game...")
            exit()

        # Show the updated stats and the action feedback
        display_menu(options, selected_index, species, action_feedback)

        # Stop the game loop for now after showing feedback
        running = False

    # Start the menu loop
    display_menu(options, selected_index, species)

    while running:
        # Keep the prompt active for handling keypresses
        prompt("""
Press Enter to select an option, or use Up/Down arrow keys to navigate...
        """, key_bindings=kb)


# Start the game
main()
