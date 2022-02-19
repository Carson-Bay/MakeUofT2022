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