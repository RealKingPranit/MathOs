import curses
import time
import os

def set_cmd_title(title1):
    os.system(f"echo \033]0;{title1}\a")
def draw_loading_bar(stdscr):
    title1 = "Booting.MathOS"
    set_cmd_title(title1)
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Disable blocking for getch

    # Title and version information
    title_line1 = "██     ██    █████    ███████    █     █            █████      ███████"
    title_line2 = "█ █   █ █   █     █      █       █     █           █     █     ██"
    title_line3 = "█  █ █  █   █▀▀▀▀▀█      █       █▀▀▀▀▀█           █     █     ███████"
    title_line4 = "█   █   █   █     █      █       █     █           █     █          ██"
    title_line5 = "█       █   █     █      █       █     █            █████      ███████" 

    version = "v1.0"
    made_by = "Made by: Pranit Priyadarshi (from Class:- VIII-B)"

    # Calculate screen dimensions
    height, width = stdscr.getmaxyx()

    # Display the title across multiple lines
    title_y = height // 2 - 5
    title_x = width // 2 - len(title_line1) // 2

    stdscr.addstr(title_y, title_x, title_line1)
    stdscr.addstr(title_y + 1, title_x, title_line2)
    stdscr.addstr(title_y + 2, title_x, title_line3)
    stdscr.addstr(title_y + 3, title_x, title_line4)
    stdscr.addstr(title_y + 4, title_x, title_line5)

    # Calculate position for version and made by
    version_y = title_y + 6
    version_x = width // 2 - len(version) // 2

    made_by_y = version_y + 1  # Adjusted position for the loading bar
    made_by_x = width // 2 - len(made_by) // 2

    # Draw version and made by
    stdscr.addstr(version_y, version_x, version)
    stdscr.addstr(made_by_y, made_by_x, made_by)

    # Initialize variables for loading bar
    loading_bar_width = 30
    progress = 0

    while progress < loading_bar_width:
        # Update progress in the loading bar
        progress += 1
        loading_bar = '[' + '#' * progress + '-' * (loading_bar_width - progress) + ']'

        # Move the cursor and display loading bar
        stdscr.move(made_by_y + 1, width // 2 - loading_bar_width // 2)  # Adjusted position for the loading bar
        stdscr.addstr(loading_bar)

        # Refresh the screen
        stdscr.refresh()

        # Delay for animation
        time.sleep(0.1)

curses.wrapper(draw_loading_bar)
from menu import menu
menu()