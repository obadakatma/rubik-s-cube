import os
import time

import numpy as np

import FiveByFive as Five
import FiveByFiveCubeMoves as Move2
import FourByFour as Four
import FourByFourCubeMoves as Move1
import HSV_Filtering as Hsv
import ThreeByThree as Three
import ThreeByThreeCubeMoves as Move
from object_detector import *


# host, port = "127.0.0.1", 25001
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((host, port))


def rotate(image, Angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, Angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)


def nothing():
    pass


angle, box, box2, box3, rotated = 0, 0, 0, 0, 0
maximum = 0
x, y, w, h = 0, 0, 0, 0
std = [0, 0, 0, 0, 0, 0]
rotateNum = [2, 2, 3, 0, 1, 1]
pt1 = (200, 116)
pt2 = (400, 316)
i, keyNum = 0, 0
cv.namedWindow("CameraLight")
cv.createTrackbar("exposure", "CameraLight", 1, 7, nothing)
capture = cv.VideoCapture(0)

while True:
    _, frame = capture.read()
    exposure = cv.getTrackbarPos("exposure", "CameraLight")
    capture.set(15, -exposure)
    capture.set(10, 255)
    capture.set(12, 255)
    cv.imshow('Main', frame)
    if cv.waitKey(1) == ord('s'):
        print('Start!')
        time.sleep(0.5)
        keyNum = 1
    if keyNum == 1:
        if i == 0:
            time.sleep(3)
            cv.imwrite(f"photos/{i}.png", frame)
            print("done0")
            os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove1.exe")
            time.sleep(7)
            i += 1
        elif i == 1:
            cv.imwrite(f"photos/{i}.png", frame)
            print("done1")
            os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\leftMove.exe")
            time.sleep(6)
            i += 1

        elif i == 2:
            cv.imwrite(f"photos/{i}.png", frame)
            print("done2")
            os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\leftMove.exe")
            time.sleep(7)
            i += 1

        elif i == 3:
            cv.imwrite(f"photos/{i}.png", frame)
            print("done3")
            os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\leftMove.exe")
            time.sleep(8)
            i += 1

        elif i == 4:
            cv.imwrite(f"photos/{i}.png", frame)
            print("done4")
            os.startfile(r"C:\Users\obada\Desktop\Rubik'sCubeSolverPROJECT\EV3 small basic\centerMove1.exe")
            time.sleep(6)
            i += 1

        elif i == 5:
            cv.imwrite(f"photos/{i}.png", frame)
            print("done5")
            i += 1

        elif i == 6:
            break
    elif i == 7:
        break
    if cv.waitKey(32) & 0xFF == ord(' '):
        break
cv.destroyWindow("Main")
cv.destroyWindow("CameraLight")
# ###############################################################################################################################
for i in range(6):
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

    std[i] = three.standard_deviation(hsv2.get_hsv())

    cv.imshow(f"{i}", rotated)

# tes = ""
# for i in range(6):
#     for j in range(3):
#         for k in range(3):
#             tes = tes + str(Move.test2[i][j][k].value)

# sock.sendall(tes.encode("UTF-8"))
maximum = max(std)
print(maximum)
for i in range(6):
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
    if maximum <= 20:
        three = Three.Three(x, y, x2, y2)
        three.rec_place(rotated)
        hue1 = three.centers(hsv.get_hsv())
        three.assigning(hue1, i)
        print(Move.test2)

    elif 5 < maximum <= 27:
        five = Five.Five(x, y, x2, y2)
        five.rec_place(rotated)
        hue3 = five.centers(hsv2.get_hsv())
        five.assigning(hue3, i)
        print(Move2.test2)

    elif 27 <= maximum:
        four = Four.Four(x, y, x2, y2)
        four.rec_place(rotated)
        hue2 = four.centers(hsv.get_hsv())
        four.assigning(hue2, i)
        print(Move1.test2)

    cv.imshow(f"{i}", rotated)
# state = Move.State(0, Move.test2)
# state = state.switchIndexes(rotateNum)
# for line in state.state:
#     for line1 in line:
#         print(line1)

cv.waitKey(0)
