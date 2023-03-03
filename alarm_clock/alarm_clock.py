from playsound import playsound
import time


# Manipulate Terminal with ANSI Characters
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    """Countdown method"""
    time_elapsed = 0

    # Clear all Terminal
    print(CLEAR)
    while time_elapsed < seconds:
        # Wait 1 second and add in time_elapsed
        time.sleep(1)
        time_elapsed += 1

        # Find Remaining time
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        second_left = time_left % 60

        # Print the remaining time on first line of terminal
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{second_left:02d}")


alarm(125)
