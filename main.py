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
#print(imagepgm.histogram())
#print(imagepgm.cumulated_histogram())
new_imagepgm=ImagePgm()
new_imagepgm.clone(imagepgm)
#new_imagepgm.image=imagepgm.noise()
#print(new_imagepgm.histogram())
#showimage(imagepgm.image)
#showimage(imagepgm.egalization())
#print(imagepgm.image)
filtered_image=new_imagepgm.filter_gauss(17)
#print(filtered_image)
showimage(filtered_image)
#image.write("output\\test.pgm")
