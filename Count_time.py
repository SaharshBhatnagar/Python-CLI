import time

def count_time():
    """
    A simple console-based countdown timer.

    This function prompts the user to enter a duration in seconds. It validates
    the input to ensure it is a positive integer. Once a valid duration is
    provided, it starts a countdown, printing the remaining time in an
    HH:MM:SS format to the console every second. After the countdown
    completes, it prints a confirmation message.

    -------------INPUT----------------
    Enter 'TIME' (in seconds):  5

    -------------OUTPUT---------------

    00:00:05
    00:00:04
    00:00:03
    00:00:02
    00:00:01
    00:00:00
    CountDown has been completed⏱️⏱️
    """

    while True:
        try:
            count = int(input("Enter 'TIME' (in seconds):  "))
            if count <= 0:
                raise ValueError
            break
        except ValueError:
            print(f"Timer can't be set for '{count}' value")
    print()


    for timecount in range(count, -1, -1):

        seconds = timecount % 60
        minutes = (timecount // 60) % 60
        hours = timecount // 3600
        print(f"{hours:02}:{minutes:02}:{seconds:02}")

        time.sleep(1)

    print("CountDown has been completed⏱️⏱️")


count_time()