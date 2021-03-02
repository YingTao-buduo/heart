import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
from math import *

cap = cv2.VideoCapture('C:/Users/YT-Laptop/Downloads/C18.mp4')  # 文件名及格式
count = 1
data = list()
while True:
    try:
        # capture frame-by-frame
        ret, frame = cap.read()
        # our operation on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        b, g, r = cv2.split(frame)

        # display the result
        #   ing frame
        print(str(count) + '--' + str(sum(sum(g))))
        data.append(sum(sum(g)))
        count = count + 1
        cv2.imshow('g', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
            break
    except:
        break
# when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
print('ok')
plt.plot(data)
plt.ylabel('some numbers')
plt.show()

