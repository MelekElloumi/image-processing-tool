import imageIO
import utils

class ImagePgm:
    def __init__(self, filepath):
        self.read(filepath)

    def read(self, filepath):
        image = imageIO.readPGM(filepath)
        if (image == None):
            print("File not found")
        else:
            data, self.width, self.height, self.graylevel = image[0], image[1], image[2], image[3]
            self.pixels = utils.arrayToMatrix(data, self.width, self.height)

    def write(self, filepath):
        data=utils.matrixToArray(self.pixels, self.width, self.height)
        imageIO.writePGM(filepath, (data ,self.width, self.height, self.graylevel))
