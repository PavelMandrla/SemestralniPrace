import os
from settings import settings


def addExifs():
    print("adding exif to scanned images")

    os.system('mm3d SetExif ".*png" F=3.04 F35=196 Cam="Camera Module v2"')

def computeTiePoints():
    print("computing tie points")
    os.system('mm3d Tapioca MulScale ".*png" 500 2000')

def reconstruct():
    # GO TO DIR WITH SCANNED IMAGES
    os.chdir(settings['current_save_dir'])

    addExifs()
    computeTiePoints()
