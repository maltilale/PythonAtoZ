# PROBLEM STATEMENT:
# Create a countdown timer application that counts down from a user-specified
# time and triggers an alarm when the countdown reaches zero.

# REQUIREMENTS:
# 1. USER INPUT:
#    - Accept time input in one of these formats:
#      * Seconds only (e.g., 60)
#      * Minutes and seconds (e.g., 5:30)
#      * Hours, minutes, and seconds (e.g., 1:30:45)
#    - Validate the input to ensure it's a valid time format
#    - Handle edge cases (negative numbers, invalid formats, etc.)

# 2. COUNTDOWN DISPLAY:
#    - Display the remaining time in HH:MM:SS format
#    - Update the display every second
#    - Clear/overwrite the previous display line (not print new lines)
#    - Show a smooth countdown experience

# 3. ALARM TRIGGER:
#    - When countdown reaches 00:00:00, trigger an alarm
#    - Options for alarm:
#      * Print a visual alert message
#      * Play a beep sound (bonus)
#      * Flash the console (bonus)
#      * Print ASCII art alarm bell (bonus)

# 4. ADDITIONAL FEATURES (Optional):
#    - Pause/Resume functionality (using keyboard input)
#    - Reset timer option
#    - Show progress bar along with timer
#    - Allow setting multiple alarms
#    - Save/Load preset timers
#    - Display motivational messages at intervals

from datetime import datetime, timedelta
from typing import NoReturn
import time

TIME_FORMAT = "%H:%M:%S"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BOLD = "\033[1m"
BG_RED = "\033[41m"


def get_time_input(prompt: str) -> datetime:
    while True:
        try:
            input_time = input(f"{prompt}")
            input_time_object = datetime.strptime(input_time, TIME_FORMAT)
            return input_time_object
        except ValueError:
            print(
                "Error: Invalid time format. Please use format HH:MM:SS (e.g 1:30:45)"
            )
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted")
            raise


class CountDownManager:

    def __init__(self, input_time):
        self.user_input_time = input_time
        self.remaining = input_time
        self._display_remaining_countdown()

    def _display_remaining_countdown(self) -> None:
        remainder = self.remaining
        while True:
            interval = 1
            target = datetime.strptime("00:00:00", TIME_FORMAT)
            if remainder == target:
                self._time_up_display()
                break
            remainder = remainder - timedelta(seconds=interval)
            days = remainder.day
            hours, remaind = divmod(remainder.second, 3600)
            minutes, seconds = divmod(remaind, 60)

            print(
                f"{days:02d}d {hours:02d}:{minutes:02d}:{seconds:02d}",
                end="\r",
                flush=True,
            )
            time.sleep(interval)

    def _time_up_display(self) -> None:
        for _ in range(6):
            print(
                f"{BG_RED}{BOLD}    ⏰ ALARM! TIME'S UP! ⏰    {RESET}",
                end="\r",
                flush=True,
            )
            time.sleep(0.3)
            print(" " * 40, end="\r", flush=True)
            time.sleep(0.3)
        print(f"{RED}{BOLD} Count-Down Finished!! {RESET}")

    def pause_alarm():
        # future to-do
        pass

    def reset_timer():
        # future to-do
        pass


def main() -> NoReturn:
    print("-" * 60)
    print("Welcome to Count-Down Timer App")
    print("-" * 60)
    try:
        while True:
            input_time = get_time_input("Enter time in HH:MM:SS format: ")
            print(f"TIME SET BY USER: {input_time.time()}")
            CountDownManager(input_time)
    except (KeyboardInterrupt, EOFError):
        print("\nThanks you for using the app!")

    raise SystemExit(0)


if __name__ == "__main__":
    main()
