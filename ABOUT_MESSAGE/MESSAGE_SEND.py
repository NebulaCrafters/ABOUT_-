import pyautogui
import time

# Input parameters
MESSAGE = str(input("ENTER WHAT YOU WANT TO SEND: "))
TIMES = int(input("HOW MANY TIMES YOU WANT TO SEND: "))
REQUIRED = int(input("HOW MANY SECONDS TO SWITCH WINDOWS: "))

# PyAutoGUI settings
pyautogui.PAUSE = 0.05  # Minimize the pause between actions
pyautogui.FAILSAFE = False  # Disable fail-safe

# Function to send the message multiple times
def send_message(message, repetitions, delay_between_messages):
    for _ in range(repetitions):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(delay_between_messages)

# Main program
if __name__ == "__main__":
    print(f"You have {REQUIRED} seconds to switch to the Messenger window...")

    time.sleep(REQUIRED)

    send_message(MESSAGE, TIMES, 0)

    print("Messages sent successfully!")
