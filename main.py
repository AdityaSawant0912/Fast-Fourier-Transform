# Python 3
# Aditya Sawant

# Imports
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

# Import Images
left = imread('vertical.jpg')
right = imread('horizontal.jpg')

# Show both Images
plt.imshow(left)
plt.show()
plt.imshow(right)
plt.show()

# Convert and show both Grayscaled Images
dark_image_grey_left = rgb2gray(left)
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(dark_image_grey_left, cmap='gray');
plt.show()

dark_image_grey_right = rgb2gray(right)
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(dark_image_grey_right, cmap='gray');
plt.show()

# Convert and show both Transformed Images
dark_image_grey_fourier_left = np.fft.fftshift(np.fft.fft2(left))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(dark_image_grey_fourier_left)), cmap='gray');
plt.show()

dark_image_grey_fourier_right = np.fft.fftshift(np.fft.fft2(right))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(dark_image_grey_fourier_right)), cmap='gray');
plt.show()

