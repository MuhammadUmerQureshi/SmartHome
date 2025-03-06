"""
  Student Number: 2248793
  Unique Last Two Numbers: 9,3
  Classes to be implemented as per the student number: SmartAirFryer and SmartTV
    
"""
class SmartDevice:

    
    def __init__(self, name):
        self._name = name
        self._switched_on = False
    
    def toggle_switch(self):
        self._switched_on = not self._switched_on
    
    @property
    def switched_on(self):
        return self._switched_on
    
    @property
    def name(self):
        return self._name
class SmartTV(SmartDevice):
   
    def __init__(self):
        super().__init__("SmartTV")
        self._channel = 1  # Default value
    
    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, value):
        if not isinstance(value, int) or value < 1 or value > 734:
            raise ValueError("Channel must be an integer between 1 and 734")
        self._channel = value
    
    def __str__(self):
        status = "on" if self._switched_on else "off"
        return f"SmartTV is {status} with a channel of {self._channel}"
class SmartAirFryer(SmartDevice):
  
    
    def __init__(self):
        super().__init__("SmartAirFryer")
        self._cook_mode = "Healthy"  # Default value
    
    @property
    def cook_mode(self):
        return self._cook_mode
    
    @cook_mode.setter
    def cook_mode(self, value):
        
        allowed_modes = ["Healthy", "Defrost", "Crispy"]
        if value not in allowed_modes:
            raise ValueError("Cook mode must be one of: Healthy, Defrost, or Crispy")
        self._cook_mode = value
    
    def __str__(self):
        status = "on" if self._switched_on else "off"
        return f"SmartAirFryer is {status} with a cook_mode of {self._cook_mode}"

def test_custom_device():
    print("Testing Custom Device Classes")
    
    TV = SmartTV()
    AirFryer = SmartAirFryer()
    
    
    print(TV)  # Should be off with channel 1
    print(AirFryer)  # Should be off with cook_mode "Healthy"
    
    
    TV.toggle_switch()
    AirFryer.toggle_switch()
    print(TV)  # Should be on with channel 1
    print(AirFryer)  # Should be on with cook_mode "Healthy"
    
    
    TV.channel = 100
    AirFryer.cook_mode = "Crispy"
    print(TV)  # Should be on with channel 100
    print(AirFryer)  # Should be on with cook_mode "Crispy"
    

    try:
        TV.channel = 0
        print("Failed: Accepted channel < 1")
    except ValueError:
        print("Success: Rejected channel < 1")
    
    try:
        TV.channel = 735
        print("Failed: Accepted channel > 734") #Should not be printed for successful harder constraints
    except ValueError:
        print("Success: Rejected channel > 734")
    
    try:
        AirFryer.cook_mode = "Bake"
        print("Failed: Accepted invalid cook mode") #Should not be printed for successful harder constraints
    except ValueError:
        print("Success: Rejected invalid cook mode")
    
    print(TV)  # Should still be on with channel 100
    print(AirFryer)  # Should still be on with cook_mode "Crispy"
    
    print("Custom device testing complete")


if __name__ == "__main__":
    test_custom_device()