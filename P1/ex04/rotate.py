import numpy as np


def ft_rotate(img):
    rotatedImg = []
    for x in range(img.shape[1]):
        row = []
        for y in range(img.shape[0]):
            row.append(img[y][x][0])
        rotatedImg.append(row)
    return np.array(rotatedImg)
