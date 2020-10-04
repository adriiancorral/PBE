# Libraries
from lcd_display import lcd
from time import strftime
from subprocess import check_output

# Variables
screen = lcd()
counter = 0

# Code
try:
    screen.clear()
    while 1:
        #Date & Time
        date = strftime("%x")   # to obtain the date as a string
        time = strftime("%X")   # to obtain the time as a string
        screen.display_string("Date & Time:", 1)
        screen.display_string(f"  {date} {time}", 2)
        #IP
        screen.display_string("IP Adress:", 3)
        ip_adress = check_output(['hostname', '-I']).decode("utf-8").strip()
        screen.display_string(f"  {ip_adress}", 4)
        #Counter to end the script
        counter = counter + 1
        if counter == 200:
            break
finally:
    screen.clear()