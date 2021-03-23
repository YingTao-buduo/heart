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
import sys


###################################################################################
# parameters
fromWhere = 0    # 0: from camera, 1: from file
mode = 0          # 0: brightness, 1: from red channel, 2: from h of hsv
fps = 30           # device's fps
filename = 'C:/Users/YT-Laptop/Downloads/HRV/C10_2.mp4'     # video filename

###################################################################################
# choose from where
cap_frames = []
if fromWhere == 0:
    # from camera
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (150, 150))
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
else:
    # from file
    cap = cv2.VideoCapture(filename)
    cap_frames = from_video.get_video_frames(cap)
    cap.release()
    cv2.destroyAllWindows()

###################################################################################
# data processing
data_before_fit = []
if mode == 0:
    data_before_fit = by_brightness.get_brightness_data(cap_frames[30:330])
elif mode == 1:
    data_before_fit = by_red.get_red_data(cap_frames[30:330])
elif mode == 2:
    data_before_fit = by_hsv.get_hsv_data(cap_frames[30:330])

###################################################################################
# MedianAverageFilter
# data_hsv_filter = filter.median_average(data_hsv, 3)
# print(data_hsv_filter)
data_after_fit = np.array(fitter.fit(data_before_fit))
data_fixed = data_before_fit - data_after_fit

###################################################################################
# count peak
data_heart_frame = peak_counter.count_peak(data_fixed)
# calculate hrv
# hr = heart_rate.get_heart_rate(data_heart_frame, 30)
hrv_sdnn = heart_rate.get_heart_rate_variability(data_heart_frame, fps)

print('Minimum heart rate: ' + str(hrv_sdnn[0]))
print('Maximum heart rate: ' + str(hrv_sdnn[1]))
print('Average heart rate: ' + str(hrv_sdnn[2]))
print('Heart rate variability: ' + str(hrv_sdnn[3]))

plt.plot(data_fixed)
plt.show()
