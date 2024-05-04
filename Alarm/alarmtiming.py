from datetime import datetime
from playsound import playsound
import winsound

alarm_date=input('Enter the date on which you want to set the alarm: ').strip()
alarm_time=''.join(input("Enter the time of alarm to be set in HH:MM,AM/PM format: ").split())
music_or_beep = input("Enter m for a music or b for beep sound: ")