import tkinter as tk
from tkinter import ttk
from smart_plug import SmartPlug
from smartDevice import SmartLight, SmartFridge
from smartHome import SmartHome
class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Control")
        self.root.configure(bg='lightgray')
        
        # Top control buttons
        self.btn_turn_on_all = ttk.Button(root, text="Turn on all", command=self.turn_on_all)
        self.btn_turn_on_all.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        
        self.btn_turn_off_all = ttk.Button(root, text="Turn off all", command=self.turn_off_all)
        self.btn_turn_off_all.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        # Device list frame with scrollbar
        self.frame_devices = ttk.Frame(root)
        self.frame_devices.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.canvas = tk.Canvas(self.frame_devices, bg="lightgray")
        self.scrollbar = ttk.Scrollbar(self.frame_devices, orient="vertical", command=self.canvas.yview)
        self.device_frame = ttk.Frame(self.canvas)
        
        self.device_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.window = self.canvas.create_window((0, 0), window=self.device_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Add button
        self.btn_add = ttk.Button(root, text="Add Device", command=self.add_device)
        self.btn_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Dynamic device storage
        self.devices = []
        
        # Grid resizing
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
    
    def add_device(self):
        device = SmartDevice(self.device_frame, f"Device {len(self.devices) + 1}")
        self.devices.append(device)
        self.root.update_idletasks()
    
    def turn_on_all(self):
        for device in self.devices:
            device.toggle(True)
    
    def turn_off_all(self):
        for device in self.devices:
            device.toggle(False)

class SmartDevice:
    def __init__(self, parent, name):
        self.frame = ttk.Frame(parent, padding=5, relief="solid")
        self.frame.pack(fill="x", padx=5, pady=2)
        
        self.name = name
        self.status = tk.StringVar(value=f"{name}: off")
        self.label = ttk.Label(self.frame, textvariable=self.status)
        self.label.pack(side="left", padx=5)
        
        self.btn_toggle = ttk.Button(self.frame, text="Toggle", command=self.toggle)
        self.btn_toggle.pack(side="right", padx=2)
        
        self.btn_delete = ttk.Button(self.frame, text="Delete", command=self.delete)
        self.btn_delete.pack(side="right", padx=2)
    
    def toggle(self, state=None):
        if state is None:
            state = "off" in self.status.get()
        self.status.set(f"{self.name}: {'on' if state else 'off'}")
    
    def delete(self):
        self.frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
