import pygame
import datetime
import time
import sys

a = int(input("Enter hours: "))
b = int(input("Enter miniutes: "))
c = int(input("Enter seconds: "))

music = "music/jingle-bells-alarm-clock-version-129333.mp3"

t = datetime.time(a,b,c)
print(f"Alarm set for {t}")
ti = time.localtime()
hr = ti.tm_hour
min = ti.tm_min
sec = ti.tm_sec

while(hr!=a or min!= b or sec!=c):
    ti = time.localtime()
    hr = ti.tm_hour
    min = ti.tm_min
    sec = ti.tm_sec
    sys.stdout.write(f"\r{hr:02}:{min:02}:{sec:02}")
    sys.stdout.flush()      #This gives direct control over printing — you can:
                                    # Write text without a newline
                                    # Force immediate display (no buffering)
                                    # Update text on the same line
    time.sleep(1)
print("\nTimes upp!! ⏰")
pygame.mixer.init()
pygame.mixer.music.load(music)
m='s'
while(m != ''):
    pygame.mixer.music.play()
    m = input("Press Enter to stop the alarm: ")