class SmartPlug:
    def __init__(self, consumption_rate: int):
        if not (0 <= consumption_rate <= 150):
            raise ValueError("Consumption rate must be between 0 and 150 watts.")
        
        self._switched_on = False
        self._consumption_rate = consumption_rate
    
    def toggle_switch(self):
        self._switched_on = not self._switched_on
    
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"SmartPlug is {state} with a consumption rate of {self._consumption_rate}"
    
    @property
    def consumption_rate(self):
        return self._consumption_rate
    
    @consumption_rate.setter
    def consumption_rate(self, value):
        if not (0 <= value <= 150):
            raise ValueError("Consumption rate must be between 0 and 150 watts.")
        self._consumption_rate = value

def test_smart_plug():
    try:
        plug = SmartPlug(45)
        print(plug)  # Expected: "SmartPlug is off with a consumption rate of 45"

        plug.toggle_switch()
        print(plug)  # Expected: "SmartPlug is on with a consumption rate of 45"
        
        plug.consumption_rate = 75
        print(plug)  # Expected: "SmartPlug is on with a consumption rate of 75"
        
        plug.toggle_switch()
        print(plug)  # Expected: "SmartPlug is off with a consumption rate of 75"
        
        # Test invalid consumption rates
        try:
            plug.consumption_rate = -10  # Should raise ValueError
        except ValueError as e:
            print("Invalid update prevented:", e)

        try:
            plug.consumption_rate = 200  # Should raise ValueError
        except ValueError as e:
            print("Invalid update prevented:", e)

        # Test invalid instantiation
        try:
            SmartPlug(-5)  # Should raise ValueError
        except ValueError as e:
            print("Invalid instantiation prevented:", e)

        try:
            SmartPlug(160)  # Should raise ValueError
        except ValueError as e:
            print("Invalid instantiation prevented:", e)

    except Exception as e:
        print("Test failed:", e)

# Run the test function
test_smart_plug()