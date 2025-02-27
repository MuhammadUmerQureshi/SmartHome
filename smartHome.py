from smartDevice import SmartLight, SmartFridge
from smart_plug import SmartPlug
class SmartHome:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
    
    def get_device(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        raise IndexError("Invalid device index.")
    
    def toggle_device(self, index):
        device = self.get_device(index)
        device.toggle_switch()
    
    def switch_all_on(self):
        for device in self.devices:
            if not device._switched_on:
                device.toggle_switch()
    
    def switch_all_off(self):
        for device in self.devices:
            if device._switched_on:
                device.toggle_switch()
    
    def __str__(self):
        result = f"SmartHome with {len(self.devices)} device(s):\n"
        for i, device in enumerate(self.devices, start=1):
            result += f"{i}- {device}\n"
        return result.strip()

def test_smart_home():
    home = SmartHome()
    
    light = SmartLight()
    fridge = SmartFridge()
    plug = SmartPlug(60)
    
    home.add_device(light)
    home.add_device(fridge)
    home.add_device(plug)
    
    print(home)
    
    home.toggle_device(0)  # Toggle SmartLight
    home.toggle_device(2)  # Toggle SmartPlug
    print(home)
    
    home.switch_all_off()
    print(home)

def test_invalid_operations():
    home = SmartHome()
    try:
        home.toggle_device(0)  # Should raise IndexError
    except IndexError as e:
        print("Error handled:", e)
    
# Run the test functions
test_smart_home()
test_invalid_operations()
