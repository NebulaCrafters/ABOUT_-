from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    try:
        datetime.strptime(alarm_time, '%I:%M:%S %p')
        return True
    except ValueError:
        return False

def set_alarm():
    while True:
        alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")
        if validate_time(alarm_time):
            break
        else:
            print("Invalid time format. Please enter the time in HH:MM:SS AM/PM format.")

    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()

    print(f"Alarm set for {alarm_hour}:{alarm_minute}:{alarm_seconds} {alarm_period}.")
    
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        
        if (alarm_period == current_period and
            alarm_hour == current_hour and
            alarm_minute == current_minute and
            alarm_seconds == current_seconds):
            print("Wake Up!")
            playsound('audio.mp3')
            break

if __name__ == "__main__":
    set_alarm()
