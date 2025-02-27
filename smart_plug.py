class SmartPlug:
    """
    A class representing a smart plug that can be switched on/off and has a power consumption rate.
    """
    
    def __init__(self, consumption_rate):
        """
        Initialize a SmartPlug with a specified consumption rate.
        
        Args:
            consumption_rate (int): The power consumption rate in watts (0-150).
        
        Raises:
            ValueError: If consumption_rate is not within the allowed range.
        """
        if not isinstance(consumption_rate, int) or consumption_rate < 0 or consumption_rate > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150 watts")
        
        self._consumption_rate = consumption_rate
        self._switched_on = False
    
    def toggle_switch(self):
        """Toggle the switch state between on and off."""
        self._switched_on = not self._switched_on
    
    @property
    def switched_on(self):
        """Get the current switch state."""
        return self._switched_on
    
    @property
    def consumption_rate(self):
        """Get the current consumption rate."""
        return self._consumption_rate
    
    @consumption_rate.setter
    def consumption_rate(self, value):
        """
        Set the consumption rate.
        
        Args:
            value (int): The new consumption rate (0-150).
            
        Raises:
            ValueError: If value is not within the allowed range.
        """
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150 watts")
        self._consumption_rate = value
    
    def __str__(self):
        """Return a string representation of the SmartPlug."""
        status = "on" if self._switched_on else "off"
        return f"SmartPlug is {status} with a consumption rate of {self._consumption_rate}"


def test_smart_plug():
    """
    Test function for the SmartPlug class.
    Tests initialization, toggling, and updating consumption rate.
    Also tests handling of invalid values.
    """
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
        print("Failed: Accepted negative consumption rate")
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
        print("Failed: Created SmartPlug with negative consumption rate")
    except ValueError:
        print("Success: Rejected SmartPlug with negative consumption rate")
    
    try:
        invalid_plug = SmartPlug(160)
        print("Failed: Created SmartPlug with consumption rate > 150")
    except ValueError:
        print("Success: Rejected SmartPlug with consumption rate > 150")
    
    print("SmartPlug testing complete")


if __name__ == "__main__":
    test_smart_plug()