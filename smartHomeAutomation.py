import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class SmartDevice:
    def __init__(self, name, state=False, option_value=None):
        self.name = name
        self.state = state
        self.option_value = option_value

    def toggle(self):
        self.state = not self.state
        return f"{self.name}: {'on' if self.state else 'off'}"

    def edit(self, new_value):
        self.option_value = new_value
        return f"{self.name} setting updated to {self.option_value}"

    def __str__(self):
        return f"{self.name}: {'on' if self.state else 'off'}, {self.option_value}" if self.option_value is not None else f"{self.name}: {'on' if self.state else 'off'}"


def update_display():
    for widget in frame.winfo_children():
        widget.destroy()
    
    for device in devices:
        row = tk.Frame(frame)
        row.pack(fill="x", pady=2)
        
        tk.Label(row, text=str(device)).pack(side="left", padx=5)
        tk.Button(row, text="Toggle", command=lambda d=device: toggle_device(d)).pack(side="left", padx=2)
        tk.Button(row, text="Edit", command=lambda d=device: edit_device(d)).pack(side="left", padx=2)
        tk.Button(row, text="Delete", command=lambda d=device: delete_device(d)).pack(side="left", padx=2)

def toggle_device(device):
    messagebox.showinfo("Toggle", device.toggle())
    update_display()

def edit_device(device):
    new_value = simpledialog.askstring("Edit", f"Enter new setting for {device.name}:")
    if new_value:
        messagebox.showinfo("Edit", device.edit(new_value))
    update_display()

def delete_device(device):
    devices.remove(device)
    update_display()

def turn_on_all():
    for device in devices:
        device.state = True
    update_display()

def turn_off_all():
    for device in devices:
        device.state = False
    update_display()

def add_device():
    name = simpledialog.askstring("Add Device", "Enter device name:")
    if name:
        devices.append(SmartDevice(name))
    update_display()

root = tk.Tk()
root.title("Smart Home Controller")

control_frame = tk.Frame(root)
control_frame.pack(fill="x", pady=5)

tk.Button(control_frame, text="Turn on all", command=turn_on_all).pack(side="left", padx=5)
tk.Button(control_frame, text="Turn off all", command=turn_off_all).pack(side="left", padx=5)
tk.Button(control_frame, text="Add", command=add_device).pack(side="left", padx=5)

canvas = tk.Canvas(root)
frame = tk.Frame(canvas)
canvas.pack(fill="both", expand=True)
frame.pack(fill="both", expand=True)

devices = [SmartDevice("Light", False, "Brightness: 0"), SmartDevice("Fridge", False, "Temperature: 3"), SmartDevice("Plug", False, "Consumption: 45")]

update_display()
root.mainloop()
