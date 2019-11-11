import qrcode


def main(data):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("./qr.png")

if __name__ == "__main__":
    main("https://chrischou2018.github.io/")