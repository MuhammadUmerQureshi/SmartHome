class SmartPlug:
    def __init__(self, consumption_rate: int):
        if not (0 <= consumption_rate <= 150):
            raise ValueError("Consumption rate must be between 0 and 150 watts.")
        self.consumption_rate = consumption_rate
        self.switched_on = False

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def set_consumption_rate(self, value: int):
        if not (0 <= value <= 150):
            raise ValueError("Consumption rate must be between 0 and 150 watts.")
        self.consumption_rate = value

    def get_consumption_rate(self):
        return self.consumption_rate

    def __str__(self):
        state = "on" if self.switched_on else "off"
        return f"SmartPlug is {state} with a consumption rate of {self.consumption_rate}"



