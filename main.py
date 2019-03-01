import RPi.GPIO as GPIO
import time

pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(7.5)
print("ready")

def degree_90():
    # 90 degree
    p.ChangeDutyCycle(7.5)
    time.sleep(1)    
    print("90 dgree (NEUTRAL)")

def degree_180():
    # 180 degree
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    print("180 degree")
    

def degree_0():
    # 0 degree
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    print("0 degree")
    
def repeat():
    degree_90()
    degree_0()
    degree_180()
    
def press_labtop_button():
    t = 0.2
    p.ChangeDutyCycle(5)
    print("completed step1")
    time.sleep(t)
    p.ChangeDutyCycle(10)
    print("completed step2")
    time.sleep(t)
    p.ChangeDutyCycle(5)
    print("completed step3")
    time.sleep(t)
    
    print()
    print("succeed pressing button")


try:
    
    press_labtop_button()

    
    p.stop()

    GPIO.cleanup()


except KeyboardInterrupt:
    p.stop()

    GPIO.cleanup()
