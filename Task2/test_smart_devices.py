# My student ID is 2247637.
# Unique Last Digits:3,7
# Classes to implement: SmartTV, SmartWashingMachine

from smart_devices import SmartTV, SmartWashingMachine

def test_smart_tv():
    try:
        tv = SmartTV()
        print(tv)  
        
        tv.toggle_switch()
        print(tv)  
        
        tv.set_channel(100)
        print(tv)  
        
        try:
            tv.set_channel(800) 
        except ValueError as e:
            print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)


def test_smart_washing_machine():
    try:
        washer = SmartWashingMachine()
        print(washer)  
        
        washer.toggle_switch()
        print(washer)  
        
        washer.set_wash_mode("Eco")
        print(washer) 
        
        try:
            washer.set_wash_mode("Heavy wash")  # Should raise an exception
        except ValueError as e:
            print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

test_smart_tv()
test_smart_washing_machine()