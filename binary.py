import settings as s
from utils import clone
from stats import histogram
from stats import cumulated_histogram
import math

def binarize(image,threshold):
    new_image = clone(image)
    for h in range(s.height):
        for w in range(s.width):
            if(image[h][w]>threshold):
                new_image[h][w] = s.graylevel
            else:
                new_image[h][w] = 0
    return new_image

def thresholding(image):
    hist=histogram(image)
    cum_hist=cumulated_histogram(image)
    fmin=math.inf
    thmin=-1
    for i in range(0,s.graylevel+1):
        q1,q2=cum_hist[i],cum_hist[s.graylevel]-cum_hist[i]
        if q1<1.e-6 or q2<1.e-6:
            continue
        m1,m2,v1,v2=0,0,0,0
        for g in range(0,i+1):
            m1+=g*hist[g]/s.graylevel
        m1=m1/q1
        for g in range(0,i+1):
            v1+=((g-m1)**2)*hist[g]/s.graylevel
        v1=v1/q1
        for g in range(i+1,s.graylevel+1):
            m2+=g*hist[g]/s.graylevel
        m2 = m2 / q2
        for g in range(i+1,s.graylevel+1):
            v2 += ((g - m2) ** 2) * hist[g] / s.graylevel
        v2 = v2 / q2
        f=v1*q1+v2*q2
        if (f<fmin):
            fmin=f
            thmin=i
    print(thmin)
    return binarize(image,thmin)

def ascii(image):
    new_image = clone(image)
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    for h in range(s.height):
        for w in range(s.width):
            new_image[h][w] = chars[new_image[h][w]//25]+" "
    return new_image


