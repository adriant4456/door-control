import pigpio

#init GPIO 
pi = pigpio.pi()

#set servo pin
active_pin = 2

def lock_status():
    pw = pigpio.get_servo_pulsewidth(active_pin)
    if pw = 500:
        return 'locked'
    elif pw = 2500:
        return ' unlocked'
    else:
        raise RuntimeError
        
def servo_unlock():
    pigpio.set_servo_pulsewidth(active_pin, 2500)

def servo_lock():
    pigpio.set_servo_pulsewidth(active_pin, 500)
