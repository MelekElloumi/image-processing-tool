import matplotlib.pyplot as plt

def showimage(image,title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.show()