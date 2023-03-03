from playsound import playsound
import time


def alarm(seconds):
    """Countdown method"""
    time_elapsed = 0

    while time_elapsed < seconds:
        # Wait 1 second and add in time_elapsed
        time.sleep(1)
        time_elapsed += 1

        # Find Remaining time and print
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        second_left = time_left % 60

        print(f"{minutes_left:02d}:{second_left:02d}")


alarm(125)
