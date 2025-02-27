class SmartDevice:
    """
    Base class for all smart devices.
    Contains common attributes and methods for all smart devices.
    """
    
    def __init__(self, name):
        """
        Initialize a SmartDevice with a given name.
        
        Args:
            name (str): The name/type of the smart device.
        """
        self._name = name
        self._switched_on = False
    
    def toggle_switch(self):
        """Toggle the switch state between on and off."""
        self._switched_on = not self._switched_on
    
    @property
    def switched_on(self):
        """Get the current switch state."""
        return self._switched_on
    
    @property
    def name(self):
        """Get the device name."""
        return self._name


class SmartLight(SmartDevice):
    """
    SmartLight device with brightness control.
    """
    
    def __init__(self):
        """Initialize a SmartLight with default brightness of 50%."""
        super().__init__("SmartLight")
        self._brightness = 50  # Default value
    
    @property
    def brightness(self):
        """Get the current brightness level."""
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        """
        Set the brightness level.
        
        Args:
            value (int): Brightness percentage (1-100).
            
        Raises:
            ValueError: If value is not within the allowed range.
        """
        if not isinstance(value, int) or value < 1 or value > 100:
            raise ValueError("Brightness must be an integer between 1 and 100")
        self._brightness = value
    
    def __str__(self):
        """Return a string representation of the SmartLight."""
        status = "on" if self._switched_on else "off"
        return f"SmartLight is {status} with a brightness of {self._brightness}"


class SmartFridge(SmartDevice):
    """
    SmartFridge device with temperature control.
    """
    
    def __init__(self):
        """Initialize a SmartFridge with default temperature of 3°C."""
        super().__init__("SmartFridge")
        self._temperature = 3  # Default value
    
    @property
    def temperature(self):
        """Get the current temperature setting."""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        """
        Set the temperature.
        
        Args:
            value (int): Temperature in degrees Celsius (1, 3, or 5).
            
        Raises:
            ValueError: If value is not within the allowed values.
        """
        if value not in [1, 3, 5]:
            raise ValueError("Temperature must be either 1, 3, or 5 degrees Celsius")
        self._temperature = value
    
    def __str__(self):
        """Return a string representation of the SmartFridge."""
        status = "on" if self._switched_on else "off"
        return f"SmartFridge is {status} with a temperature of {self._temperature}"


class SmartHeater(SmartDevice):
    """
    SmartHeater device with heat setting control.
    """
    
    def __init__(self):
        """Initialize a SmartHeater with default setting of 2."""
        super().__init__("SmartHeater")
        self._setting = 2  # Default value
    
    @property
    def setting(self):
        """Get the current heat setting."""
        return self._setting
    
    @setting.setter
    def setting(self, value):
        """
        Set the heat setting.
        
        Args:
            value (int): Heat setting (0-5).
            
        Raises:
            ValueError: If value is not within the allowed range.
        """
        if not isinstance(value, int) or value < 0 or value > 5:
            raise ValueError("Setting must be an integer between 0 and 5")
        self._setting = value
    
    def __str__(self):
        """Return a string representation of the SmartHeater."""
        status = "on" if self._switched_on else "off"
        return f"SmartHeater is {status} with a setting of {self._setting}"


class SmartTV(SmartDevice):
    """
    SmartTV device with channel control.
    """
    
    def __init__(self):
        """Initialize a SmartTV with default channel of 1."""
        super().__init__("SmartTV")
        self._channel = 1  # Default value
    
    @property
    def channel(self):
        """Get the current channel."""
        return self._channel
    
    @channel.setter
    def channel(self, value):
        """
        Set the channel.
        
        Args:
            value (int): Channel number (1-734).
            
        Raises:
            ValueError: If value is not within the allowed range.
        """
        if not isinstance(value, int) or value < 1 or value > 734:
            raise ValueError("Channel must be an integer between 1 and 734")
        self._channel = value
    
    def __str__(self):
        """Return a string representation of the SmartTV."""
        status = "on" if self._switched_on else "off"
        return f"SmartTV is {status} with a channel of {self._channel}"


