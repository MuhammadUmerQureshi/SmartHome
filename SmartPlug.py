class SmartPlug:  
    def __init__(self, consumption_rate):
        
        if not isinstance(consumption_rate, int) or consumption_rate < 0 or consumption_rate > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150 watts")
        
        self._consumption_rate = consumption_rate
        self._switched_on = False
    
    def toggle_switch(self):
        self._switched_on = not self._switched_on
    
    @property
    def switched_on(self):
        return self._switched_on
    
    
    @property
    def consumption_rate(self):
        return self._consumption_rate
    @consumption_rate.setter
    def consumption_rate(self, value):

        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150 watts")
        self._consumption_rate = value
   
    def __str__(self):
        status = "on" if self._switched_on else "off"
        return f"SmartPlug is {status} with a consumption rate of {self._consumption_rate}"


def test_smart_plug():
  
 
    print("Testing SmartPlug class...")
    
    # Test initialization and default state
    plug = SmartPlug(45)
    print(plug)  # Should be off with consumption rate of 45
    
    # Test toggling on
    plug.toggle_switch()
    print(plug)  # Should be on with consumption rate of 45
    
    # Test updating consumption rate
    plug.consumption_rate = 75
    print(plug)  # Should be on with consumption rate of 75
    
    # Test toggling off
    plug.toggle_switch()
    print(plug)  # Should be off with consumption rate of 75
    
    # Test invalid consumption rate updates
    try:
        plug.consumption_rate = -10
        print("Harder constrain failed: Accepted a negative consumption rate")#Should not be printed for successful harder constraints
    except ValueError:
        print("Success: Rejected negative consumption rate")
    
    try:
        plug.consumption_rate = 200
        print("Failed: Accepted consumption rate > 150")
    except ValueError:
        print("Success: Rejected consumption rate > 150")
    
    # Current state should be unchanged
    print(plug)  # Should still be off with consumption rate of 75
    
    # Test invalid initialization
    try:
        invalid_plug = SmartPlug(-5)
        print("Failed: Created SmartPlug with negative consumption rate")#Should not be printed for successful harder constraints
    except ValueError:
        print("Success: Rejected SmartPlug with negative consumption rate")
    
    try:
        invalid_plug = SmartPlug(160)
        print("Failed: Created SmartPlug with consumption rate > 150")#Should not be printed for successful harder constraints
    except ValueError:
        print("Success: Rejected SmartPlug with consumption rate > 150")
    
    print("SmartPlug testing complete")


if __name__ == "__main__":
    test_smart_plug()