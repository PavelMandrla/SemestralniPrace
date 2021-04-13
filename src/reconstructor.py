import os
from settings import settings


def addExifs():
    os.chdir(settings['current_save_dir'])
    os.system('mm3d SetExif ".*png" F=3.04 F35=196 Cam="Camera Module v2"')


def reconstruct():
    addExifs()
