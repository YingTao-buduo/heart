import cv2
import numpy as np
import matplotlib.pyplot as plt
import by_bgr
import by_brightness
import filter

cap = cv2.VideoCapture('C:/Users/YT-Laptop/Downloads/C18.mp4')  # 文件名及格式
count = 0
data = list()

# data = by_bgr.get_b_g_r_data(cap, data, count)
data = by_brightness.get_brightness_data(cap, data, count)

data_1 = filter.median_average(np.array(data), 3)

cap.release()
cv2.destroyAllWindows()

count_1 = list()
for i in range(0, 594):
    count_1.append(i)

plt.plot(data_1)
plt.ylabel('some numbers')
plt.show()
