import settings as s
from utils import clone


def filter_median(image, size):
    if (size % 2 == 0):
        size += 1
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            medians = []
            for py in range(max(0, h - size // 2), min(s.height, h + size // 2 + 1)):
                for px in range(max(0, w - size // 2), min(s.width, w + size // 2 + 1)):
                    medians.append(image[py][px])
            medians.sort()
            new_image[h][w] = medians[len(medians) // 2 + 1]
    return new_image


def convolution(image, filter, size):
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            conv = 0
            for py in range(-size // 2, size // 2 + 1):
                if not (((py + h) < 0) or ((py + h) >= s.height)):
                    for px in range(-size // 2, size // 2 + 1):
                        if not (((px + w) < 0) or ((px + w) >= s.width)):
                            conv += image[py + h][px + w] * filter[py + size // 2][px + size // 2]
            if (conv < 0):
                conv = 0
            if (conv > s.graylevel):
                conv = s.graylevel
            new_image[h][w] = int(conv)
    return new_image


def filter_average(image, size):
    if (size % 2 == 0):
        size += 1
    filter = [[1 / size ** 2 for i in range(size)] for j in range(size)]
    return convolution(image, filter, size)


def filter_gauss(image, size):
    if (size % 2 == 0):
        size += 1
    filter = [[1 for i in range(size)] for j in range(size)]
    sum = 0
    center = size // 2
    for py in range(-center, center + 1):
        for px in range(-center, center + 1):
            filter[py + center][px + center] = 2 ** (center ** 2 - abs(py) - abs(px))
            sum += filter[py + center][px + center]
    for py in range(-center, center + 1):
        for px in range(-center, center + 1):
            filter[py + center][px + center] /= sum
    return convolution(image, filter, size)


def filter_highboost(image, size):
    image_low = filter_average(image, size)
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            new_image[h][w] = abs(image[h][w] - image_low[h][w])
    return new_image


def filter_high(image):
    filter = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
    return convolution(image, filter, 3)


def filter_laplace(image):
    filter = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    return convolution(image, filter, 3)


def filter_prewitt(image, size):
    new_image = clone(image)
    if (size % 2 == 0):
        size += 1
    filterh = [[i for i in range(-size // 2, size // 2 + 1)] for j in range(size)]
    filterv = [[j for i in range(0, size)] for j in range(-size // 2, size // 2 + 1)]
    prewitth= convolution(image, filterh, size)
    prewittv = convolution(image, filterv, size)
    for h in range(s.height):
        for w in range(s.width):
            conv=(prewitth[h][w]**2 + prewittv[h][w]**2)**0.5
            if (conv < 0):
                conv = 0
            if (conv > s.graylevel):
                conv = s.graylevel
            new_image[h][w]=int(conv)
    return new_image
