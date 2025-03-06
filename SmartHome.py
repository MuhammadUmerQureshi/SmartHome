from SmartPlug import SmartPlug
from SmartDevice import SmartTV, SmartAirFryer

class SmartHome:
        
    def __init__(self, max_items=10):
        self._devices = []
        self._max_items = max_items # Maximum number of devices could be passed as a contructor argument
    
    def add_device(self, device):
        
        if len(self._devices) >= self._max_items:
            raise ValueError(f"Cannot add more devices. Maximum of {self._max_items} reached.")
        self._devices.append(device)
    
    def get_device(self, index):
        
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        return self._devices[index]
    
    def toggle_device(self, index):
        
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        self._devices[index].toggle_switch()
    
    def switch_all_on(self):
        for device in self._devices:
            if not device.switched_on:
                device.toggle_switch()
    
    def switch_all_off(self):
        for device in self._devices:
            if device.switched_on:
                device.toggle_switch()
    
    def remove_device(self, index):
        
        if index < 0 or index >= len(self._devices):
            raise IndexError("Device index out of range")
        return self._devices.pop(index)
    
    def update_option(self, index, value):
        
        device = self.get_device(index)
        
        # For SmartPlug
        if hasattr(device, 'consumption_rate'):
            device.consumption_rate = value
        # For SmartTV
        elif hasattr(device, 'channel'):
            device.channel = value
        # For SmartAirFryer
        elif hasattr(device, 'cook_mode'):
            device.cook_mode = value
        else:
            raise AttributeError(f"Device at index {index} does not have a matching option")
    
    def __str__(self):
        result = f"SmartHome with {len(self._devices)} device(s):"
        
        for i, device in enumerate(self._devices):
            result += f"\n{i+1}- {device}"
        
        return result


def test_smart_home():

    
    print("Testing SmartHome class...")
    
    plug = SmartPlug(60)
    tv = SmartTV()
    air_fryer = SmartAirFryer()
    
    # Create a SmartHome with a maximum of 5 devices
    home = SmartHome(max_items=5)
    
    # Add devices
    home.add_device(plug)
    home.add_device(tv)
    home.add_device(air_fryer)
    
    # Print initial state
    print(home)
    
    # Retrieve and verify each device
    retrieved_plug = home.get_device(0)
    retrieved_tv = home.get_device(1)
    retrieved_air_fryer = home.get_device(2)
    
    print("Retrieved devices:")
    print(retrieved_plug)
    print(retrieved_tv)
    print(retrieved_air_fryer)
    
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
    try:
        home.update_option(0, 90)  # Update SmartPlug consumption rate
        home.update_option(1, 5)   # Update SmartTV channel
        home.update_option(2, 'bake')  # Update SmartAirFryer cook mode
    except ValueError as e:
        print(f"Error updating device options: {e}")
    
    print("After updating options:")
    print(home)
    
    # Test max_items limit
    print("\nTesting max_items limit...")
    for i in range(5):
        try:
            home.add_device(SmartPlug(50))
            print(f"Added device {i+4}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Test invalid option updates
    print("\nTesting invalid option updates...")
    try:
        home.update_option(0, 200)  # Invalid consumption rate
        print("Failed: Accepted invalid consumption rate") #should not be printed for successful harder constraints
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
        print("Failed: Accessed invalid device index") #should not be printed for successful harder constraints
    except IndexError as e:
        print(f"{e}")
    
    print("SmartHome testing complete")


if __name__ == "__main__":
    test_smart_home()