import cv2

citra = cv2.imread("img/img6.png")

# mengubah ukuran gambar original
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize = cv2.resize(citra, dim, interpolation=cv2.INTER_LINEAR)

#cv2.GaussianBlurr(image, kernel_size, sigmaX, sigmaY)
# Kernel_size: width dan height daripada kernel (bilangan ganjil positif).
# SigmaX: Gaussian kernel standard deviation untuk X.
# SigmaY: Gaussian kernel standard deviation untuk Y; JIka sigmaY = nol, maka akan diset sama dengan sigmaX, jika kedua sigma = nol, sigma akan dihitung dari kernel_size width dan height.

# Gausian Blur
Gaussian_blur = cv2.GaussianBlur(citra, (5,  5), 0)

# mengubah ukuran gambar blur
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize_Gaussianblur = cv2.resize(
    Gaussian_blur, dim, interpolation=cv2.INTER_LINEAR)


# gambar noise
cv2.imshow("Gambar Noise", citra_resize)

# tampilkan gambar yang gausianBlur
cv2.imshow("GaaussianBlur", citra_resize_Gaussianblur)

cv2.waitKey()
cv2.destroyAllWindows()
