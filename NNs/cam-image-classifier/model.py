from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL

class Model:
    def __init__(self):
        self.model = LinearSVC()
        self.trained = False

    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])
        for i in range (1, counters[0]):
            img = cv.imread(f"1/frame{i}.jpeg")[:,:,0]
            img = img.reshape(16800) # flattening the image
            img_list = np.append(img_list, img)
            class_list = np.append(class_list, 1)

        for i in range (1, counters[1]):
            img = cv.imread(f"2/frame{i}.jpeg")[:,:,0]
            img = img.reshape(16800) # flattening the image
            img_list = np.append(img_list, img)
            class_list = np.append(class_list, 2)

        img_list = img_list.reshape(counters[0] - 1 + counters[1] - 1, 16800) # reshaping the image list to be of shape (n_samples, n_features)
        self.model.fit(img_list, class_list)
        print("Model trained successfully")

    def predict(self, frame):
        frame = frame[1]
        cv.imwrite("frame.jpeg", cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = PIL.Image.open("frame.jpeg")
        img.thumbnail((150, 150), PIL.Image.ANTIALIAS)
        img.save("frame.jpeg")

        img = cv.imread('frame.jpeg')[:, :, 0]
        img = img.reshape(16800)
        prediction = self.model.predict([img])

        return prediction[0]