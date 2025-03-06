from smart_home_app import SmartHomeApp
import tkinter as tk

def test_smart_home_system():
    try:
        root = tk.Tk()
        app = SmartHomeApp(root)
        print("GUI opened successfully.")
        root.mainloop()
    except Exception as e:
        print("Error encountered:", e)

test_smart_home_system()
