from hardware.pump import *
from config import *

class Pumps:

  def __init__ (self, pump_list):
    self.pump_list = pump_list
    self.pump_my_dict = {
      str(button_pin_1): 0,
      str(button_pin_2): 1,
      str(button_pin_3): 2,
      str(button_pin_4): 3,
    }

  def toggle_pumps (self, channel):
    time.sleep(0.001)
    
    other_pump_on = False
    
    pump_index = self.pump_my_dict[str(channel)]
    
    for i in range(len(self.pump_list)):
      if i == pump_index:
        break
      
      if self.pump_list[i].is_on == 1:
        other_pump_on = True

    if not other_pump_on:
      self.pump_list[pump_index].toggle()
