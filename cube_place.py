import cv2 as cv


class place:
    @staticmethod
    def rec_place(frame):
        cv.rectangle(frame, (frame.shape[1] // 2 - 200, frame.shape[0] // 2 - 200),
                     (frame.shape[1] // 2 - 100, frame.shape[0] // 2 - 100), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 200),
                     (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 100), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 + 100, frame.shape[0] // 2 - 200),
                     (frame.shape[1] // 2 + 200, frame.shape[0] // 2 - 100), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 - 200, frame.shape[0] // 2 - 50),
                     (frame.shape[1] // 2 - 100, frame.shape[0] // 2 + 50), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 50),
                     (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 50), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 + 100, frame.shape[0] // 2 - 50),
                     (frame.shape[1] // 2 + 200, frame.shape[0] // 2 + 50), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 - 200, frame.shape[0] // 2 + 100),
                     (frame.shape[1] // 2 - 100, frame.shape[0] // 2 + 200), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 100),
                     (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 200), (211, 211, 211), 3)

        cv.rectangle(frame, (frame.shape[1] // 2 + 100, frame.shape[0] // 2 + 100),
                     (frame.shape[1] // 2 + 200, frame.shape[0] // 2 + 200), (211, 211, 211), 3)

        ####################################################
        # cv.rectangle(frame, (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 150),
        #              (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 150),
        #              (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 150),
        #              (frame.shape[1] // 2 + 150, frame.shape[0] // 2 - 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 - 150, frame.shape[0] // 2 - 50),
        #              (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 - 50),
        #              (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 + 50, frame.shape[0] // 2 - 50),
        #              (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 50), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 - 150, frame.shape[0] // 2 + 50),
        #              (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 150), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 - 50, frame.shape[0] // 2 + 50),
        #              (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 150), (211, 211, 211), 3)
        #
        # cv.rectangle(frame, (frame.shape[1] // 2 + 50, frame.shape[0] // 2 + 50),
        #              (frame.shape[1] // 2 + 150, frame.shape[0] // 2 + 150), (211, 211, 211), 3)