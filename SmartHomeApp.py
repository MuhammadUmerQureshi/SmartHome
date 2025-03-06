import tkinter as tk
from tkinter import messagebox
from SmartDevice import SmartTV, SmartAirFryer
from SmartPlug import SmartPlug

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Controller")
        self.devices = []
        
        self.control_frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
        self.control_frame.pack(padx=10, pady=10)
        
        tk.Button(self.control_frame, text="Turn on all", command=self.turn_on_all).grid(row=0, column=0)
        tk.Button(self.control_frame, text="Turn off all", command=self.turn_off_all).grid(row=0, column=1)
        
        self.device_frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
        self.device_frame.pack(padx=10, pady=10)
        
        self.add_device_button = tk.Button(root, text="Add Device", command=self.add_device)
        self.add_device_button.pack(pady=5)
        
        self.update_device_list()
    
    def update_device_list(self):
        for widget in self.device_frame.winfo_children():
            widget.destroy()
        
        for idx, device in enumerate(self.devices):
            tk.Label(self.device_frame, text=str(device)).grid(row=idx, column=0, sticky='w')
            tk.Button(self.device_frame, text="Toggle", command=lambda d=device: self.toggle_device(d)).grid(row=idx, column=1)
            tk.Button(self.device_frame, text="Edit", command=lambda d=device: self.edit_device(d)).grid(row=idx, column=2)
            tk.Button(self.device_frame, text="Delete", command=lambda d=device: self.delete_device(d)).grid(row=idx, column=3)
    
    def toggle_device(self, device):
        device.toggle_switch()
        self.update_device_list()
    
    def edit_device(self, device):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Device")
        
        if isinstance(device, SmartTV):
            tk.Label(edit_window, text="Channel:").pack()
            entry = tk.Entry(edit_window)
            entry.insert(0, str(device.channel))
            entry.pack()
            tk.Button(edit_window, text="Save", command=lambda: self.save_edit(device, entry.get(), edit_window)).pack()
        elif isinstance(device, SmartAirFryer):
            tk.Label(edit_window, text="Cooking Mode:").pack()
            entry = tk.Entry(edit_window)
            entry.insert(0, str(device.cook_mode))
            entry.pack()
            tk.Button(edit_window, text="Save", command=lambda: self.save_edit(device, entry.get(), edit_window)).pack()
        elif isinstance(device, SmartPlug):
            tk.Label(edit_window, text="Consumption Rate:").pack()
            entry = tk.Entry(edit_window)
            entry.insert(0, str(device.consumption_rate))
            entry.pack()
            tk.Button(edit_window, text="Save", command=lambda: self.save_edit(device, entry.get(), edit_window)).pack()
    
    def save_edit(self, device, new_value, window):
        try:
            if isinstance(device, SmartTV):
                device.channel = int(new_value)
            elif isinstance(device, SmartAirFryer):
                device.cook_mode = new_value
            elif isinstance(device, SmartPlug):
                device.consumption_rate = int(new_value)
            self.update_device_list()
            window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid value.")
    
    def delete_device(self, device):
        self.devices.remove(device)
        self.update_device_list()
    
    def add_device(self):
        def add():
            device_type = device_var.get()
            if device_type == "TV":
                self.devices.append(SmartTV())
            elif device_type == "Air Fryer":
                self.devices.append(SmartAirFryer())
            elif device_type == "Plug":
                self.devices.append(SmartPlug(consumption_rate=50))
            self.update_device_list()
            add_window.destroy()
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Device")
        
        tk.Label(add_window, text="Select device type:").pack()
        device_var = tk.StringVar(value="TV")
        tk.Radiobutton(add_window, text="Smart TV", variable=device_var, value="TV").pack()
        tk.Radiobutton(add_window, text="Smart Air Fryer", variable=device_var, value="Air Fryer").pack()
        tk.Radiobutton(add_window, text="Smart Plug", variable=device_var, value="Plug").pack()
        tk.Button(add_window, text="Add", command=add).pack()
    
    def turn_on_all(self):
        for device in self.devices:
            if not device.switched_on:
                device.toggle_switch()
        self.update_device_list()
    
    def turn_off_all(self):
        for device in self.devices:
            if device.switched_on:
                device.toggle_switch()
        self.update_device_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()