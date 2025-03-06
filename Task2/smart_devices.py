class SmartDevice:
    def __init__(self):
        self.switched_on = False

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def __str__(self):
        state = "on" if self.switched_on else "off"
        return f"{self.__class__.__name__} is {state}"


class SmartTV(SmartDevice):
    def __init__(self, channel=1):
        super().__init__()
        if not (1 <= channel <= 734):
            raise ValueError("Channel must be between 1 and 734.")
        self.channel = channel

    def set_channel(self, channel):
        if not (1 <= channel <= 734):
            raise ValueError("Channel must be between 1 and 734.")
        self.channel = channel

    def get_channel(self):
        return self.channel

    def __str__(self):
        state = "on" if self.switched_on else "off"
        return f"SmartTV is {state} and channel is {self.channel}"


class SmartWashingMachine(SmartDevice):
    VALID_WASH_MODES = ["Daily wash", "Quick wash", "Eco"]
    
    def __init__(self, wash_mode="Daily wash"):
        super().__init__()
        if wash_mode not in self.VALID_WASH_MODES:
            raise ValueError(f"Wash mode must be one of {self.VALID_WASH_MODES}.")
        self.wash_mode = wash_mode

    def set_wash_mode(self, wash_mode):
        if wash_mode not in self.VALID_WASH_MODES:
            raise ValueError(f"Wash mode must be one of {self.VALID_WASH_MODES}.")
        self.wash_mode = wash_mode

    def get_wash_mode(self):
        return self.wash_mode

    def __str__(self):
        state = "on" if self.switched_on else "off"
        return f"SmartWashingMachine is {state} with wash mode {self.wash_mode}"



