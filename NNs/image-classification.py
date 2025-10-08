import cv2 as cv
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Load and preprocess the CIFAR-10 dataset
(training_images, training_labels), (test_images, test_labels) = datasets.cifar10.load_data()
training_images, test_images = training_images / 255, test_images / 255

# classes or features
class_names = ['airplane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i][0]])

plt.show()

# smaller dataset for faster training
training_images = training_images[:20000]
training_labels = training_labels[:20000]
test_images = test_images[:4000]
test_labels = test_labels[:4000]

