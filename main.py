from interface import showimage
import settings as s
import filters as f
import imageIO as io
import contrast as c
import stats as st
import binary as b

s.isread=False
io.read("input\\melek.pgm")
imagethresh=b.thresholding(s.image_orig)
showimage(s.image_orig,"otsu threshold")
showimage(imagethresh,"otsu threshold")
#io.write("output\\ascii.txt",imageascii)
"""
print(s.graylevel,s.width,s.height)
showimage(s.image_orig,"original")
input("1-Press Enter to continue...")
print(st.average(s.image_orig))
print(st.deviation(s.image_orig))
print(st.dynamic(s.image_orig))
print(st.entropy(s.image_orig))
print(st.histogram(s.image_orig))
print(st.cumulated_histogram(s.image_orig))
image_binarized=b.binarize(s.image_orig,0.5)
showimage(image_binarized,"binarization")
input("12-Press Enter to continue...")
image_equalized=c.equalization(s.image_orig)
showimage(image_equalized,"equalization")
input("2-Press Enter to continue...")
image_equalized=c.local_equalization(s.image_orig,5)
showimage(image_equalized,"local equalization 5")
input("3-Press Enter to continue...")
image_equalized=c.dark_dilatation(s.image_orig)
showimage(image_equalized,"dark dilatation")
print(st.SNR(image_equalized))
input("4-Press Enter to continue...")
filtered_image=f.filter_median(s.image_orig,3)
showimage(filtered_image,"median 3")
input("5-Press Enter to continue...")
filtered_image=f.filter_median(s.image_orig,17)
showimage(filtered_image,"median 17")
input("6-Press Enter to continue...")
filtered_image=f.filter_average(s.image_orig,17)
showimage(filtered_image,"average 17")
input("7-Press Enter to continue...")
filtered_image=f.filter_gauss(s.image_orig,17)
showimage(filtered_image,"gauss 17")
input("8-Press Enter to continue...")
filtered_image=f.filter_laplace(s.image_orig)
showimage(filtered_image,"laplace")
input("9-Press Enter to continue...")
"""