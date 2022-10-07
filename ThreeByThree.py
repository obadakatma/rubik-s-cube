import cv2 as cv

import ThreeByThreeCubeMoves as Move
from Color import Color


class Three:
    def __init__(self, x1, y1, x2, y2):
        v = 9
        self.pt1 = (int(x1 + v), int(y1 + v))
        self.pt2 = (int(x2 - v), int(y2 - v))
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
        try:
            pt1 = (self.pt1[0] + (self.length * 2) + 8, self.pt1[1] + (self.length * 2) + 8)
            pt2 = (self.pt1[0] + (self.length * 4) - 8, self.pt1[1] + (self.length * 4) - 8)
            cv.rectangle(frame, pt1, pt2, (255, 255, 255), 2)

            cv.rectangle(frame, self.pt1, self.pt2, (211, 211, 211), 2)
            for i in range(self.pt1[0] + self.length, self.pt2[0], self.length):
                cv.line(frame, (i, self.pt1[1]), (i, self.pt2[1]), (211, 211, 211), 2)
            for i in range(self.pt1[1] + self.length, self.pt2[1], self.length):
                cv.line(frame, (self.pt1[0], i), (self.pt2[0], i), (211, 211, 211), 2)
        except ValueError:
            print(ValueError)

    def centers(self, hsv):
        for row, i in zip(range(3), range(self.pt1[1] + self.length, self.pt2[1], self.length * 2)):
            for col, j in zip(range(3), range(self.pt1[0] + self.length, self.pt2[0], self.length * 2)):
                self.h[row][col] = hsv[i, j][0]
                # print(self.h)
                self.s[row][col] = hsv[i, j][1]
                # print(self.s)

        return self.h

    def standard_deviation(self, frame):
        frame = cv.GaussianBlur(frame, (187, 187), 7)
        pt1 = (self.pt1[0] + (self.length * 2), self.pt1[1] + (self.length * 2))
        pt2 = (self.pt1[0] + (self.length * 4), self.pt1[1] + (self.length * 4))
        hue_sum = 0
        count = 0
        sig = 0
        for i in range(pt1[1] + 8, pt2[1] - 8):
            for j in range(pt1[0] + 8, pt2[0] - 8):
                hue_sum += frame[i, j][0] % 170
                count += 1
        avg = hue_sum // count

        for i in range(pt1[1] + 8, pt2[1] - 8):
            for j in range(pt1[0] + 8, pt2[0] - 8):
                sig += (frame[i, j][0] - avg) ** 2
        std = (sig / count) ** 0.5
        return std

    def assigning(self, hue, face):
        # for face in range(6):
        for row in range(3):
            for col in range(3):
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
