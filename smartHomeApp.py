import tkinter as tk
from tkinter import Label, Button
from smart_plug import SmartPlug
from smartDevice import SmartLight, SmartFridge
from smartHome import SmartHome
import tkinter as tk
from tkinter import messagebox

class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home App")
        self.root.configure(bg='lightgray')
        
        self.devices = [
            {"name": "Light", "status": "off", "attribute": "Brightness: 0"},
            {"name": "Fridge", "status": "off", "attribute": "Temperature: 3"},
            {"name": "Plug", "status": "off", "attribute": "Consumption: 45"}
        ]
        
        self.create_widgets()

    def create_widgets(self):
        button_style = {'bd': 5, 'relief': 'ridge', 'bg': 'white', 'padx': 10, 'pady': 5}
        
        top_frame = tk.Frame(self.root, bg='lightgray')
        top_frame.pack(pady=10)
        
        tk.Button(top_frame, text="Turn on all", command=self.turn_on_all, **button_style).pack(side=tk.LEFT, padx=10)
        tk.Button(top_frame, text="Turn off all", command=self.turn_off_all, **button_style).pack(side=tk.LEFT, padx=10)
        
        self.device_frame = tk.Frame(self.root, bg='lightgray')
        self.device_frame.pack(pady=10)
        
        self.display_devices()
        
        add_button = tk.Button(self.root, text="Add", command=self.add_device, **button_style)
        add_button.pack(pady=10)
    
    def display_devices(self):
        for widget in self.device_frame.winfo_children():
            widget.destroy()
        
        for device in self.devices:
            frame = tk.Frame(self.device_frame, bg='lightgray', pady=2)
            frame.pack(fill='x')
            
            label = tk.Label(frame, text=f"{device['name']}: {device['status']}, {device['attribute']}", bg='lightgray')
            label.pack(side=tk.LEFT, padx=10)
            
            button_frame = tk.Frame(frame, bg='lightgray')
            button_frame.pack(side=tk.RIGHT)
            
            tk.Button(button_frame, text="Toggle", command=lambda d=device: self.toggle_device(d), bd=5, relief='ridge').pack(side=tk.LEFT, padx=5)
            tk.Button(button_frame, text="Edit", command=lambda d=device: self.edit_device(d), bd=5, relief='ridge').pack(side=tk.LEFT, padx=5)
            tk.Button(button_frame, text="Delete", command=lambda d=device: self.delete_device(d), bd=5, relief='ridge').pack(side=tk.LEFT, padx=5)
    
    def toggle_device(self, device):
        device["status"] = "on" if device["status"] == "off" else "off"
        self.display_devices()
    
    def edit_device(self, device):
        messagebox.showinfo("Edit", f"Editing {device['name']}")
    
    def delete_device(self, device):
        self.devices.remove(device)
        self.display_devices()
    
    def turn_on_all(self):
        for device in self.devices:
            device["status"] = "on"
        self.display_devices()
    
    def turn_off_all(self):
        for device in self.devices:
            device["status"] = "off"
        self.display_devices()
    
    def add_device(self):
        self.devices.append({"name": "New Device", "status": "off", "attribute": "Custom"})
        self.display_devices()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()
