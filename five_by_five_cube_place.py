import cv2 as cv

in_array = [[], [], [], [], [],
            [], [], [], [], [],
            [], [], [], [], [],
            [], [], [], [], [],
            [], [], [], [], []]

out_array = [[], [], [], [], [],
             [], [], [], [], [],
             [], [], [], [], [],
             [], [], [], [], [],
             [], [], [], [], []]


class five:
    @staticmethod
    def rec_place(frame):
        pt1 = [(frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 + 90)]

        pt2 = [(frame.shape[1] // 2 - 90, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 - 90),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 - 30),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 30),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 90),
               (frame.shape[1] // 2 - 90, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 - 30, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 30, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 90, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 150)]

        for p1, p2 in zip(pt1, pt2):
            cv.rectangle(frame, p1, p2, (211, 211, 211), 3)

    @staticmethod
    def centers(frame):
        cen = [(frame.shape[0] // 2 - 120, frame.shape[1] // 2 - 120),
               (frame.shape[0] // 2 - 120, frame.shape[1] // 2 - 60),
               (frame.shape[0] // 2 - 120, frame.shape[1] // 2),
               (frame.shape[0] // 2 - 120, frame.shape[1] // 2 + 60),
               (frame.shape[0] // 2 - 120, frame.shape[1] // 2 + 120),
               (frame.shape[0] // 2 - 60, frame.shape[1] // 2 - 120),
               (frame.shape[0] // 2 - 60, frame.shape[1] // 2 - 60),
               (frame.shape[0] // 2 - 60, frame.shape[1] // 2),
               (frame.shape[0] // 2 - 60, frame.shape[1] // 2 + 60),
               (frame.shape[0] // 2 - 60, frame.shape[1] // 2 + 120),
               (frame.shape[0] // 2, frame.shape[1] // 2 - 120),
               (frame.shape[0] // 2, frame.shape[1] // 2 - 60),
               (frame.shape[0] // 2, frame.shape[1] // 2),
               (frame.shape[0] // 2, frame.shape[1] // 2 + 60),
               (frame.shape[0] // 2, frame.shape[1] // 2 + 120),
               (frame.shape[0] // 2 + 60, frame.shape[1] // 2 - 120),
               (frame.shape[0] // 2 + 60, frame.shape[1] // 2 - 60),
               (frame.shape[0] // 2 + 60, frame.shape[1] // 2),
               (frame.shape[0] // 2 + 60, frame.shape[1] // 2 + 60),
               (frame.shape[0] // 2 + 60, frame.shape[1] // 2 + 120),
               (frame.shape[0] // 2 + 120, frame.shape[1] // 2 - 120),
               (frame.shape[0] // 2 + 120, frame.shape[1] // 2 - 60),
               (frame.shape[0] // 2 + 120, frame.shape[1] // 2),
               (frame.shape[0] // 2 + 120, frame.shape[1] // 2 + 60),
               (frame.shape[0] // 2 + 120, frame.shape[1] // 2 + 120)]

        for i, tup in zip(range(25), cen):
            in_array[i] = list(frame[tup])

    @staticmethod
    def print_values():
        for i, lis in zip(range(25), in_array):
            out_array[i] = lis[::-1]
        print(out_array)
