import cv2
import numpy as np


def get_red_data(frames):
    data = []
    print('Red Begin')
    for frame in frames:
        b, g, r = cv2.split(frame)
        print(r)
        data.append(sum(map(sum, r)))
    print('Red OK')
    return data
