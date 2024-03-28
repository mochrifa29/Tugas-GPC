import cv2

citra = cv2.imread("img/img6.png")

# mengubah ukuran gambar original
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize = cv2.resize(citra, dim, interpolation=cv2.INTER_LINEAR)

# Bilateral Blurring efektif menghilangkan noise dan tetap menjaga edges tetap tajam.
# Namun proses memakan waktu lebih banyak dibandingkan dengan filter lainnya.

# Bilateral Blur
bilateralBlur = cv2.bilateralFilter(citra, 9, 75, 75)

# mengubah ukuran gambar blur
widht = 300
heigth = 300
dim = (widht, heigth)
citra_resize_Bilateralblur = cv2.resize(
    bilateralBlur, dim, interpolation=cv2.INTER_LINEAR)


# gambar noise
cv2.imshow("Gambar Noise", citra_resize)

# tampilkan gambar yang bilateral blur
cv2.imshow("Bilateral Blur", citra_resize_Bilateralblur)

cv2.waitKey()
cv2.destroyAllWindows()
