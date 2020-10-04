from lcd_display import lcd
from time import sleep

screen = lcd()

screen.display_string("*------------------*", 1)
screen.display_string("|       Jesus      |", 2)
screen.display_string("|  Sos medio puto  |", 3)
screen.display_string("*------------------*", 4)

sleep(2)

screen.display_off()

sleep(2)

screen.display_on()