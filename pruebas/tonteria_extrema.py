from lcd_display import lcd
from time import sleep

a = lcd()

a.clear()

while 1:
    a.display_string("     ------      ***", 1)
    a.display_string("      ----        **", 2)
    a.display_string("  @                 ", 3)
    a.display_string("--------------------", 4)
    
    a.display_string("  @                +", 3)
    a.display_string("  @               + ", 3)
    a.display_string("  @              +  ", 3)
    a.display_string("  @             +   ", 3)
    a.display_string("  @            +    ", 3)
    a.display_string("  @           +     ", 3)
    a.display_string("  @          +      ", 3)
    a.display_string("  @         +       ", 3)
    a.display_string("  @        +        ", 3)
    a.display_string("  @       +         ", 3)
    a.display_string("  @      +          ", 3)
    a.display_string("  @     +           ", 3)
    a.display_string("  @    +            ", 3)
    a.display_string("  @   +             ", 3)
    a.display_string("  @  +              ", 3)
    a.display_string("  @   ----        **", 2)
    a.display_string("    +               ", 3)
    a.display_string("   +                ", 3)
    a.display_string("  +                 ", 3)
    a.display_string(" +                  ", 3)
    a.display_string("      ----        **", 2)
    a.display_string("+ @                 ", 3)
    







