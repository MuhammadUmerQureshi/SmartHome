class SmartDevice:
    def __init__(self, option_value, option_range, default_value):
        if option_value not in option_range:
            raise ValueError(f"Option value must be within {option_range}.")
        self._switched_on = False
        self._option_value = option_value
        self._option_range = option_range
        self._default_value = default_value
    
    def toggle_switch(self):
        self._switched_on = not self._switched_on
    
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"{self.__class__.__name__} is {state} with {self._option_value}"
    
    @property
    def option_value(self):
        return self._option_value
    
    @option_value.setter
    def option_value(self, value):
        if value not in self._option_range:
            raise ValueError(f"Option value must be within {self._option_range}.")
        self._option_value = value

class SmartLight(SmartDevice):
    def __init__(self, brightness=50):
        super().__init__(brightness, range(1, 101), 50)

class SmartFridge(SmartDevice):
    def __init__(self, temperature=3):
        super().__init__(temperature, {1, 3, 5}, 3)

class SmartHeater(SmartDevice):
    def __init__(self, setting=2):
        super().__init__(setting, range(0, 6), 2)

class SmartTV(SmartDevice):
    def __init__(self, channel=1):
        super().__init__(channel, range(1, 735), 1)

class SmartSpeaker(SmartDevice):
    def __init__(self, streaming="Amazon"):
        super().__init__(streaming, {"Amazon", "Apple", "Spotify"}, "Amazon")

class SmartDoorBell(SmartDevice):
    def __init__(self, sleep_mode=False):
        super().__init__(sleep_mode, {True, False}, False)

class SmartOven(SmartDevice):
    def __init__(self, temperature=150):
        super().__init__(temperature, range(0, 261), 150)

class SmartWashingMachine(SmartDevice):
    def __init__(self, wash_mode="Daily wash"):
        super().__init__(wash_mode, {"Daily wash", "Quick wash", "Eco"}, "Daily wash")

class SmartDoor(SmartDevice):
    def __init__(self, locked=True):
        super().__init__(locked, {True, False}, True)

class SmartAirFryer(SmartDevice):
    def __init__(self, cook_mode="Healthy"):
        super().__init__(cook_mode, {"Healthy", "Defrost", "Crispy"}, "Healthy")

def test_custom_devices():
    devices = [SmartLight(), SmartFridge(), SmartHeater(), SmartTV(), SmartSpeaker(),
               SmartDoorBell(), SmartOven(), SmartWashingMachine(), SmartDoor(), SmartAirFryer()]
    
    for device in devices:
        print(device)  # Print initial state
        device.toggle_switch()
        print(device)  # Print after toggle
    
    try:
        devices[0].option_value = 120  # Invalid for SmartLight
    except ValueError as e:
        print("Invalid update prevented:", e)

def test_invalid_initialization():
    try:
        SmartLight(150)  # Should raise ValueError
    except ValueError as e:
        print("Invalid instantiation prevented:", e)

# Run the test functions
test_custom_devices()
test_invalid_initialization()
