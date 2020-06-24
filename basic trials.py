import cv2

# bkg = cv2.imread("background.png")
# frg = cv2.imread("foreground.png")

bkg = cv2.imread("back.jpg")
frg = cv2.imread("fore.jpg")

bkggray = cv2.cvtColor(bkg, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(bkggray, 127, 255, 4)
bkgcontours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

frggray = cv2.cvtColor(frg, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(frggray, 127, 255, 4)
frgcontours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

img2 = cv2.drawContours(frg, frgcontours, -1, (0,255,0), 3)
cv2.imshow("Show", img2)


cv2.waitKey()
cv2.destroyAllWindows()