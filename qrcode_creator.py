import qrcode

def generate_qr_code(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
link = "https://example.com"
filename = "qrcode.png"

generate_qr_code(link, filename)
print(f"QR code generated and saved as {filename}")
