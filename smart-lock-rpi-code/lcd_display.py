
from rpi_lcd import LCD
import time
lcd = LCD()

def display_msg(msg1,msg2):

        lcd.clear()
        lcd.text(msg1,1)
        lcd.text(msg2,2)
        time.sleep(0.5)
