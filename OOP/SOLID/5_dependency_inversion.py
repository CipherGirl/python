# Depends upon Abstraction/Interface(High-Level) rather than concrete classes(Low-Level)
# High-level modules should not depend on low-level modules

"""
we need to ensure that high-level modules do not depend on low level modules, but instead depend on abstractions. 
The abstraction should not depend on details, instead the details should depend on abstractions
"""

"""Bad Example

class LightBulb:
    def turn_on(self):
        print("LightBulb: Turned On")

    def turn_off(self):
        print("LightBulb: Turned Off") 


# PowerSwitch is high-level — it controls “something switchable”.
# But it directly depends on LightBulb, a low-level concrete class.
# So if we want to switch on a Fan or Heater, you must modify PowerSwitch — violating OCP and DIP.

class PowerSwitch:
    def __init__(self, lb: LightBulb):
        self.light_bulb = lb
        self.on = False

    def press(self):
        if(self.on):
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True

hue_bulb = LightBulb()

switch_for_huebulb = PowerSwitch(hue_bulb)

switch_for_huebulb.press()
switch_for_huebulb.press()
"""

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Turned On")

    def turn_off(self):
        print("LightBulb: Turned Off") 

class Heater(Switchable):
    def turn_on(self):
        print("Heater: Turned On")

    def turn_off(self):
        print("Heater: Turned Off") 

class PowerSwitch:
    # PowerSwitch is Depending on the implmentation of the LightBulb in above example
    # It should depend on the abtract class Switchable not on the LightBulb
    # LightBulb (and any other device like Fan or Heater) can implement Switchable.
    # This PowerSwitch is dependant on the abstraction of the Switable device, doesn't matter how they implment the methods
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if(self.on):
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

hue_bulb = LightBulb()

switch_for_huebulb = PowerSwitch(hue_bulb)

switch_for_huebulb.press()
switch_for_huebulb.press()

heater = Heater()

switch_for_heater = PowerSwitch(heater)

switch_for_heater.press()
switch_for_heater.press()