from ImagePgm import ImagePgm
import matplotlib.pyplot as plt

def showimage(imagepgm):
    plt.imshow(imagepgm, cmap='gray')
    plt.show()

imagepgm=ImagePgm()
imagepgm.read("input\\mona.pgm")
print(imagepgm.graylevel,imagepgm.width,imagepgm.height)
#print(imagepgm.average())
#print(imagepgm.deviation())
#print(imagepgm.dynamic())
#print(imagepgm.entropy())
print(imagepgm.histogram())
print(imagepgm.cumulated_histogram())
#new_imagepgm=ImagePgm()
#new_imagepgm.clone(imagepgm)
#new_imagepgm.image=imagepgm.egalization()
#print(new_imagepgm.histogram())
#showimage(imagepgm.image)
#showimage(imagepgm.egalization())
showimage(imagepgm.local_egalization(17))
#image.write("output\\test.pgm")
