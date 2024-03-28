import cv2

# membaca citra digital dari komputer
citra = cv2.imread("img/img2.png")

# menampilkan citra digital yang sudah dibaca
cv2.imshow("Albert Einstein", citra)

# BGR ( blue,green,red) => (0,1,2)
# cv2.imshow("gambar red", citra[:, :, 2])
# cv2.imshow("gambar green", citra[:, :, 1])
# cv2.imshow("gambar blue", citra[:, :, 0])

# mengubah ukuran gambar
widht = 300
heigth = 300
dim = (widht, heigth)
citra_new = cv2.resize(citra, dim, interpolation=cv2.INTER_LINEAR)

# menampilkan citra digital yang sudah di ubah ukuran nya
cv2.imshow("Albert Einstein resize", citra_new)


# menyimpan citra digital
cv2.imwrite("simpan gambar/Einstein.jpg", citra)

# menampilkan matriks dari citra
print(citra)  # print semua chanel warna
print("")
print("")

print("Blue")
print(citra[:, :, 0])  # print chanel warna biru
print("")
print("Green")
print(citra[:, :, 1])  # print chanel warna green
print("")
print("Red")
print(citra[:, :, 2])  # print chanel warna red


# menunggu sampai user menekan sembaramg tombol
cv2.waitKey()

cv2.destroyAllWindows()
