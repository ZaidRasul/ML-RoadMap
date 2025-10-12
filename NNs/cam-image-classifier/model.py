from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL

class Model:
    def __init__(self):
        self.model = LinearSVC()
        self.trained = False

    def train_model(self):
        pass        