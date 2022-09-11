import math

import cv2 as cv

import ThreeByThreeCubeMoves as Move
from Color import Color


class Three:

    def __init__(self, x1, y1, x2, y2):
        v = 10
        self.pt1 = (x1 + v, y1 + v)
        self.pt2 = (x2 - v, y2 - v)
        self.square_len_x = self.pt2[0] - self.pt1[0]
        self.square_len_y = self.pt2[1] - self.pt1[1]
        self.length = self.square_len_x // 6
        self.h = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.s = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    def rec_place(self, frame):
        cv.rectangle(frame, self.pt1, self.pt2, (211, 211, 211), 2)
        for i in range(self.pt1[0] + self.length, self.pt2[0], self.length):
            cv.line(frame, (i, self.pt1[1]), (i, self.pt2[1]), (211, 211, 211), 2)
        for i in range(self.pt1[1] + self.length, self.pt2[1], self.length):
            cv.line(frame, (self.pt1[0], i), (self.pt2[0], i), (211, 211, 211), 2)

    def centers(self, frame):
        for row, i in zip(range(3), range(self.pt1[1] + self.length, self.pt2[1], self.length * 2)):
            for col, j in zip(range(3), range(self.pt1[0] + self.length, self.pt2[0], self.length * 2)):
                self.h[row][col] = frame[i, j][0]
                self.s[row][col] = frame[i, j][1]
        return self.h

    def standard_deviation(self, frame):
        pt2 = [self.pt1[0] + (self.length * 2), self.pt1[1] + (self.length * 2)]
        hue_sum = 0
        count = 0
        sig = 0
        for i in range(self.pt1[1], pt2[1]):
            for j in range(self.pt1[0], pt2[0]):
                hue_sum += frame[i, j][0]
                count += 1
        avg = hue_sum // count
        for i in range(self.pt1[1], pt2[1]):
            for j in range(self.pt1[0], pt2[0]):
                sig += math.pow(frame[i, j][0] - avg, 2)
        sigma = math.sqrt(sig / count)
        return sigma

    def assigning(self, hue, face):
        for row in range(3):
            for col in range(3):
                if 26 <= hue[row][col] <= 60:
                    Move.test2[face][row][col] = Color.YELLOW

                elif 10 <= hue[row][col] <= 25:
                    Move.test2[face][row][col] = Color.ORANGE

                elif 0 <= self.s[row][col] <= 70:
                    Move.test2[face][row][col] = Color.WHITE

                elif 160 <= hue[row][col] <= 180 or 0 <= hue[row][col] <= 9:
                    Move.test2[face][row][col] = Color.RED

                elif 61 <= hue[row][col] <= 84:
                    Move.test2[face][row][col] = Color.GREEN

                elif 85 <= hue[row][col] <= 140 and 170 <= self.s[row][col]:
                    Move.test2[face][row][col] = Color.BLUE
