import qrcode

url = "https://127.0.0.1.8000"
image = qrcode.make(url)

image.save("img.png")
