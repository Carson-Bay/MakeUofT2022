from pump import pump
import config import *

class Pumps:

  def __init__ (self, pump_list):
    self.pump_list = pump_list
    self.dict = {
      str(button_pin_1)  : 0
      str(button_pin_2)  : 1
      str(button_pin_3) : 2
      str(button_pin_4) : 3
    }

  def toggle_pumps (self, channel):
    other_pump_on = False

    for i in self.pump_list:
      if self.pump_list[i].is_on == 1:
        other_pump_on = True

    if not other_pump_on:
      self.pump_list[pump_num].toggle

  