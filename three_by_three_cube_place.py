import cv2 as cv


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
