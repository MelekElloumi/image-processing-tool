from interface import showimage
import settings as s
import filters as f
import imageIO as io
import contrast as c
import stats as st

io.read("input\\mona.pgm")
print(s.graylevel,s.width,s.height)
showimage(s.image_orig)
input("1-Press Enter to continue...")
print(st.average(s.image_orig))
print(st.deviation(s.image_orig))
print(st.dynamic(s.image_orig))
print(st.entropy(s.image_orig))
print(st.histogram(s.image_orig))
print(st.cumulated_histogram(s.image_orig))
image_equalized=c.equalization(s.image_orig)
showimage(image_equalized)
input("2-Press Enter to continue...")
image_equalized=c.local_equalization(s.image_orig,5)
showimage(image_equalized)
input("3-Press Enter to continue...")
image_equalized=c.dark_dilatation(s.image_orig)
showimage(image_equalized)
print(st.SNR(image_equalized))
input("4-Press Enter to continue...")
filtered_image=f.filter_median(s.image_orig,3)
showimage(filtered_image)
input("5-Press Enter to continue...")
filtered_image=f.filter_median(s.image_orig,17)
showimage(filtered_image)
input("6-Press Enter to continue...")
filtered_image=f.filter_average(s.image_orig,17)
showimage(filtered_image)
input("7-Press Enter to continue...")
filtered_image=f.filter_laplace(s.image_orig)
showimage(filtered_image)
input("8-Press Enter to continue...")
#image.write("output\\test.pgm")

