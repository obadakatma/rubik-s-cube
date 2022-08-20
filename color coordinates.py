import cv2 as cv
import win32api

import cube_place as cp

color_arr = [[], [], [],
             [], [], [],
             [], [], []]

counter = 1
capture = cv.VideoCapture(0)
while True:
    _, frame = capture.read()
    flip = cv.flip(frame, 1)
    obj = cp.place()
    rec = cp.place.rec_place(flip)
    cv.imshow('Video', flip)
    state_left = win32api.GetKeyState(0x01)
    a = win32api.GetKeyState(0x01)

    if state_left == a and counter == 1:

        if a < 0:
            print("clicked 1")
            color_arr[0] = list(flip[flip.shape[1] // 2 - 150, flip.shape[0] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 2:

        if a < 0:
            print("clicked 2")
            color_arr[1] = list(flip[flip.shape[1] // 2, flip.shape[0] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 3:

        if a < 0:
            print("clicked 3")
            color_arr[2] = list(flip[flip.shape[1] // 2 + 150, flip.shape[0] // 2 - 150])
            counter = counter + 1
    elif state_left == a and counter == 4:

        if a < 0:
            print("clicked 4")
            color_arr[3] = list(flip[flip.shape[1] // 2 - 150, flip.shape[0] // 2])
            counter = counter + 1
    elif state_left == a and counter == 5:

        if a < 0:
            print("clicked 5")
            color_arr[4] = list(flip[flip.shape[1] // 2, flip.shape[0] // 2])
            counter = counter + 1
    elif state_left == a and counter == 6:

        if a < 0:
            print("clicked 6")
            color_arr[5] = list(flip[flip.shape[1] // 2 + 150, flip.shape[0] // 2])
            counter = counter + 1
    elif state_left == a and counter == 7:

        if a < 0:
            print("clicked 7")
            color_arr[6] = list(flip[flip.shape[1] // 2 - 150, flip.shape[0] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 8:

        if a < 0:
            print("clicked 8")
            color_arr[7] = list(flip[flip.shape[1] // 2, flip.shape[0] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 9:

        if a < 0:
            print("clicked 9")
            color_arr[8] = list(flip[flip.shape[1] // 2 + 150, flip.shape[0] // 2 + 150])
            counter = counter + 1
    elif state_left == a and counter == 10:

        if a < 0:
            print(color_arr)
            counter = 1
            break

    if cv.waitKey(20) & 0xFF == ord(' '):
        break

cv.waitKey(0)
cv.destroyAllWindows()
