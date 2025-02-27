import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import json

DEVICE_TYPES = ["Light", "Fridge", "Plug", "Heater", "TV", "Speaker"]

class SmartHome:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_name):
        self.devices = [d for d in self.devices if d['name'] != device_name]
    
    def toggle_device(self, device_name):
        for device in self.devices:
            if device['name'] == device_name:
                device['status'] = "on" if device['status'] == "off" else "off"
    
    def edit_device(self, device_name):
        for device in self.devices:
            if device['name'] == device_name:
                new_status = simpledialog.askstring("Edit Device", f"Set new value for {device_name}:")
                if new_status:
                    device['status'] = new_status

    def to_dict(self):
        return {"name": self.name, "devices": self.devices}

    @staticmethod
    def from_dict(data):
        home = SmartHome(data["name"])
        home.devices = data["devices"]
        return home

class SmartHomesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Homes Manager")
        self.homes = []
        self.load_homes()
        self.create_main_screen()

    def create_main_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Smart Homes", font=("Arial", 16, "bold")).pack(pady=10)
        
        home_frame = tk.Frame(self.root)
        home_frame.pack(fill=tk.BOTH, expand=True)
        
        for home in self.homes:
            frame = tk.LabelFrame(home_frame, text=home.name, padx=10, pady=10)
            frame.pack(fill=tk.X, padx=5, pady=5)
            
            for device in home.devices:
                device_frame = tk.Frame(frame)
                device_frame.pack(fill=tk.X)
                tk.Label(device_frame, text=f"{device['name']}: {device['status']}").pack(side=tk.LEFT)
                tk.Button(device_frame, text="Toggle", command=lambda d=device['name'], h=home: self.toggle_device(h, d)).pack(side=tk.LEFT, padx=5)
                tk.Button(device_frame, text="Edit", command=lambda d=device['name'], h=home: self.edit_device_popup(h, d)).pack(side=tk.LEFT, padx=5)
                tk.Button(device_frame, text="Delete", command=lambda d=device['name'], h=home: self.remove_device(h, d)).pack(side=tk.LEFT, padx=5)
            
            tk.Button(frame, text="Add Device", command=lambda h=home: self.add_device(h)).pack(pady=2)
            tk.Button(frame, text="Remove Home", command=lambda h=home: self.remove_home(h)).pack(pady=2)
        
        tk.Button(self.root, text="Add Home", command=self.add_home).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.save_and_exit).pack(pady=10)
    
    def toggle_device(self, home, device_name):
        home.toggle_device(device_name)
        self.create_main_screen()
    
    def edit_device_popup(self, home, device_name):
        home.edit_device(device_name)
        self.create_main_screen()
    
    def remove_device(self, home, device_name):
        home.remove_device(device_name)
        self.create_main_screen()
    
    def add_home(self):
        name = simpledialog.askstring("Add Home", "Enter home name:")
        if name:
            self.homes.append(SmartHome(name))
            self.create_main_screen()
    
    def remove_home(self, home):
        self.homes.remove(home)
        self.create_main_screen()
    
    def add_device(self, home):
        device_popup = tk.Toplevel(self.root)
        device_popup.title("Add Device")
        tk.Label(device_popup, text="Select Device Type:").pack()
        device_type = ttk.Combobox(device_popup, values=DEVICE_TYPES)
        device_type.pack()
        
        def confirm():
            selected_device = device_type.get()
            if selected_device:
                home.add_device({"name": selected_device, "status": "off"})
                device_popup.destroy()
                self.create_main_screen()
        
        tk.Button(device_popup, text="Add", command=confirm).pack()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def load_homes(self):
        try:
            with open("homes.json", "r") as file:
                data = json.load(file)
                self.homes = [SmartHome.from_dict(home) for home in data]
        except FileNotFoundError:
            self.homes = []
    
    def save_and_exit(self):
        with open("homes.json", "w") as file:
            json.dump([home.to_dict() for home in self.homes], file)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomesApp(root)
    root.mainloop()