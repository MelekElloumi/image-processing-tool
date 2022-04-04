import settings as s
from utils import clone

def binarize(image):
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            if(image[h][w]>s.graylevel/2):
                new_image[h][w] = s.graylevel
            else:
                new_image[h][w] = 0
    return new_image


