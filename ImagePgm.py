import imageIO
import utils
import math

class ImagePgm:
    def __init__(self, filepath):
        self.read(filepath)

    def read(self, filepath):
        imagepgm = imageIO.readPGM(filepath)
        if (imagepgm == None):
            print("File not found")
        else:
            data, self.width, self.height, self.graylevel = imagepgm[0], imagepgm[1], imagepgm[2], imagepgm[3]
            self.image = utils.arrayToMatrix(data, self.width, self.height)

    def write(self, filepath):
        data=utils.matrixToArray(self.image, self.width, self.height)
        imageIO.writePGM(filepath, (data ,self.width, self.height, self.graylevel))

    def nbPixels(self):
        return self.height*self.width

    def average(self):
        avg = 0
        for h in range(self.height):
            for w in range(self.width):
                avg += self.image[h][w]
        return avg / self.nbPixels()

    def deviation(self):
        avg = self.average()
        dev = 0
        for h in range(self.height):
            for w in range(self.width):
                dev += (self.image[h][w] - avg) ** 2
        return math.sqrt(dev / self.nbPixels())

    def histogram(self):
        hist=[0]*(self.graylevel+1)
        for h in range(self.height):
            for w in range(self.width):
                hist[self.image[h][w]] += 1
        return hist

    def cumulated_histogram(self):
        hist=self.histogram()
        cum_hist=[0]*(self.graylevel+1)
        cum_hist[0]=hist[0]
        for g in range(1,self.graylevel+1):
            cum_hist[g]=hist[g]+cum_hist[g-1]
        return cum_hist

    def entropy(self):
        hist=self.histogram()
        ent=0
        for h in range(self.graylevel+1):
            p=hist[h]/self.nbPixels()
            ent+=p*math.log2(1/p)
        return ent

    def dynamic(self):
        hist = self.histogram()
        dmin,dmax=0,self.graylevel
        for h in range(self.graylevel+1):
            if (hist[h]==0):
                continue
            else:
                dmin=h
                break
        for h in reversed(range(self.graylevel+1)):
            if (hist[h]==0):
                continue
            else:
                dmax=h
                break
        return dmin,dmax

    def inverse(self):
        new_image=self.image.copy()
        for h in range(self.height):
            for w in range(self.width):
                new_image[h][w]=self.graylevel-self.image[h][w]
        return new_image

    """
    def egalization(self):
        cum_hist=self.cumulated_histogram()
        new_= [0] * (self.graylevel + 1)
    """


