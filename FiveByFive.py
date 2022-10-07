import cv2 as cv

import FiveByFiveCubeMoves as Move
from Color import Color


class Five:
    def __init__(self, x1, y1, x2, y2):
        v = 10
        self.pt1 = (x1 + v, y1 + v)
        self.pt2 = (x2 - v, y2 - v)
        self.square_len_x = self.pt2[0] - self.pt1[0]
        self.square_len_y = self.pt2[1] - self.pt1[1]
        self.length = self.square_len_x // 10
        self.h = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        self.s = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

    def rec_place(self, frame):
        num=4
        pt1 = (self.pt1[0] + (self.length * 4) + num, self.pt1[1] + (self.length * 4) + num)
        pt2 = (self.pt1[0] + (self.length * 6) - num, self.pt1[1] + (self.length * 6) - num)
        cv.rectangle(frame, pt1, pt2, (255, 255, 255), 2)
        cv.rectangle(frame, self.pt1, self.pt2, (211, 211, 211), 2)
        for i in range(self.pt1[0] + self.length, self.pt2[0], self.length):
            cv.line(frame, (i, self.pt1[1]), (i, self.pt2[1]), (211, 211, 211), 2)
        for i in range(self.pt1[1] + self.length, self.pt2[1], self.length):
            cv.line(frame, (self.pt1[0], i), (self.pt2[0], i), (211, 211, 211), 2)

    def centers(self, frame):
        for row, i in zip(range(5), range(self.pt1[1] + self.length, self.pt2[1], self.length * 2)):
            for col, j in zip(range(5), range(self.pt1[0] + self.length, self.pt2[0], self.length * 2)):
                self.h[row][col] = frame[i, j][0]
                # print(self.h)
                self.s[row][col] = frame[i, j][1]
        return self.h

    def standard_deviation(self, frame):
        frame = cv.GaussianBlur(frame, (101,101), 0)
        pt1 = (self.pt1[0] + (self.length * 4), self.pt1[1] + (self.length * 4))
        pt2 = (self.pt1[0] + (self.length * 6), self.pt1[1] + (self.length * 6))
        hue_sum = 0
        count = 0
        sig = 0
        num = 4
        for i in range(pt1[1] + num, pt2[1] - num):
            for j in range(pt1[0] + num, pt2[0] - num):
                hue_sum += frame[i, j][0] % 180
                count += 1
        avg = hue_sum // count

        for i in range(pt1[1] + num, pt2[1] - num):
            for j in range(pt1[0] + num, pt2[0] - num):
                sig += (frame[i, j][0] - avg) ** 2
        std = (sig / count) ** 0.5
        return std

    def assigning(self, hue, face):
        # for face in range(6):
        for row in range(5):
            for col in range(5):
                if self.s[row][col] == 0 or self.s[row][col] <= 40:
                    Move.test2[face][row][col] = Color.WHITE

                elif 95 <= hue[row][col] <= 130:
                    Move.test2[face][row][col] = Color.BLUE

                elif 27 <= hue[row][col] <= 40:
                    Move.test2[face][row][col] = Color.YELLOW

                elif 9 <= hue[row][col] <= 25:
                    Move.test2[face][row][col] = Color.ORANGE

                elif 170 <= hue[row][col] <= 180 or 0 <= hue[row][col] <= 8:
                    Move.test2[face][row][col] = Color.RED

                elif 41 <= hue[row][col] <= 75:
                    Move.test2[face][row][col] = Color.GREEN
