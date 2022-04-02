import imageIO

class ImagePgm:
    def __init__(self, filepath):
        self.read(filepath)

    def read(self,filepath):
        image=imageIO.readPGM(filepath)
        if (image==None):
            print("File not found")
        else:
            self.pixels,self.width,self.height,self.graylevel=image[0],image[1],image[2],image[3]
            self.pixels=self.arrayToMatrix(self.pixels)

    def arrayToMatrix(self,imageArray):
        imageMatrix=[]
        for i in range(self.height):
            imageRow=[]
            for j in range(self.width):
                imageRow.append(imageArray[i*self.width+j])
            imageMatrix.append(imageRow)
        return imageMatrix