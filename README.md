# Image Processing Tool 

- This is a Python application that lets you open .pgm files and edit them.
- Edits include contrast manipulation, filtering and thresholding functions.
- You can also add random noise and generate an ascii art from you image (find it in output folder)
- To execute it, run the image_processing_tool.bat file.

## Interface
- It's made with python tkinter
- Images and histograms are shown using matplotlib.Figure.
- The image statistics are automatically calculated after each operation.
- When you choose manual transformation in the contrast menu, a new window will appear that will allow you to add points to the transformation graph and visiualise it.

### Execution:
![2014-10-22 11_35_09](https://media1.giphy.com/media/3lRoMhENgQhoWJ8MfJ/giphy.gif?cid=790b7611fd80a93158743023960bfac43c7088f922f64f92&rid=giphy.gif&ct=g)

### Input images
- You can find sample images in the input folder (including me)
- The application can read ascii and binary pgm files. It saves in ascii mode.
- To add your photo, you can convert a jpeg to pgm in this online [converter](https://convertio.co/fr/jpg-pgm/).

#### Ascii art 
- lena.pgm in ascii form
![Imgur](https://i.imgur.com/7khn6Wt.png)
