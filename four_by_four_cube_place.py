import cv2 as cv

in_array = [[], [], [], [],
            [], [], [], [],
            [], [], [], [],
            [], [], [], []]

out_array = [[], [], [], [],
             [], [], [], [],
             [], [], [], [],
             [], [], [], []]


class four:
    @staticmethod
    def rec_place(frame):
        pt1 = [(frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 - 150),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2),
               (frame.shape[1] // 2, frame.shape[0] // 2),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2),
               (frame.shape[1] // 2 - 150, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 + 75)]

        pt2 = [(frame.shape[1] // 2 - 75, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 - 75),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2),
               (frame.shape[1] // 2, frame.shape[0] // 2),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 75),
               (frame.shape[1] // 2 - 75, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 75, frame.shape[0] // 2 + 150),
               (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 150)]

        for p1, p2 in zip(pt1, pt2):
            cv.rectangle(frame, p1, p2, (211, 211, 211), 3)

    @staticmethod
    def centers(frame):
        cen = [(frame.shape[0] // 2 - 113, frame.shape[1] // 2 - 113),
               (frame.shape[0] // 2 - 113, frame.shape[1] // 2 - 37),
               (frame.shape[0] // 2 - 113, frame.shape[1] // 2 + 37),
               (frame.shape[0] // 2 - 113, frame.shape[1] // 2 + 113),
               (frame.shape[0] // 2 - 37, frame.shape[1] // 2 - 113),
               (frame.shape[0] // 2 - 37, frame.shape[1] // 2 - 37),
               (frame.shape[0] // 2 - 37, frame.shape[1] // 2 + 37),
               (frame.shape[0] // 2 - 37, frame.shape[1] // 2 + 113),
               (frame.shape[0] // 2 + 37, frame.shape[1] // 2 - 113),
               (frame.shape[0] // 2 + 37, frame.shape[1] // 2 - 37),
               (frame.shape[0] // 2 + 37, frame.shape[1] // 2 + 37),
               (frame.shape[0] // 2 + 37, frame.shape[1] // 2 + 113),
               (frame.shape[0] // 2 + 113, frame.shape[1] // 2 - 113),
               (frame.shape[0] // 2 + 113, frame.shape[1] // 2 - 37),
               (frame.shape[0] // 2 + 113, frame.shape[1] // 2 + 37),
               (frame.shape[0] // 2 + 113, frame.shape[1] // 2 + 113)]

        for i, tup in zip(range(16), cen):
            in_array[i] = list(frame[tup])

    @staticmethod
    def print_values():
        for i, lis in zip(range(16), in_array):
            out_array[i] = lis[::-1]
        print(out_array)
