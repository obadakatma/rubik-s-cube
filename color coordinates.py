import cv2 as cv
import time
import win32api

import HSV_filtering as hf
import three_by_three_cube_place as cp

in_array = [[], [], [],
            [], [], [],
            [], [], []]

out_array = [[], [], [],
             [], [], [],
             [], [], []]

capture = cv.VideoCapture(0)
while True:
    _, frame = capture.read()

    flip = cv.flip(frame, 1)

    obj = cp.place()
    obj2 = hf.Hsv()

    main_frame = hf.Hsv.processing(flip)

    rec = cp.place.rec_place(main_frame)
    centers = cp.place.centers(main_frame, in_array)

    final_frame = hf.Hsv.show(main_frame)

    if win32api.GetKeyState(0x01) < 0:
        time.sleep(0.5)
        values = cp.place.print_values(in_array, out_array)

    if cv.waitKey(32) & 0xFF == ord(' '):
        break

