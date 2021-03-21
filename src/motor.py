from time import sleep
import Jetson.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self, dir_pin, step_pin, spr, delay, ramp, acc, gear_ratio):
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.spr = spr          # steps per rotation
        self.delay = delay
        self.ramp = ramp
        self.acc = acc
        self.gear_ratio = gear_ratio

        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)

    def turn(self, angle):
        step_count = int(angle * self.gear_ratio * self.spr/360)
        if step_count > 0:
            GPIO.output(self.dir_pin, GPIO.HIGH)
        if step_count < 0:
            GPIO.output(self.dir_pin, GPIO.LOW)
            step_count = -step_count
        for x in range(step_count):
            GPIO.output(self.step_pin, GPIO.HIGH)
            if x <= self.ramp and x <= step_count/2:
                delay = self.delay + (self.ramp - x) * self.delay / self.acc
            elif step_count - x <= self.ramp and x > step_count / 2:
                delay = self.delay + (self.ramp - step_count + x) * self.delay / self.acc
            sleep(delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(delay)
