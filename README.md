Simple QR Code Creator (Python)

A lightweight Python script to generate QR codes from any link or text using the qrcode library.
Perfect for quickly creating scannable codes for websites, apps, or text.
Features

    Generate QR codes from any URL or text

    Customize colors (fill and background)

    Save as PNG image

    Simple and beginner-friendly

Installation

    Clone the repository

git clone https://github.com/MrMace/simple_qrcode_creator_python.git
cd simple_qrcode_creator_python

Install dependencies

    pip install qrcode[pil]

Usage

Edit the link and filename variables in main.py:

link = "https://example.com"  # Replace with your link or text
filename = "qrcode.png"       # Output filename

Run the script:

python main.py

Your QR code will be generated and saved as an image file in the same folder.
Example Output

For:

link = "https://example.com"
filename = "qrcode.png"

You'll get a QR code like this:

Example QR Code
Customization

You can change the colors by modifying:

img = qr.make_image(fill_color="black", back_color="white")

Example:

img = qr.make_image(fill_color="blue", back_color="yellow")

License

This project is licensed under the MIT License — see the LICENSE file for details.
