import cv2
import numpy as np
import matplotlib.pyplot as plt
import by_hsv
import fitter
import peak_counter
import heart_rate

cap = cv2.VideoCapture('C:/Users/YT-Laptop/Downloads/C10_2.mp4')
count = 0
data = []

# data_bgr = by_bgr.get_b_g_r_data(cap, data, count)
# data_gray = by_brightness.get_brightness_data(cap, data, count)
data_hsv = by_hsv.get_hsv_data(cap, data)

data_before_fit = np.array(data_hsv)
data_after_fit = np.array(fitter.fit(data_before_fit))


data_fixed = data_before_fit - data_after_fit

data_heart_frame = peak_counter.count_peak(data_fixed)
print(data_heart_frame)
hr = heart_rate.get_heart_rate(data_heart_frame, 30)
print('心率：' + str(hr))

# 中值滤波
# data_1 = filter.median_average(np.array(data_0), 3)

cap.release()
cv2.destroyAllWindows()

plt.plot(data_fixed)
plt.ylabel('some data')
plt.show()
