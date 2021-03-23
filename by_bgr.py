import cv2


def get_b_g_r_data(cap, data, count):
    while True:
        try:
            ret, frame = cap.read()
            b, g, r = cv2.split(frame)
            data.append(sum(sum(r)))
            count = count + 1
        except Exception as e:
            print(e)
            break

    print('RGB OK')
    return data

