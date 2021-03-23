import cv2
import numpy as np
import numba_sum


def get_brightness_data(frames):
    data = []
    print('Begin to read brightness')
    for frame in frames:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_img = gray_img.reshape(1, -1)
        shift_mean_sum = numba_sum.nb_sum(gray_img[0])
        data.append(shift_mean_sum)
    print('Brightness OK')
    return data
