from settings import settings
import cv2
import threading
import time


# Other thread continuously reads frames from camera to work around buffer
class CameraBufferCleanerThread(threading.Thread):

    def __init__(self, cap, name='camera-buffer-cleaner-thread'):
        self.cap = cap
        self.running = True
        self.last_frame = None
        super(CameraBufferCleanerThread, self).__init__(name=name)
        self.start()

        print("starting camera")
        time.sleep(1)

    def run(self):
        while self.running:
            ret, self.last_frame = self.cap.read()
        print("stopping capture")
        self.cap.release()


class Camera:

    def get_gstreamer_pipeline(self):
        camera_settings = settings['camera']

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

    def __init__(self):
        cap = cv2.VideoCapture(self.get_gstreamer_pipeline(), cv2.CAP_GSTREAMER)
        if not cap.isOpened():
            raise Exception("Could not open camera, while creating the camera object.")
        self.capCleaner = CameraBufferCleanerThread(cap)

    def release_camera(self):
        self.capCleaner.running = False

    def capture(self, filepath):
        cv2.imwrite(filepath, self.capCleaner.last_frame)
