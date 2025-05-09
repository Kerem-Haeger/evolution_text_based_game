import curses


def draw_progress_bar(stdscr, progress, max_progress, bar_width=20, x=2, y=2):
    """
    Draw the progress bar.
    `progress` is the current value of the resource.
    `max_progress` is the maximum value of the resource.
    `bar_width` is the width of the progress bar in characters.
    """
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Calculate percentage of the progress
    progress_percentage = progress / max_progress

    # Calculate how many characters should be filled
    fill_length = int(bar_width * progress_percentage)
    empty_length = bar_width - fill_length

    # Create the bar using blocks for filled and empty portions
    filled_bar = "█" * fill_length
    empty_bar = " " * empty_length

    # Clear the screen and display the bar with text
    stdscr.clear()
    height, width = stdscr.getmaxyx()  # Get terminal size

    # Print the "Food: " part
    stdscr.addstr(y, x, "Food: ")

    # Print the progress bar with appropriate colors
    stdscr.addstr(y, x + 6, filled_bar, curses.color_pair(1))
    stdscr.addstr(y, x + 6 + fill_length, empty_bar, curses.color_pair(2))

    stdscr.refresh()


def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    max_progress = 100  # Max resource value

    # Variable you can manually change
    progress = 50  # (from 0 to max_progress)

    # Draw the progress bar once with the given progress
    draw_progress_bar(stdscr, progress, max_progress)

    # Wait for any key press before exiting
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
