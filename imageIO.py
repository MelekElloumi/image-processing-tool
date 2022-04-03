
def readPGM(filepath):
    file = open(filepath,'r')
    #print(file.readline())
    if file.readline() == "P2\n":
        while True:
            line = file.readline()
            if line[0] != '#': break
        dimx,dimy=line.split()
        dimx,dimy=int(dimx),int(dimy)
        nivg=file.readline()
        data=[]
        for line in file:
            for x in line.split():
                data.append(int(x))
        if len(data) != dimx*dimy:
            print ('readPGM: error with ' + filepath + ': has wrong size')
        file.close()
        return (data,dimx,dimy,nivg)
    else:
        print('readPGM: error with '+ filepath + ': unsupported format')
    file.close()
    return None

def writePGM(filepath,image):
    #image is a tuple of (data,width,height,graylevel)
    file = open(filepath, "w")
    file.write("P2\n")
    file.write("#output image created by image-processing-tool, Melek Elloumi\n")
    file.write(str(image[1])+" "+str(image[2])+"\n")
    file.write(str(image[3]))
    for i in range(len(image[0])):
        file.write(str(image[0][i])+"\t")
        if((i+1)%17==0):
            file.write("\n")
    file.close()


