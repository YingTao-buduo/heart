import cv2
import numpy as np


def get_brightness_data(cap):
    data = []
    while True:
        try:
            ret, frame = cap.read()
            if frame is not None:
                # gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #
                # img_shape = gray_img.shape
                # height, width = img_shape[0], img_shape[1]
                #
                # reduce_matrix = np.full((height, width), 128)
                # shift_value = gray_img - reduce_matrix
                # shift_sum = sum(map(sum, shift_value))
                # print(str(shift_sum))
                # data.append(shift_sum)

                b, g, r = cv2.split(frame)
                print(r)
                data.append(sum(map(sum, r)))
            else:
                break
        except Exception as e:
            print(e)
            break

    print('bgr OK')
    return data