class SmartSpeaker(SmartDevice):
    """
    SmartSpeaker device with streaming service control.
    """
    
    def __init__(self):
        """Initialize a SmartSpeaker with default streaming service of Amazon."""
        super().__init__("SmartSpeaker")
        self._streaming = "Amazon"  # Default value
    
    @property
    def streaming(self):
        """Get the current streaming service."""
        return self._streaming
    
    @streaming.setter
    def streaming(self, value):
        """
        Set the streaming service.
        
        Args:
            value (str): Streaming service (Amazon, Apple, or Spotify).
            
        Raises:
            ValueError: If value is not one of the allowed services.
        """
        allowed_services = ["Amazon", "Apple", "Spotify"]
        if value not in allowed_services:
            raise ValueError("Streaming service must be one of: Amazon, Apple, or Spotify")
        self._streaming = value
    
    def __str__(self):
        """Return a string representation of the SmartSpeaker."""
        status = "on" if self._switched_on else "off"
        return f"SmartSpeaker is {status} with a streaming of {self._streaming}"


class SmartDoorBell(SmartDevice):
    """
    SmartDoorBell device with sleep mode control.
    """
    
    def __init__(self):
        """Initialize a SmartDoorBell with default sleep_mode of False."""
        super().__init__("SmartDoorBell")
        self._sleep_mode = False  # Default value
    
    @property
    def sleep_mode(self):
        """Get the current sleep mode state."""
        return self._sleep_mode
    
    @sleep_mode.setter
    def sleep_mode(self, value):
        """
        Set the sleep mode.
        
        Args:
            value (bool): Sleep mode state.
            
        Raises:
            ValueError: If value is not a boolean.
        """
        if not isinstance(value, bool):
            raise ValueError("Sleep mode must be a boolean value")
        self._sleep_mode = value
    
    def __str__(self):
        """Return a string representation of the SmartDoorBell."""
        status = "on" if self._switched_on else "off"
        sleep = "enabled" if self._sleep_mode else "disabled"
        return f"SmartDoorBell is {status} with a sleep_mode of {sleep}"


class SmartOven(SmartDevice):
    """
    SmartOven device with temperature control.
    """
    
    def __init__(self):
        """Initialize a SmartOven with default temperature of 150°C."""
        super().__init__("SmartOven")
        self._temperature = 150  # Default value
    
    @property
    def temperature(self):
        """Get the current temperature setting."""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        """
        Set the temperature.
        
        Args:
            value (int): Temperature in degrees Celsius (0-260).
            
        Raises:
            ValueError: If value is not within the allowed range.
        """
        if not isinstance(value, int) or value < 0 or value > 260:
            raise ValueError("Temperature must be an integer between 0 and 260 degrees Celsius")
        self._temperature = value
    
    def __str__(self):
        """Return a string representation of the SmartOven."""
        status = "on" if self._switched_on else "off"
        return f"SmartOven is {status} with a temperature of {self._temperature}"


class SmartWashingMachine(SmartDevice):
    """
    SmartWashingMachine device with wash mode control.
    """
    
    def __init__(self):
        """Initialize a SmartWashingMachine with default wash_mode of 'Daily wash'."""
        super().__init__("SmartWashingMachine")
        self._wash_mode = "Daily wash"  # Default value
    
    @property
    def wash_mode(self):
        """Get the current wash mode."""
        return self._wash_mode
    
    @wash_mode.setter
    def wash_mode(self, value):
        """
        Set the wash mode.
        
        Args:
            value (str): Wash mode ("Daily wash", "Quick wash", or "Eco").
            
        Raises:
            ValueError: If value is not one of the allowed modes.
        """
        allowed_modes = ["Daily wash", "Quick wash", "Eco"]
        if value not in allowed_modes:
            raise ValueError("Wash mode must be one of: Daily wash, Quick wash, or Eco")
        self._wash_mode = value
    
    def __str__(self):
        """Return a string representation of the SmartWashingMachine."""
        status = "on" if self._switched_on else "off"
        return f"SmartWashingMachine is {status} with a wash_mode of {self._wash_mode}"


