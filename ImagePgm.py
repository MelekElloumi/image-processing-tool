import imageIO
import utils
import math

class ImagePgm:

    def read(self, filepath):
        imagepgm = imageIO.readPGM(filepath)
        if (imagepgm == None):
            print("File not found")
        else:
            data, self.width, self.height, self.graylevel = imagepgm[0], imagepgm[1], imagepgm[2], imagepgm[3]
            self.image = utils.arrayToMatrix(data, self.width, self.height)

    def clone(self,imagepgm2):
        self.image=imagepgm2.image
        self.width=imagepgm2.width
        self.height=imagepgm2.height
        self.graylevel=imagepgm2.graylevel

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
        for g in range(self.graylevel+1):
            p=hist[g]/self.nbPixels()
            ent+=p*math.log2(1/p)
        return ent

    def dynamic(self):
        hist = self.histogram()
        dmin,dmax=0,self.graylevel
        for g in range(self.graylevel+1):
            if (hist[g]==0):
                continue
            else:
                dmin=g
                break
        for g in reversed(range(self.graylevel+1)):
            if (hist[g]==0):
                continue
            else:
                dmax=g
                break
        return dmin,dmax

    def egalization(self):
        cum_hist=self.cumulated_histogram()
        LUT= [0] * (self.graylevel + 1)
        for g in range(self.graylevel + 1):
            LUT[g]=int(self.graylevel*cum_hist[g]/self.nbPixels())
        new_image = self.image.copy()
        for h in range(self.height):
            for w in range(self.width):
                new_image[h][w]=LUT[self.image[h][w]]
        return new_image

    def local_egalization(self,size):
        if (size%2==0):
            size+=1
        new_image = self.image.copy()
        for h in range(self.height):
            for w in range(self.width):
                histc=0
                nbp=0
                for py in range(max(0,h-size//2),min(self.height,h+size//2+1)):
                    for px in range(max(0, w - size // 2), min(self.width, w + size // 2 + 1)):
                        if(self.image[py][px]<=self.image[h][w]):
                            histc+=1
                        nbp += 1
                new_image[h][w] = int(self.graylevel * histc / nbp)
        return new_image






    def linear_transformation(self,points):
        LUT= [0] * (self.graylevel + 1)
        for p in range(1,len(points)):
            slope = (points[p][1] - points[p - 1][1]) / (points[p][0] - points[p - 1][0])
            intercept = points[p][1] - slope * points[p][0]
            for g in range(points[p-1][0],points[p][0]+1):
                LUT[g]=int(slope*g+intercept)
        new_image = self.image.copy()
        for h in range(self.height):
            for w in range(self.width):
                new_image[h][w] = LUT[new_image[h][w]]
        return new_image

    def dark_dilatation(self):
        points=[
            [0,0],
            [int(self.graylevel/4),int(self.graylevel/2)],
            [self.graylevel,self.graylevel]
        ]
        return self.linear_transformation(points)

    def inverse(self):
        points = [
            [0, self.graylevel],
            [self.graylevel, 0]
        ]
        return self.linear_transformation(points)

    def light_dilatation(self):
        points = [
            [0, 0],
            [int(self.graylevel / 2), int(self.graylevel / 4)],
            [self.graylevel, self.graylevel]
        ]
        return self.linear_transformation(points)

    def middle_dilatation(self):
        points = [
            [0, 0],
            [int(self.graylevel / 3), int(self.graylevel / 6)],
            [int(self.graylevel * 2 / 3), int(self.graylevel * 5 / 6)],
            [self.graylevel, self.graylevel]
        ]
        return self.linear_transformation(points)

    def binarize(self):
        new_image = self.image.copy()
        for h in range(self.height):
            for w in range(self.width):
                if(self.image[h][w]>self.graylevel/2):
                    new_image[h][w] = self.graylevel
                else:
                    new_image[h][w] = 0
        return new_image



