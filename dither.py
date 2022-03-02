import numpy as np
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from sklearn.cluster import KMeans

def generate_palette(image, k):
    return 

def closest_value(im_source, palette):
    new_image = np.zeros((len(im_source), len(im_source[0])))
    for i in range(len(im_source)):
        for j in range(len(im_source[0])):
            val = np.argmin(abs(im_source[i][j] - palette))
            new_image[i][j] = palette[val]
    return new_image
    
def floyd_steinberg(im_source, palette):
    new_image = np.zeros((len(im_source), len(im_source[0])))
    errors = np.zeros((len(im_source), len(im_source[0])))
    for i in range(1,len(im_source)-1):
        for j in range(1,len(im_source[0])-1):
            val = np.argmin(abs(im_source[i][j] - palette + errors[i][j]))
            err = (im_source[i][j] - palette[val])/16
            errors[i][j+1] = 7*err
            errors[i+1][j-1] = 1*err
            errors[i+1][j] = 5*err
            errors[i+1][j+1] = 3*err
            new_image[i][j] = palette[val]
    return new_image

image = np.array(Image.open('20211003_134230.jpg').convert('L'))

image = 1 - image

palette = np.linspace(0, 255, 5)

FS_image = floyd_steinberg(image, palette)

CV_image = closest_value(image, palette)

plt1 = pyplot.figure(1)
pyplot.imshow(FS_image)
pyplot.axis('off')
pyplot.set_cmap('Greys')

plt1 = pyplot.figure(2)
pyplot.imshow(CV_image)
pyplot.axis('off')
pyplot.set_cmap('Greys')

pyplot.show()