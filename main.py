from stats import *
from ImagePgm import ImagePgm

image=ImagePgm("input\\examplePGM1.pgm")
print(image.width,image.height,image.graylevel)
print(image.pixels)
print(image.pixels[0][1])