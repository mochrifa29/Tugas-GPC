import cv2

citra = cv2.imread("img/img6.png")

# mengubah ukuran gambar original
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize = cv2.resize(citra, dim, interpolation=cv2.INTER_LINEAR)

# Median Blur menggunakan nilai median pada pixel yang berada dibawah kernel area.
# Sangat efektif untuk menghilangkan noise pada sebuah image.
# Ukuran kernel harus bilangan ganjil positif.

# Median Blur
medianBlur = cv2.medianBlur(citra, 5)

# mengubah ukuran gambar blur
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize_Medianblur = cv2.resize(
    medianBlur, dim, interpolation=cv2.INTER_LINEAR)


# gambar noise
cv2.imshow("Gambar Noise", citra_resize)

# tampilkan gambar yang gausianBlur
cv2.imshow("Median Blur", citra_resize_Medianblur)

cv2.waitKey()
cv2.destroyAllWindows()
