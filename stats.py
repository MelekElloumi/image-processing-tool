import settings as s
import math


def nbPixels():
    return s.width * s.height


def average(image):
    avg = 0
    for h in range(s.height):
        for w in range(s.width):
            avg += image[h][w]
    return avg / nbPixels()


def deviation(image):
    avg = average(image)
    dev = 0
    for h in range(s.height):
        for w in range(s.width):
            dev += (image[h][w] - avg) ** 2
    return math.sqrt(dev / nbPixels())


def histogram(image):
    hist = [0] * (s.graylevel + 1)
    for h in range(s.height):
        for w in range(s.width):
            hist[image[h][w]] += 1
    return hist


def cumulated_histogram(image):
    hist = histogram(image)
    cum_hist = [0] * (s.graylevel + 1)
    cum_hist[0] = hist[0]
    for g in range(1, s.graylevel + 1):
        cum_hist[g] = hist[g] + cum_hist[g - 1]
    return cum_hist


def entropy(image):
    hist = histogram(image)
    ent = 0
    for g in range(s.graylevel + 1):
        p = hist[g] / nbPixels()
        if (p != 0):
            ent += p * math.log2(1 / p)
    return ent


def dynamic(image):
    hist = histogram(image)
    dmin, dmax = 0, s.graylevel
    for g in range(s.graylevel + 1):
        if (hist[g] == 0):
            continue
        else:
            dmin = g
            break
    for g in reversed(range(s.graylevel + 1)):
        if (hist[g] == 0):
            continue
        else:
            dmax = g
            break
    return dmin, dmax


def SNR(image):
    avg = average(s.image_orig)
    S = 0
    B = 0
    for h in range(s.height):
        for w in range(s.width):
            S += (s.image_orig[h][w] - avg) ** 2
            B += (image[h][w] - s.image_orig[h][w]) ** 2
    if (B == 0):
        return 0.0
    return math.sqrt(S / B)
