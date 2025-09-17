from PIL import Image, ImageChops
from pathlib import Path

M1 = "m1.png"
M2 = "m2.png"
KEY = "key.png"


# Load and ensure grayscale
m1 = Image.open(M1).convert("1")
m2 = Image.open(M2).convert("1")
k  = Image.open(KEY).convert("1")

# Encrypt
c1 = ImageChops.logical_xor(m1, k)
c2 = ImageChops.logical_xor(m2, k)

leak = ImageChops.logical_xor(c1, c2)


c1.save("c1.png")
c2.save("c2.png")
leak.save("xor_leak.png")
