import cv2
import numba_sum


def get_red_data(frames):
    data = []
    print('Begin to read red')
    for frame in frames:
        b, g, r = cv2.split(frame)
        r = r.reshape(1, -1)
        data.append(numba_sum.nb_sum(r))
    print('Red OK')
    return data
