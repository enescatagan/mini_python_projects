from playsound import playsound
import time


# Manipulate Terminal with ANSI Escape Characters
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    """
    Play alarm sound after given time passes

    Args:
        seconds (int): How much seconds needs to pass for playing the alarm
    """
    time_elapsed = 0

    # Clear all Terminal
    print(CLEAR)
    while time_elapsed < seconds:
        # Wait 1 second and add in time_elapsed
        time.sleep(1)
        time_elapsed += 1

        minutes_left, seconds_left = _find_remaining_time(
            seconds, time_elapsed)

        # Print the remaining time on first line of terminal
        print(f"{CLEAR_AND_RETURN}"
              f"{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm_clock/alarm_sound.mp3")


def _find_remaining_time(seconds, time_elapsed):
    """
    Find Remaining time to show

    Args:
        seconds (int): How much seconds needs to pass for playing the alarm
        time_elapsed (int): The passing time

    Returns:
        minutes_left int: Remaining Minutes
        seconds_left int: Remaining Seconds
    """
    time_left = seconds - time_elapsed
    minutes_left = time_left // 60
    seconds_left = time_left % 60

    return minutes_left, seconds_left


# Enter time for alarm to run
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)
