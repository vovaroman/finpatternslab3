import cv2


class Cv2Colors:
    def __init__(self):
        self.flags = [i for i in dir(cv) if i.startswith('COLOR_')]



