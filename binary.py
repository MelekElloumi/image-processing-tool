import settings as s
from utils import clone
from stats import histogram
from stats import cumulated_histogram
import math


def binarize(image, threshold):
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            if image[h][w] > threshold:
                new_image[h][w] = s.graylevel
            else:
                new_image[h][w] = 0
    return new_image


def thresholding(image):
    hist = histogram(image)
    cum_hist = cumulated_histogram(image)
    fmin = math.inf
    thmin = -1
    for i in range(0, s.graylevel + 1):
        q1, q2 = cum_hist[i], cum_hist[s.graylevel] - cum_hist[i]
        if q1 < 1.e-6 or q2 < 1.e-6:
            continue
        m1, m2, v1, v2 = 0, 0, 0, 0
        for g in range(0, i + 1):
            m1 += g * hist[g] / s.graylevel
        m1 = m1 / q1
        for g in range(0, i + 1):
            v1 += ((g - m1) ** 2) * hist[g] / s.graylevel
        v1 = v1 / q1
        for g in range(i + 1, s.graylevel + 1):
            m2 += g * hist[g] / s.graylevel
        m2 = m2 / q2
        for g in range(i + 1, s.graylevel + 1):
            v2 += ((g - m2) ** 2) * hist[g] / s.graylevel
        v2 = v2 / q2
        f = v1 * q1 + v2 * q2
        if f < fmin:
            fmin = f
            thmin = i
    return binarize(image, thmin),thmin


def dilatation(image, size):
    if size % 2 == 0:
        size += 1
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            mintab = []
            for py in range(max(0, h - size // 2), min(s.height, h + size // 2 + 1)):
                for px in range(max(0, w - size // 2), min(s.width, w + size // 2 + 1)):
                    mintab.append(image[py][px])
            jiik
            new_image[h][w] = mintab[0]
    return new_image


def erosion(image, size):
    if size % 2 == 0:
        size += 1
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            maxtab = []
            for py in range(max(0, h - size // 2), min(s.height, h + size // 2 + 1)):
                for px in range(max(0, w - size // 2), min(s.width, w + size // 2 + 1)):
                    maxtab.append(image[py][px])
            maxtab.sort()
            new_image[h][w] = maxtab[len(maxtab) - 1]
    return new_image


def closing(image, size):
    return dilatation(erosion(image, size), size)

def opening(image, size):
    return erosion(dilatation(image, size), size)
