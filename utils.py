def arrayToMatrix(imageArray, height, width):
    imageMatrix = []
    for i in range(width):
        imageRow = []
        for j in range(height):
            imageRow.append(imageArray[i * height + j])
        imageMatrix.append(imageRow)
    return imageMatrix


def matrixToArray(imageMatrix, height, width ):
    imageArray=[]
    for i in range(height):
        for j in range(width):
            imageArray.append(imageMatrix[i][j])
    return imageArray