from settings import settings
import numpy as np
import cv2


class Camera:

    def get_gstreamer_pipeline(self):
        camera_settings = settings['camera']
        print(camera_settings['capture_width'],
                camera_settings['capture_height'],
                camera_settings['framerate'],
                camera_settings['flip_method'],
                camera_settings['display_width'],
                camera_settings['display_height'])
        return (
            "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (camera_settings['capture_width'],
                camera_settings['capture_height'],
                camera_settings['framerate'],
                camera_settings['flip_method'],
                camera_settings['display_width'],
                camera_settings['display_height']
            )
        )

    '''
    def capture(self, filepath):
        cap = cv2.VideoCapture(self.get_gstreamer_pipeline(), cv2.CAP_GSTREAMER)
        if not self.cap.isOpened():
            raise Exception("Could not open camera.")
        ret, img = cap.read()
        cv2.imwrite(filepath, img)
        cap.release()

    '''

    def __init__(self):
        self.cap = cv2.VideoCapture(self.get_gstreamer_pipeline(), cv2.CAP_GSTREAMER)
        if not self.cap.isOpened():
            raise Exception("Could not open camera, while creating the camera object.")

    def release_camera(self):
        print("releasing")
        self.cap.release()
        print("released")

    def capture(self, filepath):
        if self.cap.isOpened():
            ret, img = self.cap.read()
            cv2.imwrite(filepath, img)
        else:
            raise Exception("Could not open camera, while creating the camera object.")
