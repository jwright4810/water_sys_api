import RPi.GPIO as GPIO

def valve_controller(action):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(4, GPIO.OUT)

    if action == 'off':
        GPIO.output(4, GPIO.LOW)
        print('valve should be off') 
    elif action == 'on':
        GPIO.output(4, GPIO.HIGH)
        print('valve should be on')

    GPIO.cleanup()

def valve_status():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(4, GPIO.OUT)
    
    if GPIO.input(4) == 1:
        return 'on'
    else:
        return 'off'

    GPIO.cleanup()

 
    
    