from tkinter.tix import Tree
from PIL import Image

width = 400
height = 200

def gen_primes(p):
    for i in range(2, width*height):
        prime = True
        for entry in p:
            if i % entry == 0:
                prime = False
        if prime:
            p.append(i)

primes = []
gen_primes(primes)
print("Prime List Generated")

img = Image.new('1', (width, height))
for x in range(1, width+1):
    for y in range(height):
        current_num = x + 10*y
        if current_num in primes:
            img.putpixel((x,y),1)
filename = 'prime_square_' + str(width) + 'x' + str(height) + '.png'
img.save(filename)

print("Image File Generated")
