# Libraries
from lcd_display import lcd
from time import sleep
from colorama import init, Fore, Back, Style

# Variables that I'll use
screen = lcd()
line = 0

# Functions
def lcd_instruct(screen):
    screen.display_string("*------------------*", 1)
    screen.display_string("*INSTRUCTIONS:     *", 2)
    screen.display_string("* 1- Line by line  *", 3)
    screen.display_string("* 2- 4 lin by 4 lin*", 4)

def lcd_end(screen):
    screen.display_string("*------------------*", 1)
    screen.display_string("*    GOOD BYE!!    *", 2)
    screen.display_string("*                  *", 3)
    screen.display_string("*------------------*", 4)

# Code
init()
screen.clear()
try:
    print(Fore.RED+ "INSTRUCTIONS: \n  1- Line by line\n  2- 4 lines by 4 lines" + Style.RESET_ALL)
    lcd_instruct(screen)
    menu = int(input())
    print(Fore.YELLOW + "Insert something to print: " + Style.RESET_ALL)
    screen.clear()
    while 1:
        if menu == 1:
            text = input(f"Line {line+1}: ")
            screen.display_string(str(text), line+1)
            line = (line + 1) % 4
        else:
            text1 = input()
            text2 = input()
            text3 = input()
            text4 = input()
            screen.display_string(text1, 1)
            screen.display_string(text2, 2)
            screen.display_string(text3, 3)
            screen.display_string(text4, 4)
finally:
    print(Style.RESET_ALL)
    lcd_end(screen)
    sleep(1)
    screen.clear()




