# Simple QR Code Creator (Python)

A lightweight Python script to generate QR codes from any link or text using the [`qrcode`](https://pypi.org/project/qrcode/) library.  
Perfect for quickly creating scannable codes for websites, apps, or text.

---

## Features
- Generate QR codes from any URL or text
- Customize colors (fill and background)
- Save as PNG image
- Simple and beginner-friendly

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/MrMace/simple_qrcode_creator_python.git
cd simple_qrcode_creator_python
```

2. **Install dependencies**

```bash
pip install qrcode[pil]
```

---

## Usage

Edit the `link` and `filename` variables in `main.py`:

```python
link = "https://example.com"  # Replace with your link or text
filename = "qrcode.png"       # Output filename
```

Run the script:

```bash
python main.py
```

Your QR code will be generated and saved as an image file in the same folder.

---

## Example Output

For:

```python
link = "https://example.com"
filename = "qrcode.png"
```

You'll get a QR code like this:

![Example QR Code](qrcode.png)

---

## Customization

You can change the colors by modifying:

```python
img = qr.make_image(fill_color="black", back_color="white")
```

Example:

```python
img = qr.make_image(fill_color="blue", back_color="yellow")
```

---

