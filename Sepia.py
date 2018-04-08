import cv2
import numpy as np


def main():
    img = cv2.imread('Testers/DeadPool.jpg')
    kernel = np.asarray( [
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]] )

    sep = cv2.transform(img, kernel)
    # cv2.imshow('Sepia', sep)
    cv2.imwrite('sepia1.jpg', sep)

    # Голубая сепия
    # kernel = np.asarray( [
    # [0.393, 0.769, 0.189],
    # [0.349, 0.686, 0.168],
    # [0.272, 0.534, 0.131]] )

    # sep = cv2.transform(img, kernel)
    # # cv2.imshow('Sepia', sep)
    # cv2.imwrite('sepia2.jpg', sep)

    # cv2.waitKey(0)


if __name__ == '__main__':
    main()