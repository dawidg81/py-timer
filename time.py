import time

# Function to display the splash text
def splashtext():
    print("Timer 0-1")
    print("help' for commands, 'quit' to quit.)

# Timer Class to handle timer operations
class Timer:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False
        self.paused = False

    def set_hours(self, h):
        self.hours = int(h)
        print(f"Hours set to {self.hours}")

    def set_minutes(self, m):
        self.minutes = int(m)
        print(f"Minutes set to {self.minutes}")

    def set_seconds(self, s):
        self.seconds = int(s)
        print(f"Seconds set to {self.seconds}")

    def start(self):
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            print("You must set the timer first!")
            return
            
        if self.hours > 24 and self.minutes > 59 and self.seconds > 59:
            print("Invalid numbers! Hours can't be more than 24, minutes and seconds can't be more than 59.")
            return
        self.running = True
        self.paused = False
        print(f"Timer started: {self.hours} hours, {self.minutes} minutes, {self.seconds} seconds.")
        print("")  # Add an empty line to ensure timer starts on the second line
        self._countdown()

    def _countdown(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        while total_seconds > 0 and self.running:
            if self.paused:
                break
            mins, secs = divmod(total_seconds, 60)
            hrs, mins = divmod(mins, 60)
            time_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"

            # Overwrite the second line with the updated time
            print(f"\r{time_str}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1

        if total_seconds == 0:
            print("\nTime's up!")

        # Make sure to leave a new line after the countdown to make room for further commands
        if self.running or self.paused:
            print("\nTimer stopped or paused.")

    def pause(self):
        if self.running:
            self.paused = True
            print("Timer paused.")
        else:
            print("Timer is not running.")

    def stop(self):
        self.running = False
        self.paused = False
        print("Timer stopped.")

    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False
        self.paused = False
        print("Timer reset to 0 hours, 0 minutes, 0 seconds.")

# Show splash text
splashtext()

# Initialize timer
timer = Timer()

# Print initial empty line for timer to appear in the second line
print("")  # Add an empty line for the timer to print on the second line

# Main loop
while True:
    user_input = input("[ Timer 1.0 ] >>> ")

    if user_input == "help":
        print("""
        This is the list of available commands:

        help - Shows the current list of available commands.
        quit - Quits the program.
        timer - Enters the timer setting mode.
        splashtext - Shows the greeting splashtext.
        """)

    elif user_input == "quit":
        print("Exiting the program...")
        break

    elif user_input == "timer":
        print("You have entered the timer setting mode. Type 'help' to see available commands in this mode. To exit this mode, type 'timer quit'.")
        
        while True:
            timer_input = input("[ Timer 1.0 / Timer setting mode ] >>> ")

            if timer_input == "help":
                print("""
                This is the list of available commands in the TIMER SETTING mode:

                help - Shows this list.
                h <value> - Sets the hours of the timer.
                m <value> - Sets the minutes of the timer.
                s <value> - Sets the seconds of the timer.
                start - Starts the countdown of the timer.
                pause - Pauses the countdown of the timer.
                stop - Stops and resets the progress of the timer.
                reset - Resets the values of hours, minutes and seconds of the timer to zero.
                """)

            elif timer_input.startswith("h "):
                _, hours = timer_input.split()
                timer.set_hours(hours)

            elif timer_input.startswith("m "):
                _, minutes = timer_input.split()
                timer.set_minutes(minutes)

            elif timer_input.startswith("s "):
                _, seconds = timer_input.split()
                timer.set_seconds(seconds)

            elif timer_input == "start":
                timer.start()

            elif timer_input == "pause":
                timer.pause()

            elif timer_input == "stop":
                timer.stop()

            elif timer_input == "reset":
                timer.reset()

            elif timer_input == "quit":
                print("Exiting timer setting mode...")
                break

            else:
                print("Invalid command. Type 'help' for assistance.")
