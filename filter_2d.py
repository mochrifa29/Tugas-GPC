# importing all the required modules
import numpy as np
import cv2 as cv

gambar_ori = cv.imread('img/img2.png')

# reading the image that is to be blurred using imread() function
imageread = cv.imread('img/img2.png')

# defining the matrix for kernel to apply filter2d() function on the image to blur the image
kernelmatrix = np.ones((5, 5), np.float32)/25
# applying filter2d() function on the image to blur the image and display it as the output on the screen
resultimage = cv.filter2D(imageread, -1, kernelmatrix)
cv.imshow('Averaging', resultimage)
cv.imshow('Gambar original', gambar_ori)
cv.waitKey(0)
cv.destroyAllWindows()
