import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)   # try 1, 2, 3 if u are using secondary or tertiary cameras

time.sleep(3)
count = 0
bkg = 0

for i in range(60):
    _, bkg = cap.read()
bkg = np.flip(bkg, axis=1)

while (cap.isOpened()):
    _, img = cap.read()
    if not _:
        break
    count += 1
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # cv2.imshow("mask1", mask1)

    mask2 = cv2.bitwise_not(mask1)
    # cv2.imshow("mask2", mask2)

    reso1 = cv2.bitwise_and(img, img, mask=mask2)
    # cv2.imshow("res1", reso1)

    reso2 = cv2.bitwise_and(bkg, bkg, mask=mask1)
    # cv2.imshow("res2", reso2)

    final = cv2.addWeighted(reso1, 1, reso2, 1, 0)
    out.write(final)
    cv2.imshow("full functional", final)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
