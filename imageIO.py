import settings as s
import utils

def read(filepath):
    type=readType(filepath)
    if (type == None):
        print('readType: error with ' + filepath + ': has wrong type')
        return
    if(type=="P2\n"):
        imageread,s.width,s.height,s.graylevel=readPGMascii(filepath)
    else:
        imageread,s.width,s.height,s.graylevel=readPGMbinary(filepath)
    if (imageread == None):
        print ('readPGM: error with ' + filepath + ': has wrong size')
    else:
        s.isread=True
        s.image_orig = utils.arrayToMatrix(imageread, s.width, s.height)

def readType(filepath):
    file = open(filepath, 'rb')
    type = file.readline().decode()
    if not (type == "P2\n" or type == "P5\n"):
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
    imageread=[]
    for line in file.readlines():
        for num in line.split():
            imageread.append(int(num))
    if len(imageread) != dimx*dimy:
        file.close()
        return None,-1,-1,-1
    file.close()
    return imageread,dimx,dimy,nivg

def readPGMbinary(filepath):
    file = open(filepath, 'rb')
    file.readline()
    while True:
        line = file.readline().decode()
        if line[0] != '#': break
    dimx, dimy = line.split()
    dimx, dimy = int(dimx), int(dimy)
    nivg = int(file.readline().decode())
    print(nivg,dimx,dimy)
    imageread = []
    imageread = list(file.read(dimx * dimy))
    print(len(imageread))
    if len(imageread) != dimx * dimy:
        file.close()
        return None, -1, -1, -1
    file.close()
    return imageread, dimx, dimy, nivg

def write(filepath,image):
    data=utils.matrixToArray(image, s.width, s.height)
    writePGM(filepath, (data ,s.width, s.height, s.graylevel))

def writePGM(filepath,image):
    #image is a tuple of (data,width,height,graylevel)
    file = open(filepath, "w")
    file.write("P2\n")
    file.write("#output image created by image-processing-tool, Melek Elloumi\n")
    file.write(str(image[1])+" "+str(image[2])+"\n")
    file.write(str(image[3]))
    for num in range(len(image[0])):
        file.write(str(image[0][num])+"\t")
        if((num+1)%100==0):
            file.write("\n")
    file.close()


