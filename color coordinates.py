import time
import numpy as np
import cv2 as cv
import win32api

import cube_place as cp

color_arr = [[], [], [],
             [], [], [],
             [], [], []]

counter = 1
capture = cv.VideoCapture(1)
while True:
    _, frame = capture.read()
    flip = cv.flip(frame, 1)

    hsv = cv.cvtColor(flip, cv.COLOR_BGR2HSV)
    blur = cv.GaussianBlur(flip, (5, 5), 0)
    canny = cv.Canny(blur, threshold1=130, threshold2=200)

    # red : hue / saturation /value of brightness
    low_red = np.array([155, 100, 100])
    high_red = np.array([180, 170, 255])
    red_mask = cv.inRange(hsv, low_red, high_red)
    kernal = np.ones((3, 3), np.uint8)
    red_mask = cv.erode(red_mask, kernal)
    red = cv.bitwise_and(flip, flip, mask=red_mask)
    obj = cp.place()
    rec = cp.place.rec_place(red)
    cv.imshow("red", red)

    state_left = win32api.GetKeyState(0x01)
    a = win32api.GetKeyState(0x01)

    if state_left == a and counter == 1:

        if a < 0:
            print("clicked 1")
            time.sleep(0.5)
            color_arr[0] = list(red[red.shape[0] // 2 - 150, red.shape[1] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 2:

        if a < 0:
            print("clicked 2")
            time.sleep(0.5)
            color_arr[1] = list(red[red.shape[0] // 2 - 150, red.shape[1] // 2])
            counter = counter + 1
    elif state_left == a and counter == 3:

        if a < 0:
            print("clicked 3")
            time.sleep(0.5)
            color_arr[2] = list(red[red.shape[0] // 2 - 150, red.shape[1] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 4:

        if a < 0:
            print("clicked 4")
            time.sleep(0.5)
            color_arr[3] = list(red[red.shape[0] // 2, red.shape[1] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 5:

        if a < 0:
            print("clicked 5")
            time.sleep(0.5)
            color_arr[4] = list(red[red.shape[0] // 2, red.shape[1] // 2])
            counter = counter + 1
    elif state_left == a and counter == 6:

        if a < 0:
            print("clicked 6")
            time.sleep(0.5)
            color_arr[5] = list(red[red.shape[0] // 2, red.shape[1] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 7:

        if a < 0:
            print("clicked 7")
            time.sleep(0.5)
            color_arr[6] = list(red[red.shape[0] // 2 + 150, red.shape[1] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 8:

        if a < 0:
            print("clicked 8")
            time.sleep(0.5)
            color_arr[7] = list(red[red.shape[0] // 2 + 150, red.shape[1] // 2])
            counter = counter + 1
    elif state_left == a and counter == 9:

        if a < 0:
            print("clicked 9")
            time.sleep(0.5)
            color_arr[8] = list(red[red.shape[0] // 2 + 150, red.shape[1] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 10:

        if a < 0:
            for lis in color_arr:
                print(lis[::-1])
            counter = 1
            break

    if cv.waitKey(20) & 0xFF == ord(' '):
        break

cv.waitKey(0)
cv.destroyAllWindows()
