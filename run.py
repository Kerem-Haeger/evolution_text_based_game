import curses


def start_game(stdscr):
    # Function to simulate starting the game and showing the sub-menu
    stdscr.clear()

    # Sub-menu for "What would you like to do?"
    game_menu = ["Option 1", "Option 2", "Return to Main Menu"]
    current_row = 0  # Start at the first option

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "What would you like to do?\n")
        # Get terminal height to position the sub-menu at the bottom
        height, width = stdscr.getmaxyx()
        menu_y = height - len(game_menu) - 1

        # Display the sub-menu at the bottom
        for idx, row in enumerate(game_menu):
            x = 2  # Start a little bit off the left edge
            y = menu_y + idx  # Position the options starting at the bottom
            if idx == current_row:
                stdscr.addstr(y, x, row, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

        key = stdscr.getch()

        # Navigation through the game menu
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(game_menu) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            stdscr.clear()

            if current_row == 0:
                # Option 1 action
                stdscr.addstr(0, 0, "You chose Option 1!\n")
                stdscr.addstr(1, 0, "Press Enter to continue")
                stdscr.refresh()
                stdscr.getch()
                break  # Return to the "What would you like to do?" menu
            elif current_row == 1:
                # Option 2 action
                stdscr.addstr(0, 0, "You chose Option 2!\n")
                stdscr.addstr(1, 0, "Press Enter to continue")
                stdscr.refresh()
                stdscr.getch()
                break  # Return to the "What would you like to do?" menu
            elif current_row == 2:
                break  # Return to the main menu


def open_leaderboard(stdscr):
    # Function to simulate opening the leaderboard
    stdscr.clear()
    stdscr.addstr(0, 0, "Leaderboard\n")
    stdscr.refresh()
    stdscr.getch()  # Wait for user to press Enter
    return  # Return to the main menu


def quit_game(stdscr):
    # Function to simulate quitting the game
    stdscr.clear()
    stdscr.addstr(0, 0, "Exiting the game...\n")
    stdscr.refresh()
    stdscr.getch()  # Wait for any key press
    exit()  # Exit the program


def main(stdscr):
    # Clear screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Menu options
    menu = ["Start Game", "See Leaderboard", "Exit/Quit"]
    current_row = 0

    while True:
        height, width = stdscr.getmaxyx()  # Get screen dimensions

        # Clear screen and display instructions or game text
        stdscr.clear()

        # Display welcome message
        stdscr.addstr(0, 0, "Welcome to XYZ\n")
        stdscr.addstr(1, 0, "This is a game about evolution.\n")
        stdscr.addstr(2, 0, "Instructions:\n")
        stdscr.addstr(3, 0, "1. Do this\n")
        stdscr.addstr(4, 0, "2. Do that\n")
        stdscr.addstr(5, 0, "3. Keep playing!\n")
        stdscr.addstr(6, 0, "(use placeholder text for now)\n")

        # Now display the menu at the bottom
        menu_y = height - len(menu) - 1  # Position the menu at the bottom

        # Display the menu at the bottom of the screen
        for idx, row in enumerate(menu):
            x = 2  # Start a little bit off the left edge
            y = menu_y + idx  # Place menu options starting at the bottom
            if idx == current_row:
                stdscr.addstr(y, x, row, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

        key = stdscr.getch()  # Get user input

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            stdscr.clear()  # Clear the screen when a selection is made

            # Call the appropriate function based on the selected option
            if menu[current_row] == "Start Game":
                start_game(stdscr)
            elif menu[current_row] == "See Leaderboard":
                open_leaderboard(stdscr)
            elif menu[current_row] == "Exit/Quit":
                quit_game(stdscr)

            stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
