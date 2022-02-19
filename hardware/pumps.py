from pump import pump

class Pumps:

  def __init__ (self, pump_list):
    self.pump_list = pump_list

  def toggle_pumps (self, channel):
    other_pump_on = False

    for i in self.pump_list:
      if self.pump_list[i].is_on == 1:
        other_pump_on = True

    if not other_pump_on:
      self.pump_list[pump_num].toggle

  