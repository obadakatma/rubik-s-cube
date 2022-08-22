import cv2 as cv
import win32api


class place:
    @staticmethod
    def rec_place(frame):
        pt1 = [(frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 + 50),
               (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 50),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 50)]

        pt2 = [(frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 - 50),
               (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 50),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 50),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 50),
               (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 150)]

        for p1, p2 in zip(pt1, pt2):
            cv.rectangle(frame, p1, p2, (211, 211, 211), 3)

    @staticmethod
    def centers(frame, in_array):
        cen = [(frame.shape[0] // 2 - 100, frame.shape[1] // 2 - 100),
               (frame.shape[0] // 2 - 100, frame.shape[1] // 2),
               (frame.shape[0] // 2 - 100, frame.shape[1] // 2 + 100),
               (frame.shape[0] // 2, frame.shape[1] // 2 - 100),
               (frame.shape[0] // 2, frame.shape[1] // 2),
               (frame.shape[0] // 2, frame.shape[1] // 2 + 100),
               (frame.shape[0] // 2 + 100, frame.shape[1] // 2 - 100),
               (frame.shape[0] // 2 + 100, frame.shape[1] // 2),
               (frame.shape[0] // 2 + 100, frame.shape[1] // 2 + 100)]

        for i, tup in zip(range(9), cen):
            in_array[i] = list(frame[tup])

    @staticmethod
    def print_values(in_array, out_array):
        for i, lis in zip(range(10), in_array):
            out_array[i] = lis[::-1]
        print(out_array)
