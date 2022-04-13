import random


def arrayToMatrix(Array, height, width):
    Matrix = []
    for w in range(width):
        Row = []
        for h in range(height):
            Row.append(Array[w * height + h])
        Matrix.append(Row)
    return Matrix


def matrixToArray(Matrix, height, width):
    Array = []
    for h in range(height):
        for w in range(width):
            Array.append(Matrix[h][w])
    return Array


def clone(Matrix):
    return [row[:] for row in Matrix]


def noise(Matrix, width, height, val):
    new_Matrix = clone(Matrix)
    for h in range(height):
        for w in range(width):
            x = random.randint(0, 20)
            if (x == 0):
                new_Matrix[h][w] = 0
            if (x == 20):
                new_Matrix[h][w] = val
    return new_Matrix


def ascii(image, width, height):
    new_image = clone(image)
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    for h in range(height):
        for w in range(width):
            new_image[h][w] = chars[new_image[h][w] // 25]
    return new_image
