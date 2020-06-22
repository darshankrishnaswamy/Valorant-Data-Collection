from PIL import Image

i1 = Image.open("bruh.jpg")
i2 = Image.open("bruh1.jpg")
assert i1.mode == i2.mode
assert i1.size == i2.size

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    dif = sum(abs(p1 - p2) for p1, p2 in pairs)
else:
    dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
