import cv2
import numpy as np


def get_brightness_data(cap, data, count):
    while True:
        try:
            ret, frame = cap.read()
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


            img_shape = gray_img.shape
            height, width = img_shape[0], img_shape[1]
            size = gray_img.size

            hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

            # 计算灰度图像素点偏离均值(128)程序
            a = 0
            ma = 0
            reduce_matrix = np.full((height, width), 128)
            shift_value = gray_img - reduce_matrix
            shift_sum = sum(map(sum, shift_value))
            print(str(count) + '--' + str(shift_sum))
            data.append(shift_sum)
            #data.append(sum(map(sum, gray_img)))
            count = count + 1
        except BaseException as e:
            break
    print('brightness ok')
    return data
