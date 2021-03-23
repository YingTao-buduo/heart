import cv2
import numba_sum


def get_hsv_data(frames):
    data = []
    print('Begin rgb2hsv')
    for frame in frames:
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h = hsv_img[:, :, 0].reshape(1, -1)
        s = numba_sum.nb_sum(h)
        data.append(s)
    print('HSV OK')
    return data
