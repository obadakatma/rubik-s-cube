import cv2 as cv
import math


class Three:
    def __init__(self, frame):
        self.pt1 = (frame.shape[1] // 2 - 128, frame.shape[0] // 2 - 128)
        self.pt2 = (frame.shape[1] // 2 + 128, frame.shape[0] // 2 + 128)
        self.square_len_x = self.pt2[0] - self.pt1[0]
        self.square_len_y = self.pt2[1] - self.pt1[1]
        self.length = self.square_len_x // 4
        self.h = []

    def rec_place(self, frame):
        cv.rectangle(frame, self.pt1, self.pt2, (211, 211, 211), 3)
        for i in range(self.pt1[0] + self.length, self.pt2[0], self.length):
            cv.line(frame, (i, self.pt1[1]), (i, self.pt2[1]), (211, 211, 211), 3)
        for i in range(self.pt1[1] + self.length, self.pt2[1], self.length):
            cv.line(frame, (self.pt1[0], i), (self.pt2[0], i), (211, 211, 211), 3)

    def centers(self, frame):
        for i in range(self.pt1[1] + self.length, self.pt2[1], self.length):
            for j in range(self.pt1[0] + self.length, self.pt2[0], self.length):
                self.h.append(frame[i, j][0])

    def standard_deviation(self, frame):
        pt2 = [self.pt1[0] + self.length, self.pt1[1] + self.length]
        square_len_x = pt2[0] - self.pt1[0]
        length = square_len_x // 4
        hsum = 0
        count = 0
        sig = 0
        for i in range(self.pt1[1] + length, pt2[1], length):
            for j in range(self.pt1[0] + length, pt2[0], length):
                hsum += frame[i, j][0]
                count += 1
        avg = hsum // count
        for i in range(self.pt1[1] + length, pt2[1], length):
            for j in range(self.pt1[0] + length, pt2[0], length):
                sig += math.pow(frame[i, j][0] - avg, 2)
        sigma = math.sqrt(sig / count)
        return sigma

