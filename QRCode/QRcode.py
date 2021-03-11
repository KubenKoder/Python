import cv2 #read image / camera/video input
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)

cap.set(3, 1280) #3 = width
cap.set(4, 720) #4 = height

try:
    while True:
        success, frame = cap.read()

        for code in decode(frame):
            print(code.type)
            print(code.data.decode('utf-8'))
            time.sleep(5)
        cv2.imshow('code scanner', frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    print("closing program!")