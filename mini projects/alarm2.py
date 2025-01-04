import pygame
import time
import datetime

pygame.mixer.init()

def play_alarm_sound():
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()
    
def set_alarm(alarm_hour, alarm_minute, am_pm):   
    if am_pm == "pm" and alarm_hour != 12: 
        alarm_hour+= 12 
    elif am_pm == "am" and alarm_hour == 12:
        alarm_hour = 0
        
    alarm_time = datetime.time(alarm_hour ,alarm_minute)    
    print(f"Alarm set for {alarm_time}")    
          
    while True:    
            current_time = datetime.datetime.now().time()
            if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                print("Alarm ringing...")
                play_alarm_sound()
                while pygame.mixer.music.get_busy(): time.sleep(1)
                break
            time.sleep(30)
if __name__ == "__main__":
    alarm_hour = int(input("Enter alarm hour (1-12):  "))
    alarm_minute =int(input("Enter alarm minute (0-59):  "))
    am_pm = input ("Enter am/pm:  ").strip().lower() 
    set_alarm(alarm_hour, alarm_minute,am_pm)           