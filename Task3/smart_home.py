class SmartHome:
    def __init__(self, max_items=10):
        self.devices = []
        self.max_items = max_items
    
    def add_device(self, device):
        if len(self.devices) >= self.max_items:
            raise ValueError("Cannot add more devices. Maximum limit reached.")
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
            device.switched_on = True
    
    def switch_all_off(self):
        for device in self.devices:
            device.switched_on = False
    
    def remove_device(self, index):
        if 0 <= index < len(self.devices):
            del self.devices[index]
        else:
            raise IndexError("Invalid device index.")
    
    def update_option(self, index, value):
        device = self.get_device(index)
        if hasattr(device, "set_channel"):
            device.set_channel(value)
        elif hasattr(device, "set_wash_mode"):
            device.set_wash_mode(value)
        elif hasattr(device, "set_consumption_rate"):
            device.set_consumption_rate(value)
        else:
            raise AttributeError("Device does not support updating this option.")
    
    def __str__(self):
        output = [f"SmartHome with {len(self.devices)} device(s):"]
        for i, device in enumerate(self.devices, start=1):
            output.append(f"{i}- {device}")
        return "\n".join(output)


