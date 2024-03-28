import cv2

citra = cv2.imread("img/img2.png")

# mengubah ukuran gambar original
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize = cv2.resize(citra, dim, interpolation=cv2.INTER_LINEAR)

# Method ini akan menghitung rata-rata pixel dibawah kernel dan mengganti nilai dari central pixel.
#  Fungsi yang digunakan adalah cv2.blur() atau cv2.boxFilter().

# Averaging
blur = cv2.blur(citra, (5, 5))

# mengubah ukuran gambar blur
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize_blur = cv2.resize(blur, dim, interpolation=cv2.INTER_LINEAR)


# tampilkan gambar original
cv2.imshow("Gambar original", citra_resize)

# tampilkan gambar yang blur
cv2.imshow("Gambar Blur", citra_resize_blur)

cv2.waitKey()
cv2.destroyAllWindows()
