import cv2
import numpy as np


def get_red_data(frames):
    data = []
    print('Begin to read red')
    for frame in frames:
        b, g, r = cv2.split(frame)
        data.append(sum(map(sum, r)))
    print('Red OK')
    return data
