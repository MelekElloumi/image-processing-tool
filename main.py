from ImagePgm import ImagePgm
import matplotlib.pyplot as plt

def showimage(imagepgm):
    plt.imshow(imagepgm, cmap='gray')
    plt.show()

imagepgm=ImagePgm("input\\cours.pgm")
print(imagepgm.graylevel,imagepgm.width,imagepgm.height)
print(imagepgm.average())
print(imagepgm.deviation())
print(imagepgm.dynamic())
print(imagepgm.entropy())
print(imagepgm.histogram())
print(imagepgm.cumulated_histogram())

#showimage(imagepgm.pixels)
#showimage(imagepgm.inverse())
#image.write("output\\test.pgm")
