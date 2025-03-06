
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task3')))
import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
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
        device = self.home.devices[index]
        try:
            if isinstance(device, SmartPlug):
                new_value = simpledialog.askinteger("Edit Device", "Enter new power consumption:")
                if new_value is not None:
                    device.set_consumption_rate(new_value)
            elif isinstance(device, SmartTV):
                new_value = simpledialog.askinteger("Edit Device", "Enter new channel (1-734):")
                if new_value is not None:
                    device.set_channel(new_value)
            elif isinstance(device, SmartWashingMachine):
                new_value = simpledialog.askstring("Edit Device", "Enter new wash mode (Daily wash/Quick wash/Eco):")
                if new_value is not None:
                    device.set_wash_mode(new_value)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        self.update_display()


    def delete_device(self, index):
        self.home.remove_device(index)
        self.update_display()
    
    def add_device(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Device")
        tk.Label(add_window, text="Select device type:").pack(pady=5)
        
        device_type_var = tk.StringVar()
        device_dropdown = ttk.Combobox(add_window, textvariable=device_type_var, values=["Plug", "TV", "Washing"])
        device_dropdown.pack(pady=5)
        
        def confirm_add():
            device_type = device_type_var.get().lower()
            if device_type == "plug":
                new_device = SmartPlug(50)
            elif device_type == "tv":
                new_device = SmartTV()
            elif device_type == "washing":
                new_device = SmartWashingMachine()
            else:
                return
            self.home.add_device(new_device)
            self.update_display()
            add_window.destroy()
        
        tk.Button(add_window, text="Add", command=confirm_add).pack(pady=10)

