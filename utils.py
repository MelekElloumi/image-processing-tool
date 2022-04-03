def arrayToMatrix(Array, height, width):
    Matrix = []
    for w in range(width):
        Row = []
        for h in range(height):
            Row.append(Array[w * height + h])
        Matrix.append(Row)
    return Matrix


def matrixToArray(Matrix, height, width ):
    Array=[]
    for h in range(height):
        for w in range(width):
            Array.append(Matrix[h][w])
    return Array
