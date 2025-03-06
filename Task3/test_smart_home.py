from smart_home import SmartHome
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Task2')))

from smart_plug import SmartPlug
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
        print("---------- Initial state ----------")
        print(home)  
        
        print("---------- Using get_devices ----------")
        for i in range(home.max_items):
            print(home.get_device(i))

        print("---------- Using toggle_device ----------")
        home.toggle_device(0)
        home.toggle_device(1)
        print(home)  
        print("---------- Using switch_all_on ----------")
        home.switch_all_on()
        print(home)
        print("---------- Using switch_all_off ----------")
        home.switch_all_off()
        print(home)  
        print("---------- Using update_option ----------")
        home.update_option(0, 60)  
        home.update_option(1, 50)  
        home.update_option(2, "Quick wash")  
        print(home)  
        
        print("---------- Testing exceptions ----------")
        try:
            home.add_device(SmartPlug(90))  
        except ValueError as e:
            print("Error:", e)
        
        home.remove_device(1)  
        print(home)  
        
        try:
            home.update_option(5, 100)  
        except IndexError as e:
            print("Error:", e)
        
    except Exception as e:
        print("Unexpected error:", e)

test_smart_home()
