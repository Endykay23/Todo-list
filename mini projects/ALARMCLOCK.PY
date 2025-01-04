import pygame
import time
import datetime

# Initialize pygame mixer
pygame.mixer.init()

def play_alarm_sound():
    # Load and play the sound
    pygame.mixer.music.load('alarm.wav')  # Make sure 'alarm.wav' is in the same directory
    pygame.mixer.music.play()

def set_alarm(alarm_hour, alarm_minute, am_pm):
    # Convert 12-hour format to 24-hour format
    if am_pm == 'pm' and alarm_hour != 12:
        alarm_hour += 12
    elif am_pm == 'am' and alarm_hour == 12:
        alarm_hour = 0

    # Create a datetime object for the alarm
    alarm_time = datetime.time(alarm_hour, alarm_minute)
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("Alarm ringing...")
            play_alarm_sound()
            # Wait for the sound to finish
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    # Input from user
    alarm_hour = int(input("Enter alarm hour (1-12): "))
    alarm_minute = int(input("Enter alarm minute (0-59): "))
    am_pm = input("Enter am/pm: ").strip().lower()
    set_alarm(alarm_hour, alarm_minute, am_pm)
