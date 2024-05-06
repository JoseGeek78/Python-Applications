from datetime import datetime
from playsound import playsound
import winsound

alarm_date=input('Enter the date on which you want to set the alarm: ').strip()
alarm_time=''.join(input("Enter the time of alarm to be set in HH:MM,AM/PM format: ").split())
music_or_beep = input("Enter m for a music or b for beep sound: ")
if music_or_beep == 'b':
    dur=int(input("duration in seconds: "))*1000 
    freq = int(input("frequency of the noise: "))
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_period=alarm_time[6:8].upper()

print('setting alarm...')


while True: