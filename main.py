from tkinter.tix import Tree
from PIL import Image
import number_generators as numgen

width = 200
height = 200

size = width*height
primes = numgen.gen_primes(size)
print("Prime List Generated")

img = Image.new('1', (width, height))
for prime in primes:
    y = prime // width
    x = prime - (width*y) - 1
    if x > 1919 or y > 1079:
        print(x,y)
    img.putpixel((x,y),1)
filename = 'primes_' + str(width) + 'x' + str(height) + '.png'
img.save(filename)

print("Image File Generated")
