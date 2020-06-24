import cv2
import numpy as np

firstbkg = cv2.VideoCapture(0)          # video capture source camera (Here webcam of laptop)
ret, firstbkgimage1 = firstbkg.read()   # return a single frame in variable `frame`
ret, firstbkgimage = firstbkg.read()
firstbkg.release()

cap = cv2.VideoCapture(0)
i = 0
while True:
    _, frame = cap.read()
    if i == 0:
        bkg = frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    i += 1

    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])

    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # maskgray = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    # maskgray = cv2.cvtColor(maskgray, cv2.COLOR_BGR2GRAY)

    # ret, thresh = cv2.threshold(mask, 127, 255, 4)
    maskcontours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if maskcontours:
        c = max(maskcontours, key=cv2.contourArea)
    else:
        c = []
    masked = cv2.drawContours(frame, c, -1, (0, 255, 0), -1)
    print(c)
    # outputs = frame

    # masked = cv2.drawContours(frame, maskcontours, -1, (0, 255, 0), 3)

    cv2.imshow("contoured", masked)
    # cv2.imshow('frame', frame)
    cv2.imshow("Mask", mask)
    # cv2.imshow("bkg", bkg)
    cv2.imshow("firbkg", firstbkgimage)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()