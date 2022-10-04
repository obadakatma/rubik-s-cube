import cv2 as cv


class HomogeneousBgDetector():
    def __init__(self):
        pass

    def detect_objects(self, frame):
        # Convert Image to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Create a Mask with adaptive threshold
        mask = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 19, 5)

        # Find contours
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        #cv.imshow("mask", mask)
        objects_contours = []

        for cnt in contours:
            area = cv.contourArea(cnt)
            if area > 2000:
                #cnt = cv.approxPolyDP(cnt, 0.03*cv.arcLength(cnt, True), True)
                objects_contours.append(cnt)

        return objects_contours

    # def get_objects_rect(self):
    #     box = cv.boxPoints(rect)  # cv.boxPoints(rect) for OpenCV 3.x
    #     box = np.int0(box)