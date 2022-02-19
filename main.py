from hardware import pump
'''
4. main.py
    
    initialize everything
    
    create 4 pump instances
    
    while (1)
    
    update_lcd_all_pumps(array_of_pumps);
    
    send_notifications();
    
    update_webpage();

'''
import time
import RPi.GPIO as GPIO
from hardware.pump import * 
import hardware.LCD as LCD

# Config Variables
button_pin_1 = 25
button_pin_2 = 27
button_pin_3 = 28
button_pin_4 = 29

pump_pin_1 = 21
pump_pin_2 = 22
pump_pin_3 = 23
pump_pin_4 = 24

# Button Setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup pumps
pump1 = Pump(pump_pin_1)
pump2 = Pump(pump_pin_2)
pump3 = Pump(pump_pin_3)
pump4 = Pump(pump_pin_4)


# Callbacks
'''ON'''
GPIO.add_event_detect(button_pin_1, GPIO.RISING, callback=pump1.turn_on, bouncetime=300)
GPIO.add_event_detect(button_pin_2, GPIO.RISING, callback=pump2.turn_on, bouncetime=300)  
GPIO.add_event_detect(button_pin_3, GPIO.RISING, callback=pump3.turn_on, bouncetime=300)  
GPIO.add_event_detect(button_pin_4, GPIO.RISING, callback=pump4.turn_on, bouncetime=300)    
'''OFF'''
GPIO.add_event_detect(button_pin_1, GPIO.FALLING, callback=pump1.turn_off, bouncetime=300)
GPIO.add_event_detect(button_pin_2, GPIO.FALLING, callback=pump2.turn_off, bouncetime=300)  
GPIO.add_event_detect(button_pin_3, GPIO.FALLING, callback=pump3.turn_off, bouncetime=300)  
GPIO.add_event_detect(button_pin_4, GPIO.FALLING, callback=pump4.turn_off, bouncetime=300)    



if __name__ == "__main__":
  try:  
    while True:
      LCD.update_all(pump1.get_liquid_level(), pump2.get_liquid_level(), pump3.get_liquid_level(), pump4.get_liquid_level())
      time.sleep(2)
  except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit 

  GPIO.cleanup()           # clean up GPIO on normal exit  
