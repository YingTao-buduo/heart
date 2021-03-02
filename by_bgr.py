import cv2


def get_b_g_r_data(cap, data, count):
    while True:
        try:
            ret, frame = cap.read()
            b, g, r = cv2.split(frame)
            print(str(count) + '--' + str(sum(sum(r))))
            data.append(sum(sum(r)))
            count = count + 1
        except BaseException:
            break

    print('bgr OK')
    return data

