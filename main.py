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
from hardware.LCD import *
from hardware.pumps import *
from multiprocessing import Queue, Process
from config import *

# Button Setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(pump_pin_1, GPIO.OUT)
GPIO.setup(pump_pin_2, GPIO.OUT)
GPIO.setup(pump_pin_3, GPIO.OUT)
GPIO.setup(pump_pin_4, GPIO.OUT)

GPIO.output(pump_pin_1, GPIO.HIGH)
GPIO.output(pump_pin_2, GPIO.HIGH)
GPIO.output(pump_pin_3, GPIO.HIGH)
GPIO.output(pump_pin_4, GPIO.HIGH)

# Setup pumps
pump1 = Pump(pump_pin_1, button_pin_1)
pump2 = Pump(pump_pin_2, button_pin_2)
pump3 = Pump(pump_pin_3, button_pin_3)
pump4 = Pump(pump_pin_4, button_pin_4)

pumps = Pumps([pump1, pump2, pump3, pump4])


# Callbacks
GPIO.add_event_detect(button_pin_1, GPIO.BOTH, callback=pumps.toggle_pumps, bouncetime=300)
GPIO.add_event_detect(button_pin_2, GPIO.BOTH, callback=pumps.toggle_pumps, bouncetime=300)  
GPIO.add_event_detect(button_pin_3, GPIO.BOTH, callback=pumps.toggle_pumps, bouncetime=300)  
GPIO.add_event_detect(button_pin_4, GPIO.BOTH, callback=pumps.toggle_pumps, bouncetime=300)        

def main(liquid_levels=Queue(),to_reset=Queue(),drink_requests=Queue()):
  resets = []
  try:  
    lcd = init_lcd()
    while True:
      update_all(lcd, pump1.get_liquid_level(), pump2.get_liquid_level(), pump3.get_liquid_level(), pump4.get_liquid_level())
      pumps.update()

      # only add a liquid level to the queue if it has deteriorated less than 2
      if liquid_levels.qsize() < 2:
        l_levels = [pump1.get_liquid_level(), pump2.get_liquid_level(), pump3.get_liquid_level(), pump4.get_liquid_level()]
        liquid_levels.put(l_levels)
      
      if not to_reset.empty():
        resets = to_reset.get()
        for i in resets:
          print("MUST RESET",i)
      time.sleep(0.5)
  except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit 

  GPIO.cleanup()           # clean up GPIO on normal exit  

if __name__ == "__main__":
  main()
