import cv2
import numpy as np


def get_brightness_data(frames):
    data = []
    for frame in frames:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        img_shape = gray_img.shape
        height, width = img_shape[0], img_shape[1]

        reduce_matrix = np.full((height, width), 128)
        shift_value = gray_img - reduce_matrix
        shift_sum = sum(map(sum, shift_value))
        print(str(shift_sum))
        data.append(shift_sum)
    print('brightness ok')
    return data
