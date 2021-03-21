#from settings import ScannerSettings
from settings import settings
from motor import Motor
from camera import Camera
from scanner import Scanner

settings.load_settings("../settings.js")
scanner = Scanner()
scanner.scan()


'''
tt_settings = settings['turn_table']
arm_settings = settings['arm']
turn_table = Motor(
    tt_settings['dir_pin'],
    tt_settings['step_pin'],
    tt_settings['spr'],
    tt_settings['delay'],
    tt_settings['ramp'],
    tt_settings['acc'],
    tt_settings['gear_ratio']
    )

arm = Motor(
    arm_settings['dir_pin'],
    arm_settings['step_pin'],
    arm_settings['spr'],
    arm_settings['delay'],
    arm_settings['ramp'],
    tt_settings['acc'],
    tt_settings['gear_ratio']
    )

camera = Camera()

arm.turn(-30)
turn_table.turn(360)
camera.capture("../test.png")
turn_table.turn(-360)
arm.turn(-10)
'''
