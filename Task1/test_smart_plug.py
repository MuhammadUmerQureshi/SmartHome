from smart_plug import SmartPlug

def test_smart_plug():
    try:
        plug = SmartPlug(45)
        print(plug)  
        
        plug.toggle_switch()
        print(plug) 
        
        plug.set_consumption_rate(75)
        print(plug)
        
        plug.toggle_switch()
        print(plug)
        
        # Testing invalid values
        try:
            plug.set_consumption_rate(-10) 
        except ValueError as e:
            print("Error:", e)
        
        try:
            plug.set_consumption_rate(200)
        except ValueError as e:
            print("Error:", e)
        
        # Testing invalid initialization
        try:
            SmartPlug(-5)
        except ValueError as e:
            print("Error:", e)
        
        try:
            SmartPlug(160)
        except ValueError as e:
            print("Error:", e)
        
    except Exception as e:
        print("Unexpected error:", e)

    print(plug)

test_smart_plug()