import tkinter as tk
from tkinter import simpledialog, messagebox

# Task 1: Base SmartDevice class
class SmartDevice:
    def __init__(self, name, option_value, option_range, default_value):
        if option_value not in option_range:
            raise ValueError(f"{name} option value must be within {option_range}.")
        self.name = name
        self._switched_on = False
        self._option_value = option_value
        self._option_range = option_range
        self._default_value = default_value
    
    def toggle_switch(self):
        self._switched_on = not self._switched_on
    
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"{self.name}: {state}, {self.get_status()}"
    
    @property
    def option_value(self):
        return self._option_value
    
    @option_value.setter
    def option_value(self, value):
        if value not in self._option_range:
            raise ValueError(f"{self.name} option value must be within {self._option_range}.")
        self._option_value = value
    
    def get_status(self):
        return f"Value: {self._option_value}"  # Override in subclasses

# Task 2: SmartDevice subclasses
class SmartLight(SmartDevice):
    def __init__(self, brightness=50):
        super().__init__("Light", brightness, range(0, 101), 50)
    def get_status(self):
        return f"Brightness: {self.option_value}"

class SmartFridge(SmartDevice):
    def __init__(self, temperature=3):
        super().__init__("Fridge", temperature, {1, 3, 5}, 3)
    def get_status(self):
        return f"Temperature: {self.option_value}"

class SmartPlug(SmartDevice):
    def __init__(self, consumption=45):
        super().__init__("Plug", consumption, range(0, 101), 45)
    def get_status(self):
        return f"Consumption: {self.option_value}"

# Task 3-5: GUI Implementation
class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Automation")
        self.devices = []
        
        self.control_frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
        self.control_frame.pack(fill=tk.BOTH, expand=True)
        
        self.btn_turn_on_all = tk.Button(self.control_frame, text="Turn on all", command=self.turn_on_all)
        self.btn_turn_on_all.pack()
        
        self.btn_turn_off_all = tk.Button(self.control_frame, text="Turn off all", command=self.turn_off_all)
        self.btn_turn_off_all.pack()
        
        self.device_frame = tk.Frame(self.control_frame, bg="lightgray")
        self.device_frame.pack(fill=tk.BOTH, expand=True)
        
        self.btn_add = tk.Button(self.control_frame, text="Add", command=self.add_device)
        self.btn_add.pack()
        
        self.update_ui()
    
    def add_device(self):
        name = simpledialog.askstring("Add Device", "Enter device type (Light, Fridge, Plug):")
        if name:
            if name.lower() == "light":
                self.devices.append(SmartLight())
            elif name.lower() == "fridge":
                self.devices.append(SmartFridge())
            elif name.lower() == "plug":
                self.devices.append(SmartPlug())
            else:
                messagebox.showerror("Error", "Invalid device type!")
            self.update_ui()
    
    def remove_device(self, device):
        self.devices.remove(device)
        self.update_ui()
    
    def toggle_device(self, device):
        device.toggle_switch()
        self.update_ui()
    
    def edit_device(self, device):
        new_value = simpledialog.askinteger("Edit Device", f"Enter new value for {device.name}:")
        if new_value is not None:
            try:
                device.option_value = new_value
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            self.update_ui()
    
    def turn_on_all(self):
        for device in self.devices:
            device._switched_on = True
        self.update_ui()
    
    def turn_off_all(self):
        for device in self.devices:
            device._switched_on = False
        self.update_ui()
    
    def update_ui(self):
        for widget in self.device_frame.winfo_children():
            widget.destroy()
        
        for device in self.devices:
            row = tk.Frame(self.device_frame, bg="lightgray")
            row.pack(fill=tk.X)
            
            lbl = tk.Label(row, text=str(device), bg="lightgray")
            lbl.pack(side=tk.LEFT)
            
            tk.Button(row, text="Toggle", command=lambda d=device: self.toggle_device(d)).pack(side=tk.RIGHT)
            tk.Button(row, text="Edit", command=lambda d=device: self.edit_device(d)).pack(side=tk.RIGHT)
            tk.Button(row, text="Delete", command=lambda d=device: self.remove_device(d)).pack(side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
