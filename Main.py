import time

import win32api

import HSV_Filtering as Hsv
import ThreeByThreeCubeMoves as THMove
from FiveByFive import Five
from FourByFour import Four
from ThreeByThree import Three
from object_detector import *

face = 0
main_counter = 0
capture = cv.VideoCapture(0)
while True:
    _, frame = capture.read()
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    pt1 = (frame.shape[1] // 2 - 180, frame.shape[0] // 2 - 180)
    pt2 = (frame.shape[1] // 2 + 180, frame.shape[0] // 2 + 180)
    rectangle = cv.rectangle(blank.copy(), pt1, pt2, 255, -1)
    masked = cv.bitwise_and(frame, frame, mask=rectangle)
    # frame = frame[75:425, 125:475]
    new_frame = frame.copy()

    detector = HomogeneousBgDetector()
    hsv = Hsv.Hsv()
    main_frame = hsv.processing(hsv, masked)

    detector.detect_objects(main_frame)
    x1, y1, x2, y2 = detector.min_rec()

    three = Three(x1, y1, x2, y2)
    four = Four(x1, y1, x2, y2)
    five = Five(x1, y1, x2, y2)
    if main_counter == 0:
        three.rec_place(frame)
    elif main_counter == 1:
        four.rec_place(frame)
    elif main_counter == 2:
        four.rec_place(frame)

    hue = three.centers(hsv.get_hsv())

    cv.imshow("main", frame)
    cv.imshow("HSV", main_frame)

    if win32api.GetKeyState(0x01) < 0:
        time.sleep(0.5)
        sigma = three.standard_deviation(main_frame)
        print(sigma)
        # minSigma = 15
        # maxSigma = 70
        # if sigma < minSigma and face < 6:
        #     three.assigning(hue, face)
        #     # print(move.test2)
        #     print(sigma)
        #     print(hue)
        #     print(three.s)
        #     face += 1
        # elif sigma < minSigma and face == 6:
        #     print(sigma)
        #     print(hue)
        #     print(three.s)
        #     print(THMove.test2)
        #     # for line in move.L1R(THMove.test2):
        #     #     for line1 in line:
        #     #         print(line1)
        #     face += 1
        # elif minSigma < sigma < maxSigma and face < 6:
        #     cv.destroyWindow("main")
        #     cv.destroyWindow("HSV")
        #     main_counter = 1
        #     four.centers(main_frame)
        #     cv.imshow("main", frame)
        #     print("saturation", four.s)
        #     print("sigma = ", sigma)
        #     face += 1
        # elif sigma < minSigma < maxSigma and face == 6:
        #     print(sigma)
        #     print(hue)
        #     print(four.s)
        #     face += 1
        # elif minSigma < sigma and face < 6:
        #     sigma = five.standard_deviation(main_frame)
        #     if sigma < minSigma < maxSigma and face < 6:
        #         cv.destroyWindow("main")
        #         cv.destroyWindow("HSV")
        #         main_counter = 2
        #         five.centers(main_frame)
        #         cv.imshow("Main", frame)
        #         print("saturation", five.s)
        #         print("sigma = ", sigma)
        #         face += 1
        #     elif sigma < minSigma < maxSigma and face == 6:
        #         print(sigma)
        #         print(hue)
        #         print(five.s)
        #         face += 1
        # else:
        #     break
    if cv.waitKey(32) & 0xFF == ord(' '):
        break
