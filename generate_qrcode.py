import qrcode
from PIL import Image

# Meminta input dari pengguna
link = input("Masukkan link untuk QR code: ")

# Membuat QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Membuat gambar QR code
img = qr.make_image(fill_color="black", back_color="white")

# Menampilkan gambar QR code
img.show()
