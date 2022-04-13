import settings as s
import stats
from utils import clone


def equalization(image):
    cum_hist = stats.cumulated_histogram(image)
    LUT = [0] * (s.graylevel + 1)
    for g in range(s.graylevel + 1):
        LUT[g] = int(s.graylevel * cum_hist[g] / stats.nbPixels())
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            new_image[h][w] = LUT[image[h][w]]
    return new_image


def local_equalization(image, size):
    if (size % 2 == 0):
        size += 1
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            histc = 0
            nbp = 0
            for py in range(max(0, h - size // 2), min(s.height, h + size // 2 + 1)):
                for px in range(max(0, w - size // 2), min(s.width, w + size // 2 + 1)):
                    if (image[py][px] <= image[h][w]):
                        histc += 1
                    nbp += 1
            new_image[h][w] = int(s.graylevel * histc / nbp)
    return new_image


def linear_transformation(image, points):
    LUT = [0] * (s.graylevel + 1)
    for p in range(1, len(points)):
        slope = (points[p][1] - points[p - 1][1]) / (points[p][0] - points[p - 1][0])
        intercept = points[p][1] - slope * points[p][0]
        for g in range(points[p - 1][0], points[p][0] + 1):
            LUT[g] = int(slope * g + intercept)
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            new_image[h][w] = LUT[new_image[h][w]]
    return new_image


def dark_dilatation(image):
    points = [
        [0, 0],
        [int(s.graylevel / 4), int(s.graylevel / 2)],
        [s.graylevel, s.graylevel]
    ]
    return linear_transformation(image, points)


def inverse(image):
    points = [
        [0, s.graylevel],
        [s.graylevel, 0]
    ]
    return linear_transformation(image, points)


def light_dilatation(image):
    points = [
        [0, 0],
        [int(s.graylevel / 2), int(s.graylevel / 4)],
        [s.graylevel, s.graylevel]
    ]
    return linear_transformation(image, points)


def middle_dilatation(image):
    points = [
        [0, 0],
        [int(s.graylevel / 3), int(s.graylevel / 6)],
        [int(s.graylevel * 2 / 3), int(s.graylevel * 5 / 6)],
        [s.graylevel, s.graylevel]
    ]
    return linear_transformation(image, points)
