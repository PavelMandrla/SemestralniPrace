from settings import settings
from motor import Motor
from camera import Camera
from time import sleep


class Scanner(object):

    def __init__(self):
        tt_settings = settings['turn_table']
        arm_settings = settings['arm']

        self.turn_table = Motor(
            tt_settings['dir_pin'],
            tt_settings['step_pin'],
            tt_settings['spr'],
            tt_settings['delay'],
            tt_settings['ramp'],
            tt_settings['acc'],
            tt_settings['gear_ratio']
            )
        self.arm = Motor(
            arm_settings['dir_pin'],
            arm_settings['step_pin'],
            arm_settings['spr'],
            arm_settings['delay'],
            arm_settings['ramp'],
            tt_settings['acc'],
            tt_settings['gear_ratio']
            )
        self.camera = Camera()

    def turn_table_routine(self):
        turn_table_step = 360 / settings["turn_table_positions"]
        for x in range(settings["turn_table_positions"]):
            self.turn_table.turn(turn_table_step)
            self.camera.capture("../hello.png")
            sleep(1)

    def scan(self):
        arm_step = settings["arm_angle"] / (settings["arm_positions"]-1)
        self.arm.turn(-settings["arm_angle"]/2)
        self.turn_table_routine()
        for x in range(settings["arm_positions"]-1):
            self.arm.turn(arm_step)
            self.turn_table_routine()
        self.arm.turn(-settings["arm_angle"]/2)
