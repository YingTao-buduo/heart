import cv2


def get_hsv_data(frames):
    data = []
    print('Begin rgb2hsv')
    for frame in frames:
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        s = sum(map(sum, hsv_img[:, :, 0]))
        data.append(s)
    print('HSV OK')
    return data
