from PIL import Image
import numpy as np


im = Image.open(r"C:\Users\Jake\Pictures\ascii-pineapple.jpg")
im.thumbnail([500,325])
pixels=np.array(im)

brightness = []

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for x in range(len(pixels)):
    brightness.append([])
    for y in range(len(pixels[x])):
        brt = (0.21*pixels[x][y][0] + 0.72*pixels[x][y][1] + 0.07*pixels[x][y][2])
        brightness[x].append(chars[round(brt/3.95)])



for x in range(len(brightness)):
    print(*brightness[x], sep="")