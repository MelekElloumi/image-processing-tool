import settings as s
import utils


def read(filepath):
    type = readType(filepath)
    if (type == None):
        raise Exception
    if (type == "P2\n"):
        imageread, s.width, s.height, s.graylevel = readPGMascii(filepath)
    else:
        imageread, s.width, s.height, s.graylevel = readPGMbinary(filepath)
    if (imageread == None):
        raise Exception
    else:
        s.isread = True
        s.image_orig = utils.arrayToMatrix(imageread, s.width, s.height)


def readType(filepath):
    try:
        file = open(filepath, 'r')
        type = file.readline()
    except UnicodeDecodeError:
        file = open(filepath, 'rb')
        type = file.readline().decode()
    if not ("P2" in type or "P5" in type):
        file.close()
        return None
    file.close()
    return type


def readPGMascii(filepath):
    file = open(filepath, 'r')
    file.readline()
    while True:
        line = file.readline()
        if line[0] != '#': break
    dimx, dimy = line.split()
    dimx, dimy = int(dimx), int(dimy)
    nivg = int(file.readline())
    imageread = []
    for line in file.readlines():
        for num in line.split():
            imageread.append(int(num))
    if len(imageread) != dimx * dimy:
        file.close()
        return None, -1, -1, -1
    file.close()
    return imageread, dimx, dimy, nivg


def readPGMbinary(filepath):
    file = open(filepath, 'rb')
    file.readline()
    while True:
        line = file.readline().decode()
        if line[0] != '#': break
    dimx, dimy = line.split()
    dimx, dimy = int(dimx), int(dimy)
    nivg = int(file.readline().decode())
    imageread = []
    imageread = list(file.read(dimx * dimy))
    if len(imageread) != dimx * dimy:
        file.close()
        return None, -1, -1, -1
    file.close()
    return imageread, dimx, dimy, nivg


def write(filepath, image):
    data = utils.matrixToArray(image, s.height, s.width)
    writePGM(filepath, data)


def writePGM(filepath, image):
    # image is a tuple of (data,width,height,graylevel)
    file = open(filepath, "w")
    file.write("P2\n")
    file.write("#output image created by image-processing-tool, Melek Elloumi\n")
    file.write(str(s.width) + " " + str(s.height) + "\n")
    file.write(str(s.graylevel) + "\n")
    for num in range(0, len(image)):
        # file.write(str(num)+"\t")
        file.write(str(image[num]) + " ")
        if ((num + 1) % s.width == 0):
            file.write("\n")
    file.close()
