import cv2 as cv
import numpy as np


class Hsv:
    # def nothing(x):
    #     pass
    # cv.namedWindow("red_trackbar")
    # cv.createTrackbar("L-V", "red_trackbar", 0, 255, nothing)
    @staticmethod
    def processing(self, frame):
        self.hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        kernal = np.ones((3, 3), np.uint8)

        # L_V = cv.getTrackbarPos("L-V", "red_trackbar")
        low = np.array([0, 0, 130])
        high = np.array([180, 255, 255])
        mask = cv.inRange(self.hsv, low, high)
        mask = cv.erode(mask, kernal)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
        res = cv.bitwise_and(frame, frame, mask=mask)
        return res

    def get_hsv(self):
        return self.hsv
