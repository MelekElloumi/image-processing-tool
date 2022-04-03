from stats import *
from ImagePgm import ImagePgm
import matplotlib.pyplot as plt

image=ImagePgm("input\\examplePGM1.pgm")
print(len(image.pixels[0]))
plt.imshow(image.pixels,cmap='gray')
plt.show()
#image.write("output\\test.pgm")
