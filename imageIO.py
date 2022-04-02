
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