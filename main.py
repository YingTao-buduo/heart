import cv2
import numpy as np
import matplotlib.pyplot as plt
import by_hsv
import fitter
import peak_counter
import heart_rate
import from_video
import by_brightness
import by_red
import filter
###################################################################################
# 从摄像头获取
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30, (600, 600))

cap_frames = []
f_count = 1
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True and f_count < 361:
        frame = cv2.flip(frame, 1)
        cap_frames.append(frame)
        cv2.imshow('frame', frame)
        f_count += 1
        if cv2.waitKey(1) & 0xFF == ord('1'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
###################################################################################
# 从文件获取
# cap = cv2.VideoCapture('C:/Users/YT-Laptop/Downloads/C10_1.mp4')
# data_from_video = from_video.get_brightness_data(cap)
# cap.release()
# cv2.destroyAllWindows()

###################################################################################
# 数据转换处理
data_red = by_red.get_red_data(cap_frames[30:330])
# data_brightness = by_brightness.get_brightness_data(cap_frames[30:330])
# data_hsv = by_hsv.get_hsv_data(cap_frames[30:330])
data_in = data_red

###################################################################################
# 数据校准处理
# 中值滤波
# data_hsv_filter = filter.median_average(data_hsv, 3)
# print(data_hsv_filter)
data_before_fit = np.array(data_in)
data_after_fit = np.array(fitter.fit(data_before_fit))

data_fixed = data_before_fit - data_after_fit



###################################################################################
# 计算波峰
data_heart_frame = peak_counter.count_peak(data_fixed)
# 计算心率和HRV
# hr = heart_rate.get_heart_rate(data_heart_frame, 30)
hrv_sdnn = heart_rate.get_heart_rate_variability(data_heart_frame, 30)


print('最小心率：' + str(hrv_sdnn[0]))
print('最大心率：' + str(hrv_sdnn[1]))
print('平均心率：' + str(hrv_sdnn[2]))
print('心率变异性：' + str(hrv_sdnn[3]))

plt.plot(data_fixed, label='Brightness')
# plt.plot(data_after_fit, label='after fit')
plt.ylabel('some data')
plt.show()