class SmartDoor(SmartDevice):
    """
    SmartDoor device with lock control.
    """
    
    def __init__(self):
        """Initialize a SmartDoor with default locked state of True."""
        super().__init__("SmartDoor")
        self._locked = True  # Default value
    
    @property
    def locked(self):
        """Get the current lock state."""
        return self._locked
    
    @locked.setter
    def locked(self, value):
        """
        Set the lock state.
        
        Args:
            value (bool): Lock state.
            
        Raises:
            ValueError: If value is not a boolean.
        """
        if not isinstance(value, bool):
            raise ValueError("Locked state must be a boolean value")
        self._locked = value
    
    def __str__(self):
        """Return a string representation of the SmartDoor."""
        status = "on" if self._switched_on else "off"
        lock_status = "locked" if self._locked else "unlocked"
        return f"SmartDoor is {status} with a locked state of {lock_status}"


class SmartAirFryer(SmartDevice):
    """
    SmartAirFryer device with cook mode control.
    """
    
    def __init__(self):
        """Initialize a SmartAirFryer with default cook_mode of 'Healthy'."""
        super().__init__("SmartAirFryer")
        self._cook_mode = "Healthy"  # Default value
    
    @property
    def cook_mode(self):
        """Get the current cook mode."""
        return self._cook_mode
    
    @cook_mode.setter
    def cook_mode(self, value):
        """
        Set the cook mode.
        
        Args:
            value (str): Cook mode ("Healthy", "Defrost", or "Crispy").
            
        Raises:
            ValueError: If value is not one of the allowed modes.
        """
        allowed_modes = ["Healthy", "Defrost", "Crispy"]
        if value not in allowed_modes:
            raise ValueError("Cook mode must be one of: Healthy, Defrost, or Crispy")
        self._cook_mode = value
    
    def __str__(self):
        """Return a string representation of the SmartAirFryer."""
        status = "on" if self._switched_on else "off"
        return f"SmartAirFryer is {status} with a cook_mode of {self._cook_mode}"


def test_custom_device():
    """
    Test function for the custom device classes.
    Tests initialization, toggling, and updating properties.
    Also tests handling of invalid values.
    """
    print("Testing custom device classes...")
    
    # Create instances of two custom devices (using SmartLight and SmartFridge as examples)
    # You should replace these with the two devices corresponding to your student number
    light = SmartLight()
    fridge = SmartFridge()
    
    # Test initial state
    print(light)  # Should be off with brightness of 50
    print(fridge)  # Should be off with temperature of 3
    
    # Test toggling devices
    light.toggle_switch()
    fridge.toggle_switch()
    print(light)  # Should be on with brightness of 50
    print(fridge)  # Should be on with temperature of 3
    
    # Test updating properties with valid values
    light.brightness = 75
    fridge.temperature = 5
    print(light)  # Should be on with brightness of 75
    print(fridge)  # Should be on with temperature of 5
    
    # Test invalid property updates
    try:
        light.brightness = 0
        print("Failed: Accepted brightness < 1")
    except ValueError:
        print("Success: Rejected brightness < 1")
    
    try:
        light.brightness = 101
        print("Failed: Accepted brightness > 100")
    except ValueError:
        print("Success: Rejected brightness > 100")
    
    try:
        fridge.temperature = 2
        print("Failed: Accepted invalid temperature value")
    except ValueError:
        print("Success: Rejected invalid temperature value")
    
    # Current state should be unchanged
    print(light)  # Should still be on with brightness of 75
    print(fridge)  # Should still be on with temperature of 5
    
    print("Custom device testing complete")


if __name__ == "__main__":
    test_custom_device()