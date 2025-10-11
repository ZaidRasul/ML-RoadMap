import cv2 as cv

class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Could not open video device")
        
    def __del__(self):# destructor to close the camera
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        pass
