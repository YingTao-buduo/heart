import cv2
import numpy as np


def get_hsv_data(frames):
    data = []
    print('Begin rgb2hsv')
    for frame in frames:
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        s = sum(map(sum, hsv_img[:, :, 0]))
        print(s)
        data.append(s)
    print('HSV OK')
    return data
