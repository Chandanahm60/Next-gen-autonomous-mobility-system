import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# IR sensor pins
IR_LEFT = 5
IR_RIGHT = 6

# Ultrasonic sensor pins
TRIG = 18
ECHO = 24

# Setup pins
GPIO.setup(IR_LEFT, GPIO.IN)
GPIO.setup(IR_RIGHT, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_lane_status():
    """Returns (left sensor, right sensor)"""
    left = GPIO.input(IR_LEFT)
    right = GPIO.input(IR_RIGHT)
    return left, right


def get_distance():
    """Returns distance in cm"""

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    end = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    duration = end - start
    distance = (duration * 34300) / 2

    return distance
