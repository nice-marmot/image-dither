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
        
def bayer_dithering(im_source, palette):
    # bayer_matrix = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]])/16
    bayer_matrix = np.array([
    [0, 32, 8, 40, 2, 34, 10, 42],
    [48, 16, 56, 24, 50, 18, 58, 26],
    [12, 44, 4, 36, 14, 46, 6, 38],
    [60, 28, 52, 20, 62, 30, 54, 22],
    [3, 35, 11, 43, 1, 33, 9, 41],
    [51, 19, 59, 27, 49, 17, 57, 25],
    [15, 47, 7, 39, 13, 45, 5, 37],
    [63, 31, 55, 23, 61, 29, 53, 21]
    ])/64
    new_image = np.zeros((len(im_source), len(im_source[0])))
    for i in range(1,len(im_source)-1):
        for j in range(1,len(im_source[0])-1):
            new_color = im_source[i][j] + 8*bayer_matrix[i%8][j%8]
            val = np.argmin(abs(new_color - palette))
            new_image[i][j] = palette[val]
    return new_image
    
def whitenoise_dithering(im_source, palette):
    new_image = np.zeros((len(im_source), len(im_source[0])))
    for i in range(1,len(im_source)-1):
        for j in range(1,len(im_source[0])-1):
            new_color = im_source[i][j] -10 + 20*np.random.rand(1,1)
            val = np.argmin(abs(new_color - palette))
            new_image[i][j] = palette[val]
    return new_image

image = np.array(Image.open('20211003_134230.jpg').convert('L'))

palette = np.round(np.linspace(0, 255, 5))

# closest value mapping
CV_image = closest_value(image, palette)

# Floyd-Steinberg dithering
FS_image = floyd_steinberg(image, palette)

# Bayer dithering / ordered dithering
OD_image = bayer_dithering(image, palette)

# Gaussian noise
WN_image = whitenoise_dithering(image, palette)

pyplot.imsave("outputs/greyscale.png", image, cmap='Greys_r')
pyplot.imsave("outputs/closest_value.png", CV_image, cmap='Greys_r')
pyplot.imsave("outputs/floyd_steinberg.png", FS_image, cmap='Greys_r')
pyplot.imsave("outputs/ordered_dithering.png", OD_image, cmap='Greys_r')
pyplot.imsave("outputs/whitenoise_dithering.png", WN_image, cmap='Greys_r')