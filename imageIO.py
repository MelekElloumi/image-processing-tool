import settings as s
import utils

def read(filepath):
    imagepgm = readPGM(filepath)
    if (imagepgm == None):
        print("File not found")
    else:
        data, s.width, s.height, s.graylevel = imagepgm[0], imagepgm[1], imagepgm[2], imagepgm[3]
        s.image_orig = utils.arrayToMatrix(data, s.width, s.height)

def readPGM(filepath):
    file = open(filepath,'r')
    #print(file.readline())
    if file.readline() == "P2\n":
        while True:
            line = file.readline()
            if line[0] != '#': break
        dimx,dimy=line.split()
        dimx,dimy=int(dimx),int(dimy)
        nivg=int(file.readline())
        data=[]
        for line in file:
            for num in line.split():
                data.append(int(num))
        if len(data) != dimx*dimy:
            print ('readPGM: error with ' + filepath + ': has wrong size')
        file.close()
        return (data,dimx,dimy,nivg)
    else:
        print('readPGM: error with '+ filepath + ': unsupported format')
    file.close()
    return None

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


