import os
import socket
import time

import numpy as np

import FiveByFive as Five
import FourByFour as Four
import HSV_Filtering as Hsv
import ThreeByThree as Three
import ThreeByThreeCubeMoves as Move
from object_detector import *

# host, port = "127.0.0.1", 25001
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((host, port))


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


angle, box, box2, box3, rotated = 0, 0, 0, 0, 0
x, y, w, h = 0, 0, 0, 0
pt1 = (200, 116)
pt2 = (400, 316)
i = 0
capture = cv.VideoCapture(0)
capture.set(15, -5)
capture.set(10, 255)
capture.set(12, 255)
while True:
    _, frame = capture.read()
    cv.imshow('Main', frame)
    if i == 0:
        time.sleep(3)
        cv.imwrite(f"photos/{i}.png", frame)
        print("done0")
        i += 1
    elif i == 1:
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\leftMove.exe")
        time.sleep(6)
        cv.imwrite(f"photos/{i}.png", frame)
        print("done1")
        time.sleep(6)
        i += 1

    elif i == 2:
        cv.imwrite(f"photos/{i}.png", frame)
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove1.exe")
        print("done2")
        time.sleep(6)
        i += 1

    elif i == 3:
        cv.imwrite(f"photos/{i}.png", frame)
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove2.exe")
        print("done3")
        time.sleep(6)
        i += 1

    elif i == 4:
        cv.imwrite(f"photos/{i}.png", frame)
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove3.exe")
        print("done4")
        time.sleep(8)
        i += 1

    elif i == 5:
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove3.exe")
        time.sleep(8)
        cv.imwrite(f"photos/{i}.png", frame)
        os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\leftMove.exe")
        print("done5")
        time.sleep(6)
        i += 1

    elif i == 6:
        cv.imwrite(f"photos/{i}.png", frame)
        print("done6")
        i += 1

    elif i == 7:
        break
    # if cv.waitKey(32) & 0xFF == ord(' '):
    #     break
cv.destroyWindow("Main")
# ###############################################################################################################################
for i in range(1, 7):
    img = cv.imread(f"photos/{i}.png")

    frame = rotate(img, 90)
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    rectangle = cv.rectangle(blank.copy(), pt1, pt2, 255, -1)
    masked = cv.bitwise_and(frame, frame, mask=rectangle)

    detector = HomogeneousBgDetector()
    hsv = Hsv.Hsv()
    main_frame = hsv.processing(masked)
    contours = detector.detect_objects(main_frame)
    for cnt in contours:
        rect = cv.minAreaRect(cnt)
        print(rect[2])
        (x, y), (w, h), angle = rect
        # print(angle)
        box1 = cv.boxPoints(rect)
        box = np.int0(box1)
        # print(box)
        # cv.drawContours(img, [box], 0, (255, 0, 0), 2)
        if angle < 40:
            rotated = rotate(frame, angle)
        elif angle > 40:
            rotated = rotate(frame, angle - 90)

    blank = np.zeros(rotated.shape[:2], dtype='uint8')
    rectangle = cv.rectangle(blank.copy(), pt1, pt2, 255, -1)
    masked = cv.bitwise_and(rotated, rotated, mask=rectangle)
    hsv2 = Hsv.Hsv()
    main_frame2 = hsv2.processing(masked)
    contours2 = detector.detect_objects(main_frame2)
    for cnt in contours2:
        rect_test = cv.minAreaRect(cnt)
        (x_test, y_test), (w_test, h_test), angle_test = rect_test
        # print(angle)
        box2 = cv.boxPoints(rect_test)
        box3 = np.int0(box2)
    x, y, w, h = cv.boundingRect(box3)
    x2, y2 = x + w, y + h
    three = Three.Three(x, y, x2, y2)
    four = Four.Four(x, y, x2, y2)
    five = Five.Five(x, y, x2, y2)

    three.rec_place(rotated)
    # four.rec_place(rotated)
    # five.rec_place(rotated)

    # if win32api.GetKeyState(0x01) < 0:
    #     time.sleep(0.5)

    hue = three.centers(hsv.get_hsv())
    # hue = four.centers(hsv.get_hsv())
    # hue = five.centers(hsv.get_hsv())
    print(three.standard_deviation(hsv2.get_hsv()))
    # print(four.standard_deviation(hsv2.get_hsv()))
    # print(five.standard_deviation(hsv2.get_hsv()))

    three.assigning(hue, i-1)
    # four.assigning(hue, i - 1)
    # five.assigning(hue, i-1)
    print(Move.test2)

    # print(Move1.test2)
    # print(Move2.test2)

    cv.imshow(f"{i - 1}", rotated)
# tes = ""
# for i in range(6):
#     for j in range(3):
#         for k in range(3):
#             tes = tes + str(Move.test2[i][j][k].value)

# sock.sendall(tes.encode("UTF-8"))
cv.waitKey(0)
