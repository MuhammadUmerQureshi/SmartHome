
import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task3')))
from smart_home import SmartHome
from smart_plug import SmartPlug
from smart_devices import SmartTV, SmartWashingMachine

class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home App")
        self.root.configure(bg='lightgrey')
        
        self.home = SmartHome()
        self.home.add_device(SmartPlug(45))
        self.home.add_device(SmartTV())
        self.home.add_device(SmartWashingMachine())
        
        self.create_gui()
    
    def create_gui(self):
        control_frame = tk.Frame(self.root, bg='lightgrey')
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="Turn on all", command=self.switch_all_on, relief='ridge', borderwidth=3).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Turn off all", command=self.switch_all_off, relief='ridge', borderwidth=3).pack(side=tk.LEFT, padx=5)
        
        self.device_frame = tk.Frame(self.root, bg='lightgrey')
        self.device_frame.pack(pady=10)
        
        tk.Button(self.root, text="Add", command=self.add_device, relief='ridge', borderwidth=3).pack(pady=5)
        
        self.update_display()
    
    def update_display(self):
        for widget in self.device_frame.winfo_children():
            widget.destroy()
        
        for i, device in enumerate(self.home.devices):
            row_frame = tk.Frame(self.device_frame, bg='lightgrey')
            row_frame.pack(fill='x', pady=2)
            
            tk.Label(row_frame, text=str(device), font=("Arial", 12), bg='lightgrey').pack(side=tk.LEFT, padx=5)
            tk.Button(row_frame, text="Toggle", command=lambda i=i: self.toggle_device(i), relief='ridge', borderwidth=3).pack(side=tk.RIGHT, padx=2)
            tk.Button(row_frame, text="Edit", command=lambda i=i: self.edit_device(i), relief='ridge', borderwidth=3).pack(side=tk.RIGHT, padx=2)
            tk.Button(row_frame, text="Delete", command=lambda i=i: self.delete_device(i), relief='ridge', borderwidth=3).pack(side=tk.RIGHT, padx=2)
    
    def switch_all_on(self):
        self.home.switch_all_on()
        self.update_display()
    
    def switch_all_off(self):
        self.home.switch_all_off()
        self.update_display()
    
    def toggle_device(self, index):
        self.home.toggle_device(index)
        self.update_display()
    
    def edit_device(self, index):
        print(f"Edit device at index {index}")
    
    def delete_device(self, index):
        self.home.remove_device(index)
        self.update_display()
    
    def add_device(self):
        print("Add new device")
