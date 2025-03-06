# test_smart_home.py
from smart_home import SmartHome
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2')))
from smartplug import SmartPlug
from smart_devices import SmartTV    
from smart_devices import SmartWashingMachine
def test_smart_home():
    try:
        home = SmartHome(max_items=3)
        plug = SmartPlug(45)
        tv = SmartTV()
        washer = SmartWashingMachine()
        
        home.add_device(plug)
        home.add_device(tv)
        home.add_device(washer)
        
        print(home)  # Check initial state
        
        home.toggle_device(0)
        home.toggle_device(1)
        print(home)  # Check after toggling devices
        
        home.switch_all_off()
        print(home)  # Check if all devices turned off
        
        home.update_option(0, 60)  # Update SmartPlug consumption rate
        home.update_option(1, 50)  # Update SmartTV channel
        home.update_option(2, "Quick wash")  # Update SmartWashingMachine mode
        print(home)  # Check updated values
        
        try:
            home.add_device(SmartPlug(90))  # Should raise an exception (max limit reached)
        except ValueError as e:
            print("Error caught:", e)
        
        home.remove_device(1)  # Remove SmartTV
        print(home)  # Check after removal
        
        try:
            home.update_option(5, 100)  # Invalid index test
        except IndexError as e:
            print("Error caught:", e)
        
    except Exception as e:
        print("Unexpected error:", e)

# Run the test function
test_smart_home()
