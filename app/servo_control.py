import pigpio

#init GPIO 
pi = pigpio.pi()

#set servo pin
active_pin = 2

def lock_status():
    pw = pi.get_servo_pulsewidth(active_pin)
    if pw == 500:
        return 1
    elif pw == 2500:
        return 0
    else:
        raise RuntimeError
        
def servo_unlock():
    pi.set_servo_pulsewidth(active_pin, 2500)

def servo_lock():
    pi.set_servo_pulsewidth(active_pin, 500)
