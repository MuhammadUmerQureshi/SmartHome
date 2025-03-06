import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from SmartHome import SmartHome
from SmartPlug import SmartPlug
from SmartDevice import SmartTV, SmartAirFryer

class SmartHomesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Homes Manager")
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        
        # Data structure to hold multiple smart homes
        self.homes = {}  # {name: SmartHome}
        self.current_home = None
        self.current_home_name = tk.StringVar()
        
        # Data file
        self.data_file = "smart_homes_data.json"
        
        # Load existing data
        self.load_data()
        
        # Create the UI
        self.create_ui()
        
    def create_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top control panel
        control_frame = ttk.LabelFrame(main_frame, text="Homes Control Panel", padding="10")
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Home selector and control buttons
        home_frame = ttk.Frame(control_frame)
        home_frame.pack(fill=tk.X)
        
        ttk.Label(home_frame, text="Current Home:").grid(row=0, column=0, padx=5, pady=5)
        
        # Combobox to select homes
        self.home_selector = ttk.Combobox(home_frame, textvariable=self.current_home_name, state="readonly", width=20)
        self.home_selector.grid(row=0, column=1, padx=5, pady=5)
        self.home_selector.bind("<<ComboboxSelected>>", self.on_home_selected)
        self.update_home_selector()
        
        # Home controls
        ttk.Button(home_frame, text="Add New Home", command=self.add_new_home).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(home_frame, text="Rename Home", command=self.rename_home).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(home_frame, text="Delete Home", command=self.delete_home).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(home_frame, text="Save All", command=self.save_data).grid(row=0, column=5, padx=5, pady=5)
        
        # Split view for current home
        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Devices panel
        self.devices_frame = ttk.LabelFrame(paned, text="Devices", padding="10")
        
        # Device controls
        device_controls = ttk.Frame(self.devices_frame)
        device_controls.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(device_controls, text="Add Smart Plug", command=lambda: self.add_device("plug")).pack(side=tk.LEFT, padx=2)
        ttk.Button(device_controls, text="Add Smart TV", command=lambda: self.add_device("tv")).pack(side=tk.LEFT, padx=2)
        ttk.Button(device_controls, text="Add Air Fryer", command=lambda: self.add_device("airfryer")).pack(side=tk.LEFT, padx=2)
        ttk.Button(device_controls, text="Remove Device", command=self.remove_device).pack(side=tk.LEFT, padx=2)
        
        # Device list
        device_list_frame = ttk.Frame(self.devices_frame)
        device_list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar for device list
        scrollbar = ttk.Scrollbar(device_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for devices
        self.device_listbox = tk.Listbox(device_list_frame, yscrollcommand=scrollbar.set, height=15)
        self.device_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        scrollbar.config(command=self.device_listbox.yview)
        
        # Bind selection event
        self.device_listbox.bind('<<ListboxSelect>>', self.on_device_selected)
        
        paned.add(self.devices_frame, weight=1)
        
        # Device control panel
        self.control_panel = ttk.LabelFrame(paned, text="Device Control", padding="10")
        
        # Global controls
        global_controls = ttk.Frame(self.control_panel)
        global_controls.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(global_controls, text="All ON", command=self.switch_all_on).pack(side=tk.LEFT, padx=2)
        ttk.Button(global_controls, text="All OFF", command=self.switch_all_off).pack(side=tk.LEFT, padx=2)
        
        # Device info and controls
        self.device_info_frame = ttk.Frame(self.control_panel)
        self.device_info_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initially show "No device selected"
        ttk.Label(self.device_info_frame, text="No device selected").pack(padx=5, pady=20)
        
        paned.add(self.control_panel, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W).pack(fill=tk.X, pady=5)
        
        # Initialize the UI with the first home or prompt to create one
        if not self.homes:
            self.status_var.set("No homes found. Please create a new home.")
        else:
            first_home = next(iter(self.homes.keys()))
            self.current_home_name.set(first_home)
            self.current_home = self.homes[first_home]
            self.update_device_list()
            self.status_var.set(f"Loaded home: {first_home}")
    
    def update_home_selector(self):
        """Update the home selector combobox with current homes."""
        home_names = list(self.homes.keys())
        self.home_selector['values'] = home_names
        
        # If there are homes, select the current one or the first one
        if home_names:
            if self.current_home_name.get() not in home_names:
                self.current_home_name.set(home_names[0])
                self.current_home = self.homes[home_names[0]]
        else:
            self.current_home_name.set("")
            self.current_home = None
    
    def on_home_selected(self, event):
        """Handle home selection from combobox."""
        selected_home = self.current_home_name.get()
        if selected_home in self.homes:
            self.current_home = self.homes[selected_home]
            self.update_device_list()
            self.status_var.set(f"Switched to home: {selected_home}")
        
    def add_new_home(self):
        """Add a new smart home."""
        home_name = simpledialog.askstring("New Home", "Enter name for new home:")
        if home_name:
            if home_name in self.homes:
                messagebox.showerror("Error", f"Home '{home_name}' already exists.")
                return
            
            max_devices = simpledialog.askinteger("Max Devices", 
                                                 "Enter maximum number of devices (5-20):", 
                                                 minvalue=5, maxvalue=20)
            if max_devices:
                self.homes[home_name] = SmartHome(max_items=max_devices)
                self.current_home_name.set(home_name)
                self.current_home = self.homes[home_name]
                self.update_home_selector()
                self.update_device_list()
                self.status_var.set(f"Created new home: {home_name}")
                self.save_data()
    
    def rename_home(self):
        """Rename the current home."""
        if not self.current_home:
            messagebox.showwarning("Warning", "No home selected.")
            return
        
        old_name = self.current_home_name.get()
        new_name = simpledialog.askstring("Rename Home", f"Enter new name for '{old_name}':")
        
        if new_name and new_name != old_name:
            if new_name in self.homes:
                messagebox.showerror("Error", f"Home '{new_name}' already exists.")
                return
            
            self.homes[new_name] = self.homes.pop(old_name)
            self.current_home_name.set(new_name)
            self.update_home_selector()
            self.status_var.set(f"Renamed home: {old_name} to {new_name}")
            self.save_data()
    
    def delete_home(self):
        """Delete the current home."""
        if not self.current_home:
            messagebox.showwarning("Warning", "No home selected.")
            return
        
        home_name = self.current_home_name.get()
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{home_name}'?"):
            del self.homes[home_name]
            self.update_home_selector()
            
            # Select a new current home if available
            if self.homes:
                first_home = next(iter(self.homes.keys()))
                self.current_home_name.set(first_home)
                self.current_home = self.homes[first_home]
                self.update_device_list()
            else:
                self.current_home = None
                self.clear_device_controls()
                self.device_listbox.delete(0, tk.END)
            
            self.status_var.set(f"Deleted home: {home_name}")
            self.save_data()
    
    def add_device(self, device_type):
        """Add a new device to the current home."""
        if not self.current_home:
            messagebox.showwarning("Warning", "No home selected. Please create or select a home first.")
            return
        
        try:
            if device_type == "plug":
                consumption = simpledialog.askfloat("Smart Plug", "Enter consumption rate (1-100):", 
                                                  minvalue=1, maxvalue=100)
                if consumption is not None:
                    self.current_home.add_device(SmartPlug(consumption))
                    self.status_var.set(f"Added Smart Plug with consumption rate: {consumption}")
            
            elif device_type == "tv":
                self.current_home.add_device(SmartTV())
                self.status_var.set("Added Smart TV")
            
            elif device_type == "airfryer":
                self.current_home.add_device(SmartAirFryer())
                self.status_var.set("Added Smart Air Fryer")
            
            self.update_device_list()
            self.save_data()
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def remove_device(self):
        """Remove the selected device from the current home."""
        if not self.current_home:
            return
        
        selection = self.device_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "No device selected.")
            return
        
        device_idx = selection[0]
        
        try:
            device = self.current_home.remove_device(device_idx)
            self.update_device_list()
            self.clear_device_controls()
            self.status_var.set(f"Removed device: {device}")
            self.save_data()
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def update_device_list(self):
        """Update the device listbox with current devices."""
        self.device_listbox.delete(0, tk.END)
        
        if not self.current_home:
            return
        
        for i in range(len(self.current_home._devices)):
            device = self.current_home.get_device(i)
            status = "ON" if device.switched_on else "OFF"
            device_type = type(device).__name__
            self.device_listbox.insert(tk.END, f"{i+1}. {device_type} ({status})")
    
    def on_device_selected(self, event):
        """Handle device selection from listbox."""
        if not self.current_home:
            return
        
        selection = self.device_listbox.curselection()
        if not selection:
            return
        
        device_idx = selection[0]
        try:
            device = self.current_home.get_device(device_idx)
            self.show_device_controls(device_idx, device)
        except IndexError:
            self.clear_device_controls()
    
    def show_device_controls(self, device_idx, device):
        """Show controls for the selected device."""
        # Clear existing controls
        self.clear_device_controls()
        
        # Add new controls based on device type
        device_type = type(device).__name__
        
        # Common controls frame
        info_frame = ttk.LabelFrame(self.device_info_frame, text=f"{device_type} Controls", padding="10")
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status label
        status = "ON" if device.switched_on else "OFF"
        status_var = tk.StringVar(value=f"Status: {status}")
        status_label = ttk.Label(info_frame, textvariable=status_var)
        status_label.pack(pady=5)
        
        # Toggle button
        toggle_btn = ttk.Button(info_frame, text="Toggle ON/OFF", 
                               command=lambda: self.toggle_device(device_idx, status_var))
        toggle_btn.pack(pady=5)
        
        # Device-specific controls
        if device_type == "SmartPlug":
            ttk.Label(info_frame, text=f"Consumption Rate: {device.consumption_rate}").pack(pady=5)
            
            # Frame for consumption rate control
            rate_frame = ttk.Frame(info_frame)
            rate_frame.pack(pady=5)
            
            ttk.Label(rate_frame, text="Change Rate:").pack(side=tk.LEFT, padx=5)
            rate_var = tk.DoubleVar(value=device.consumption_rate)
            rate_scale = ttk.Scale(rate_frame, from_=1, to=100, variable=rate_var, 
                                  orient=tk.HORIZONTAL, length=200)
            rate_scale.pack(side=tk.LEFT)
            
            apply_btn = ttk.Button(rate_frame, text="Apply", 
                                  command=lambda: self.update_device_rate(device_idx, rate_var.get()))
            apply_btn.pack(side=tk.LEFT, padx=5)
            
        elif device_type == "SmartTV":
            # Channel control
            ttk.Label(info_frame, text=f"Current Channel: {device.channel}").pack(pady=5)
            
            channel_frame = ttk.Frame(info_frame)
            channel_frame.pack(pady=5)
            
            ttk.Label(channel_frame, text="Change Channel:").pack(side=tk.LEFT, padx=5)
            channel_var = tk.IntVar(value=device.channel)
            channel_entry = ttk.Spinbox(channel_frame, from_=1, to=999, textvariable=channel_var, width=5)
            channel_entry.pack(side=tk.LEFT)
            
            channel_btn = ttk.Button(channel_frame, text="Change", 
                                    command=lambda: self.update_device_channel(device_idx, channel_var.get()))
            channel_btn.pack(side=tk.LEFT, padx=5)
            
        elif device_type == "SmartAirFryer":
            # Cook mode control
            ttk.Label(info_frame, text=f"Current Mode: {device.cook_mode}").pack(pady=5)
            
            mode_frame = ttk.Frame(info_frame)
            mode_frame.pack(pady=5)
            
            ttk.Label(mode_frame, text="Change Mode:").pack(side=tk.LEFT, padx=5)
            mode_var = tk.StringVar(value=device.cook_mode)
            mode_combo = ttk.Combobox(mode_frame, textvariable=mode_var, values=["air_fry", "bake", "roast", "grill"],
                                     state="readonly", width=10)
            mode_combo.pack(side=tk.LEFT)
            
            mode_btn = ttk.Button(mode_frame, text="Change", 
                                 command=lambda: self.update_device_mode(device_idx, mode_var.get()))
            mode_btn.pack(side=tk.LEFT, padx=5)
    
    def clear_device_controls(self):
        """Clear all device control widgets."""
        for widget in self.device_info_frame.winfo_children():
            widget.destroy()
    
    def toggle_device(self, device_idx, status_var):
        """Toggle the selected device on/off."""
        try:
            self.current_home.toggle_device(device_idx)
            device = self.current_home.get_device(device_idx)
            status = "ON" if device.switched_on else "OFF"
            status_var.set(f"Status: {status}")
            self.update_device_list()
            self.status_var.set(f"Toggled device {device_idx+1}")
            self.save_data()
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def update_device_rate(self, device_idx, rate):
        """Update consumption rate for SmartPlug."""
        try:
            self.current_home.update_option(device_idx, rate)
            self.status_var.set(f"Updated consumption rate to {rate}")
            # Refresh the device controls to show new value
            self.on_device_selected(None)
            self.save_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_device_channel(self, device_idx, channel):
        """Update channel for SmartTV."""
        try:
            self.current_home.update_option(device_idx, channel)
            self.status_var.set(f"Changed channel to {channel}")
            # Refresh the device controls to show new value
            self.on_device_selected(None)
            self.save_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_device_mode(self, device_idx, mode):
        """Update cook mode for SmartAirFryer."""
        try:
            self.current_home.update_option(device_idx, mode)
            self.status_var.set(f"Changed cook mode to {mode}")
            # Refresh the device controls to show new value
            self.on_device_selected(None)
            self.save_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def switch_all_on(self):
        """Turn all devices on."""
        if not self.current_home:
            return
        
        self.current_home.switch_all_on()
        self.update_device_list()
        # Refresh device controls if a device is selected
        self.on_device_selected(None)
        self.status_var.set("All devices turned ON")
        self.save_data()
    
    def switch_all_off(self):
        """Turn all devices off."""
        if not self.current_home:
            return
        
        self.current_home.switch_all_off()
        self.update_device_list()
        # Refresh device controls if a device is selected
        self.on_device_selected(None)
        self.status_var.set("All devices turned OFF")
        self.save_data()
    
    def serialize_homes(self):
        """Serialize all homes to a dictionary for JSON storage."""
        homes_data = {}
        
        for name, home in self.homes.items():
            devices_data = []
            
            for i in range(len(home._devices)):
                device = home.get_device(i)
                device_type = type(device).__name__
                device_data = {
                    "type": device_type,
                    "switched_on": device.switched_on
                }
                
                # Add device-specific attributes
                if device_type == "SmartPlug":
                    device_data["consumption_rate"] = device.consumption_rate
                elif device_type == "SmartTV":
                    device_data["channel"] = device.channel
                elif device_type == "SmartAirFryer":
                    device_data["cook_mode"] = device.cook_mode
                
                devices_data.append(device_data)
            
            homes_data[name] = {
                "max_items": home._max_items,
                "devices": devices_data
            }
        
        return homes_data
    
    def deserialize_homes(self, data):
        """Create SmartHome instances from JSON data."""
        homes = {}
        
        for name, home_data in data.items():
            max_items = home_data.get("max_items", 10)
            home = SmartHome(max_items=max_items)
            
            for device_data in home_data.get("devices", []):
                device_type = device_data.get("type")
                
                if device_type == "SmartPlug":
                    device = SmartPlug(device_data.get("consumption_rate", 50))
                elif device_type == "SmartTV":
                    device = SmartTV()
                    device.channel = device_data.get("channel", 1)
                elif device_type == "SmartAirFryer":
                    device = SmartAirFryer()
                    device.cook_mode = device_data.get("cook_mode", "air_fry")
                else:
                    continue
                
                if device_data.get("switched_on", False) != device.switched_on:
                    device.toggle_switch()
                
                try:
                    home.add_device(device)
                except ValueError:
                    # Skip if max devices reached
                    pass
            
            homes[name] = home
        
        return homes
    
    def save_data(self):
        """Save all homes data to a JSON file."""
        try:
            homes_data = self.serialize_homes()
            
            with open(self.data_file, 'w') as f:
                json.dump(homes_data, f, indent=2)
                
            self.status_var.set(f"Data saved to {self.data_file}")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
            return False
    
    def load_data(self):
        """Load homes data from JSON file if it exists."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            self.homes = self.deserialize_homes(data)
            
            if self.homes:
                first_home = next(iter(self.homes.keys()))
                self.current_home_name.set(first_home)
                self.current_home = self.homes[first_home]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

def main():
    root = tk.Tk()
    app = SmartHomesApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: quit_app(app, root))
    root.mainloop()

def quit_app(app, root):
    """Save data and quit the application."""
    if app.save_data():
        root.destroy()

if __name__ == "__main__":
    main()