import cv2
import numpy as np


def main():
    image = cv2.imread('')
    s_vs_p = 0.5
    amount = 0.1  # Менять количество шумов тут
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
    for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
    for i in image.shape]
    out[coords] = 0

    cv2.imshow('img', out)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()