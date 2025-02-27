class SmartHome:
    """
    A class representing a smart home that can manage multiple smart devices.
    """
    
    def __init__(self, max_items=10):
        """
        Initialize a SmartHome with a maximum number of devices.
        
        Args:
            max_items (int, optional): Maximum number of devices. Defaults to 10.
        """
        self._devices = []
        self._max_items = max_items
    
    def add_device(self, device):
        """
        Add a device to the smart home.
        
        Args:
            device: A smart device object to add.
            
        Raises:
            ValueError: If the maximum number of devices is reached.
        """
        if len(self._devices) >= self._max_items:
            raise ValueError(f"Cannot add more devices. Maximum of {self._max_items} reached.")
        self._devices.append(device)
    
    def get_device(self, index):
        """
        Get a device by its index.
        
        Args:
            index (int): The index of the device.
            
        Returns:
            The device at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        return self._devices[index]
    
    def toggle_device(self, index):
        """
        Toggle a device by its index.
        
        Args:
            index (int): The index of the device.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        self._devices[index].toggle_switch()
    
    def switch_all_on(self):
        """Turn all devices on."""
        for device in self._devices:
            if not device.switched_on:
                device.toggle_switch()
    
    def switch_all_off(self):
        """Turn all devices off."""
        for device in self._devices:
            if device.switched_on:
                device.toggle_switch()
    
    def remove_device(self, index):
        """
        Remove a device by its index.
        
        Args:
            index (int): The index of the device.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        return self._devices.pop(index)
    
    def update_option(self, index, value):
        """
        Update the option attribute of a device by its index.
        
        Args:
            index (int): The index of the device.
            value: The new value for the option attribute.
            
        Raises:
            IndexError: If the index is out of range.
            AttributeError: If the device does not have a matching option attribute.
        """
        device = self.get_device(index)
        
        # For SmartPlug
        if hasattr(device, 'consumption_rate'):
            device.consumption_rate = value
        # For SmartLight
        elif hasattr(device, 'brightness'):
            device.brightness = value
        # For SmartFridge
        elif hasattr(device, 'temperature') and hasattr(device, 'name') and device.name == "SmartFridge":
            device.temperature = value
        # For SmartHeater
        elif hasattr(device, 'setting'):
            device.setting = value
        # For SmartTV
        elif hasattr(device, 'channel'):
            device.channel = value
        # For SmartSpeaker
        elif hasattr(device, 'streaming'):
            device.streaming = value
        # For SmartDoorBell
        elif hasattr(device, 'sleep_mode'):
            device.sleep_mode = value
        # For SmartOven
        elif hasattr(device, 'temperature') and hasattr(device, 'name') and device.name == "SmartOven":
            device.temperature = value
        # For SmartWashingMachine
        elif hasattr(device, 'wash_mode'):
            device.wash_mode = value
        # For SmartDoor
        elif hasattr(device, 'locked'):
            device.locked = value
        # For SmartAirFryer
        elif hasattr(device, 'cook_mode'):
            device.cook_mode = value
        else:
            raise AttributeError(f"Device at index {index} does not have a matching option attribute")
    
    def __str__(self):
        """Return a string representation of the SmartHome."""
        result = f"SmartHome with {len(self._devices)} device(s):"
        
        for i, device in enumerate(self._devices):
            result += f"\n{i+1}- {device}"
        
        return result


def test_smart_home():
    """
    Test function for the SmartHome class.
    Tests adding devices, toggling, retrieving, and managing device properties.
    """
    from smart_plug import SmartPlug
    from smart_device import SmartLight, SmartFridge
    
    print("Testing SmartHome class...")
    
    # Create devices (replace with the two devices corresponding to your student number)
    plug = SmartPlug(60)
    light = SmartLight()
    fridge = SmartFridge()
    
    # Create a SmartHome with a maximum of 5 devices
    home = SmartHome(max_items=5)
    
    # Add devices
    home.add_device(plug)
    home.add_device(light)
    home.add_device(fridge)
    
    # Print initial state
    print(home)
    
    # Retrieve and verify each device
    retrieved_plug = home.get_device(0)
    retrieved_light = home.get_device(1)
    retrieved_fridge = home.get_device(2)
    
    print("Retrieved devices:")
    print(retrieved_plug)
    print(retrieved_light)
    print(retrieved_fridge)
    
    # Toggle each device and verify
    home.toggle_device(0)
    home.toggle_device(1)
    home.toggle_device(2)
    print("\nAfter toggling each device:")
    print(home)
    
    # Turn all devices off
    home.switch_all_off()
    print("\nAfter turning all devices off:")
    print(home)
    
    # Turn all devices on
    home.switch_all_on()
    print("\nAfter turning all devices on:")
    print(home)
    
    # Update options
    print("\nUpdating device options...")
    home.update_option(0, 90)  # Update SmartPlug consumption rate
    home.update_option(1, 80)  # Update SmartLight brightness
    home.update_option(2, 1)   # Update SmartFridge temperature
    
    print("After updating options:")
    print(home)
    
    # Test max_items limit
    print("\nTesting max_items limit...")
    for i in range(2):
        try:
            home.add_device(SmartPlug(50))
            print(f"Added device {i+4}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Test invalid option updates
    print("\nTesting invalid option updates...")
    try:
        home.update_option(0, 200)  # Invalid consumption rate
        print("Failed: Accepted invalid consumption rate")
    except ValueError as e:
        print(f"Success: {e}")
    
    # Test remove_device
    print("\nTesting remove_device...")
    removed_device = home.remove_device(2)
    print(f"Removed: {removed_device}")
    print("SmartHome after removal:")
    print(home)
    
    # Test invalid device index
    print("\nTesting invalid device index...")
    try:
        home.get_device(10)
        print("Failed: Accessed invalid device index")
    except IndexError as e:
        print(f"Success: {e}")
    
    print("SmartHome testing complete")


if __name__ == "__main__":
    test_smart_home()