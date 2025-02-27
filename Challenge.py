import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class SmartHome:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_name):
        self.devices = [d for d in self.devices if d['name'] != device_name]

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
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Smart Homes", font=("Arial", 16)).pack()
        for home in self.homes:
            tk.Button(self.root, text=home.name, command=lambda h=home: self.manage_home(h)).pack()
        tk.Button(self.root, text="Add Home", command=self.add_home).pack()
        tk.Button(self.root, text="Exit", command=self.save_and_exit).pack()

    def manage_home(self, home):
        self.clear_window()
        tk.Label(self.root, text=f"Managing {home.name}", font=("Arial", 14)).pack()
        for device in home.devices:
            tk.Label(self.root, text=f"{device['name']}: {device['status']}").pack()
        tk.Button(self.root, text="Add Device", command=lambda: self.add_device(home)).pack()
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def add_home(self):
        name = simpledialog.askstring("Add Home", "Enter home name:")
        if name:
            self.homes.append(SmartHome(name))
            self.create_main_menu()

    def add_device(self, home):
        name = simpledialog.askstring("Add Device", "Enter device name:")
        status = simpledialog.askstring("Device Status", "Enter device status (on/off):")
        if name and status:
            home.add_device({"name": name, "status": status})
            self.manage_home(home)

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
