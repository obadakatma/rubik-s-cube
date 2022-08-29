import cv2 as cv
import time
import win32api

import HSV_filtering as hf
import three_by_three_cube_place as tp

capture = cv.VideoCapture(0)
while True:
    _, frame = capture.read()

    hsv = hf.Hsv()
    main_frame = hsv.processing(hsv, frame)
    three = tp.three(frame)

    three.rec_place(frame)
    sigma = three.standard_deviation(main_frame)
    cv.imshow("main", main_frame)
    cv.imshow("frame", frame)
    if win32api.GetKeyState(0x01) < 0:
        time.sleep(0.5)
        three.centers(hsv.get_hsv())
        print(three.h)
        print(sigma)

    if cv.waitKey(32) & 0xFF == ord(' '):
        break
