import cv2

cap = cv2.VideoCapture(0)

while True:
    __, frame = cap.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray, (3, 3), 0)
    edges = cv2.Canny(blur, 100, 200)
    __, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for cnt in contours[:int(len(contours) / 2)]:
        cv2.drawContours(frame, [cnt], 0, (0, 0, 255), 1)
        i += 1
    cv2.imshow('Contour', frame)
    cv2.imshow('Thresh', edges)
    cv2.imshow('imgray', imgray)
    cv2.imshow('Blur', blur)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()