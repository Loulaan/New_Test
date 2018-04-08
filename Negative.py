import cv2, time


def convert():
    img = cv2.imread('A.jpg')
    img = cv2.bitwise_not(img)
    cv2.imshow('Img', img)
    time.sleep(1)
    cv2.waitKey(0)


if __name__ == '__main__':
    convert()