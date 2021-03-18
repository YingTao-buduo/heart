import cv2
import numpy as np


def get_hsv_data(cap, data):
    print('Begin rgb2hsv')
    while True:
        try:
            ret, frame = cap.read()
            if frame is not None:
                hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                s = sum(map(sum, hsv_img[:, :, 0]))
                # print(s)
                data.append(s)
            else:
                break
        except Exception as e:
            print(e)
            break
    print('HSV OK')
    return data
