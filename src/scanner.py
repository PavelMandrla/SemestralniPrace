from settings import settings
from motor import Motor
from camera import Camera
from time import sleep
from datetime import datetime
import os


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

    def get_save_dir(self):
        now = datetime.now()
        candidate_dir = settings["save_dir"] + now.strftime("scan_%d.%m.%Y_%H:%M")

        if os.path.exists(candidate_dir):
            i = 1
            candidate_dir += candidate_dir + "_%s"
            while os.path.exists(candidate_dir % (i)):
                i += 1
            candidate_dir = candidate_dir % (i)

        os.makedirs(candidate_dir)
        return candidate_dir

    def turn_table_routine(self):
        turn_table_step = 360 / settings["turn_table_positions"]
        for x in range(settings["turn_table_positions"]):
            self.turn_table.turn(turn_table_step)

            #try:
            self.camera.capture("%s/%d.png" % (self.result_dir, self.frame_num))
            #except:
                #print("camera problem")
            self.frame_num += 1
            sleep(1)

    def scan(self):
        self.camera = Camera()
        self.frame_num = 0
        self.result_dir = self.get_save_dir()
        settings['current_save_dir'] = self.result_dir

        arm_step = settings["arm_angle"] / (settings["arm_positions"]-1)
        self.arm.turn(-settings["arm_angle"]/2)
        self.turn_table_routine()
        for x in range(settings["arm_positions"]-1):
            self.arm.turn(arm_step)
            self.turn_table_routine()
        self.arm.turn(-settings["arm_angle"]/2)

        #self.camera.capture('test.png')

        self.camera.release_camera()
        self.camera = 0
