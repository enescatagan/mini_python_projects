from playsound import playsound
import time


# Manipulate Terminal with ANSI Escape Characters
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


class Alarm:

    def __init__(self):
        self.time_elapsed = 0

        self.total_seconds = 0

        self.minutes = None
        self.seconds = None

        self.minutes_left = 0
        self.seconds_left = 0

    def alarm(self):
        """
        Play alarm sound after given time passes

        Args:
            total_seconds (int): How much seconds needs to pass for playing the alarm
        """
        # Get time from user
        self.get_time()

        # Clear Terminal
        print(CLEAR)
        while self.time_elapsed < self.total_seconds:
            # Wait 1 second and add in time_elapsed
            time.sleep(1)
            self.time_elapsed += 1

            # Get remaining time to show
            self._find_remaining_time()

            # Print the remaining time on first line of terminal
            print(f"{CLEAR_AND_RETURN}"
                  f"{self.minutes_left:02d}:{self.seconds_left:02d}")

        playsound("alarm_clock/alarm_sound.mp3")

    def _find_remaining_time(self):
        """
        Find Remaining time to show

        Args:
            seconds (int): How much seconds needs to pass for playing the alarm
            time_elapsed (int): The passing time
        """
        time_left = self.total_seconds - self.time_elapsed
        self.minutes_left = time_left // 60
        self.seconds_left = time_left % 60

    def get_time(self):
        """
        Get time values from user:
        minutes and seconds
        """
        while True:
            try:
                if self.minutes == None:
                    self.minutes = int(input("Enter Minutes: "))
                if self.seconds == None:
                    self.seconds = int(input("Enter Seconds: "))
                break
            except ValueError:
                print("Please Enter integer Value")
                continue

        self._calc_total_seconds()

    def _calc_total_seconds(self):
        """Calculate total seconds"""
        self.total_seconds = (self.minutes * 60) + self.seconds
