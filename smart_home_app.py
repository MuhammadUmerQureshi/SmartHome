import tkinter as tk
from tkinter import ttk, messagebox
from smart_home import SmartHome
from smart_plug import SmartPlug
# Import the two custom device classes based on your student number
# For this example, I'll use SmartLight and SmartFridge
from smart_device import SmartLight, SmartFridge


class SmartHomeApp:
    """
    A graphical user interface for managing a smart home.
    """
    
    def __init__(self, root):
        """
        Initialize the SmartHomeApp with a Tkinter root window.
        
        Args:
            root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Smart Home App")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Initialize the SmartHome instance
        self.smart_home = SmartHome()
        
        # Add default devices (customize based on your student number)
        self.setup_default_devices()
        
        # Print the SmartHome to console for testing
        print(self.smart_home)
        
        # Create the GUI layout
        self.create_widgets()
    
    def setup_default_devices(self):
        """Set up default devices for the SmartHome."""
        # Add a SmartPlug with default consumption rate
        plug = SmartPlug(45)
        self.smart_home.add_device(plug)
        
        # Add custom devices based on student number
        # For this example, I'll use SmartLight and SmartFridge
        # Replace with your own custom devices based on your student number
        light = SmartLight()
        fridge = SmartFridge()
        
        self.smart_home.add_device(light)
        self.smart_home.add_device(fridge)
    
    def create_widgets(self):
        """Create the widgets for the SmartHomeApp GUI."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Smart Home Control Panel", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=5, pady=10)
        
        # Global control buttons
        control_frame = ttk.LabelFrame(main_frame, text="Global Controls", padding="10")
        control_frame.grid(row=1, column=0, columnspan=5, sticky="ew", padx=5, pady=5)
        
        # Turn all on button
        on_button = ttk.Button(control_frame, text="Turn On All")
        on_button.pack(side=tk.LEFT, padx=5)
        
        # Turn all off button
        off_button = ttk.Button(control_frame, text="Turn Off All")
        off_button.pack(side=tk.LEFT, padx=5)
        
        # Add device button
        add_button = ttk.Button(control_frame, text="Add Device")
        add_button.pack(side=tk.RIGHT, padx=5)
        
        # Devices list frame
        devices_frame = ttk.LabelFrame(main_frame, text="Devices", padding="10")
        devices_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Create a canvas with scrollbar for device list
        canvas = tk.Canvas(devices_frame)
        scrollbar = ttk.Scrollbar(devices_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Display devices
        headers = ["Device", "Type", "Status", "Controls"]
        for i, header in enumerate(headers):
            label = ttk.Label(scrollable_frame, text=header, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5)
        
        for row, device in enumerate(self.smart_home.devices, start=1):
            name_label = ttk.Label(scrollable_frame, text=device.name)
            name_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
            
            type_label = ttk.Label(scrollable_frame, text=type(device).__name__)
            type_label.grid(row=row, column=1, padx=5, pady=5, sticky="w")
            
            status_label = ttk.Label(scrollable_frame, text=device.status)
            status_label.grid(row=row, column=2, padx=5, pady=5, sticky="w")
            
            control_button = ttk.Button(scrollable_frame, text="Control")
            control_button.grid(row=row, column=3, padx=5, pady=5)
    
def test_smart_home_system():
    """Test function to verify devices initialization and GUI display."""
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    test_smart_home_system()