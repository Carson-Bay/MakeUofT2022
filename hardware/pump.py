import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# time in milliseconds to liquid level via multiplication
MILLIS_TO_LIQUID = 15000000
# max millis to liquid; assuming after 30 seconds it is done pumping
MAX_LIQUID = MILLIS_TO_LIQUID*30000

'''
2. pump.py
    1. pump_class
        
        Members:
        
        1. motor_gpio: which gpio we are using
        2. total_water_usage: total water each pump has pumped... calculated by adding previous amount plus (time_off - time_on) * TIME_WATER_CONV
        3. time_on: time pump turned on
        4. time_off: time pump turned off
        5. liquid_level: current level of the liquid... needs to be updated when the user presses a button to signify refill
        
        Functions:
        
        1. pump_gpio_init(): initializes a pump
        2. getter functions
        3. setter functions
        4. liquid_level_reset()

'''

def get_time_millis():
  return round(time.time() * 1000)


class Pump:

  def __init__(self,pump_gpio,button_gpio):
    # Setup GPIO
    self.pump_gpio = pump_gpio
    self.button_gpio = button_gpio
    # All time values in milliseconds
    self.last_on = get_time_millis()
    self.last_off = get_time_millis()
    self.is_on = False
    self.time_on = 0
    # liquid level in percentages
    self.liquid_level = 100

  def toggle(self, channel):
    time.sleep(0.01)
    if GPIO.input(self.button_gpio) == 1:
      print("Rising sdf")
      # only change last_on if the pump wasn't already on
      if not self.is_on:
        self.last_on = time.time()
        self.is_on = True
        # set GPIO stuff
        GPIO.output(self.pump_gpio,GPIO.HIGH)
      else:
        print("Pump GPIO",self.pump_gpio, "turn_on called with pump already on.")

    else:
      print("Falling")
      # only change last_off if the pump wasn't already on
      if self.is_on:
        self.last_off = time.time()
        self.is_on = False
        # set GPIO stuff
        GPIO.output(self.pump_gpio,GPIO.LOW)
        # when the pump is turned off, update the time_on
        self.time_on += (self.last_off - self.last_on)
      else:
        print("Pump GPIO",self.pump_gpio, "turn_off called with pump already off.")
  
  def get_time_on(self):
    if self.is_on:
      timeon = self.time_on + (get_time_millis() - self.last_on)
    else:
      timeon = self.time_on

    return timeon

  # return the liquid level as a percentage
  def get_liquid_level(self):
    return (self.get_time_on()*MILLIS_TO_LIQUID)/MAX_LIQUID * 100

  # return liquid usage in millilitres
  def get_liquid_usage(self):
    return self.get_time_on*MILLIS_TO_LIQUID

    
