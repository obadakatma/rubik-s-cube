import cv2 as cv
import numpy as np


class HomogeneousBgDetector:
    def __init__(self):
        self.objects_contours = []
        self.x1 = 0
        self.y1 = 0
        self.w = 0
        self.h = 0

    def detect_objects(self, frame):
        # Convert Image to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Create a Mask with adaptive threshold
        mask = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 19, 5)

        # Find contours
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # cv.imshow("mask", mask)

        for cnt in contours:
            area = cv.contourArea(cnt)
            if area > 2000:
                # cnt = cv.approxPolyDP(cnt, 0.03*cv.arcLength(cnt, True), True)
                self.objects_contours.append(cnt)

    # def get_objects_rect(self):
    #     box = cv.boxPoints(rect)  # cv.boxPoints(rect) for OpenCV 3.x
    #     box = np.int0(box)
    def min_rec(self):
        x2 = 0
        y2 = 0
        for cnt in self.objects_contours:
            rect = cv.minAreaRect(cnt)
            points = cv.boxPoints(rect)
            box = np.int0(points)
            self.x1, self.y1, self.w, self.h = cv.boundingRect(box)
            x2, y2 = self.x1 + self.w, self.y1 + self.h
            # if x2 <= 350 and y2 <= 350:
        return self.x1, self.y1, x2, y2
