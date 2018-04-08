import cv2


def convert():
    img = cv2.imread('A.jpg')
    img = cv2.bitwise_not(img)
    cv2.imshow('Img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    convert()