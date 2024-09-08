import tkinter as tk
import time
import keyboard

try:
    import keyboard
except ImportError:
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "keyboard"])
    import keyboard

def start_typing():
    """Starts the typing process based on the GUI input."""
    text_to_type = text_entry.get()
    delay = float(delay_entry.get())
    initial_key = initial_key_entry.get()

    while True:
        if stop_flag.get():  # Check if the stop button was pressed
            break

        keyboard.press_and_release(initial_key)
        for char in text_to_type:
            keyboard.write(char)
            time.sleep(delay)
        keyboard.send('enter')
        time.sleep(0.1)

def stop_typing():
    """Sets the stop flag to True to stop the typing process."""
    stop_flag.set(True)

# Create the main window
window = tk.Tk()
window.title("Universal Chat Spammer")

# Text to type
text_label = tk.Label(window, text="Message to spam⬇️")
text_label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

# Delay between characters
delay_label = tk.Label(window, text="Delay between characters (seconds):")
delay_label.pack()
delay_entry = tk.Entry(window)
delay_entry.insert(0, "0.25")  # Default delay
delay_entry.pack()

# Initial key to press
initial_key_label = tk.Label(window, text="Key2EnterChat:")
initial_key_label.pack()
initial_key_entry = tk.Entry(window)
initial_key_entry.insert(0, "/")  # Default key
initial_key_entry.pack()

# Start and Stop buttons
stop_flag = tk.BooleanVar(value=False)
start_button = tk.Button(window, text="Start", command=start_typing)
start_button.pack()
stop_button = tk.Button(window, text="Stop", command=stop_typing)
stop_button.pack()

window.mainloop()
