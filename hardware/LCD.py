'''3. LCD.py
    1. LCD_init(): initializes lcd gpio pins
    2. should we abstract the LCD library functions?
  '''

from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

def init_lcd():
  # Modify this if you have a different sized character LCD
  lcd_columns = 16
  lcd_rows = 2

  # compatible with all versions of RPI as of Jan. 2019
  # v1 - v3B+
  lcd_rs = digitalio.DigitalInOut(board.D22)
  lcd_en = digitalio.DigitalInOut(board.D17)
  lcd_d4 = digitalio.DigitalInOut(board.D25)
  lcd_d5 = digitalio.DigitalInOut(board.D24)
  lcd_d6 = digitalio.DigitalInOut(board.D23)
  lcd_d7 = digitalio.DigitalInOut(board.D18)


  # Initialise the lcd class
  lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

  # wipe LCD screen before we start
  lcd.clear()

  return lcd

def update_all(lcd, bottle_1, bottle_2, bottle_3, bottle_4):
    lcd.clear()
    
    lcd_line_1 = "B1:%{} B2:%{}\n".format(str(bottle_1).ljust(3), str(bottle_1).ljust(3))

    lcd_line_2 = "B3:%{} B4:%{}".format(str(bottle_3).ljust(3), str(bottle_4).ljust(3))

    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + lcd_line_2

if __name__ == "__main__":
  update_all(19, 28, 37, 46)
