import cv2 as cv
import numpy as np


class Hsv:
    @staticmethod
    def processing(frame):
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        blur = cv.GaussianBlur(frame, (5, 5), 0)
        canny = cv.Canny(blur, threshold1=130, threshold2=200)
        kernal = np.ones((1, 1), np.uint8)

        # red : hue / saturation /value of brightness
        low_red = np.array([155, 100, 100])
        high_red = np.array([180, 170, 255])
        red_mask = cv.inRange(hsv, low_red, high_red)
        red_mask = cv.erode(red_mask, kernal)
        red = cv.bitwise_and(frame, frame, mask=red_mask)

        # blue
        low_blue = np.array([90, 100, 200])
        high_blue = np.array([130, 255, 255])
        blue_mask = cv.inRange(hsv, low_blue, high_blue)
        blue_mask = cv.erode(blue_mask, kernal)
        blue = cv.bitwise_and(frame, frame, mask=blue_mask)

        # green
        low_green = np.array([36, 0, 0])
        high_green = np.array([104, 255, 255])
        green_mask = cv.inRange(hsv, low_green, high_green)
        green_mask = cv.erode(green_mask, kernal)
        green = cv.bitwise_and(frame, frame, mask=green_mask)

        # orange
        low_orange = np.array([7, 100, 20])
        high_orange = np.array([25, 255, 255])
        orange_mask = cv.inRange(hsv, low_orange, high_orange)
        orange_mask = cv.erode(orange_mask, kernal)
        orange = cv.bitwise_and(frame, frame, mask=orange_mask)

        # yellow
        low_yellow = np.array([18, 0, 0])
        high_yellow = np.array([45, 255, 255])
        yellow_mask = cv.inRange(hsv, low_yellow, high_yellow)
        yellow_mask = cv.erode(yellow_mask, kernal)
        yellow = cv.bitwise_and(frame, frame, mask=yellow_mask)

        # white
        low_white = np.array([0, 0, 255])
        high_white = np.array([0, 0, 255])
        white_mask = cv.inRange(hsv, low_white, high_white)
        white_mask = cv.erode(white_mask, kernal)
        white = cv.bitwise_and(frame, frame, mask=white_mask)

        # merging all frames together
        red_blue = cv.bitwise_or(red, blue)
        green_orange = cv.bitwise_or(green, orange)
        yellow_white = cv.bitwise_or(yellow, white)
        rbgo = cv.bitwise_or(red_blue, green_orange)
        all_frames = cv.bitwise_or(rbgo, yellow_white)
        return all_frames

    @staticmethod
    def show(frame):
        cv.imshow("main", frame)


