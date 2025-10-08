import cv2 as cv
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(training_images, training_labels), (test_images, test_labels) = datasets.cifar10.load_data()
training_images, test_images = training_images / 255, test_images / 255
