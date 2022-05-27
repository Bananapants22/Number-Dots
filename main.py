from tkinter.tix import Tree
from PIL import Image

side_length = 200

def gen_primes(p):
    for i in range(2, side_length**2):
        prime = True
        for entry in p:
            if i % entry == 0:
                prime = False
        if prime:
            p.append(i)

primes = []
gen_primes(primes)
print("Prime List Generated")

img = Image.new('1', (side_length,side_length))
for x in range(1, side_length+1):
    for y in range(side_length):
        current_num = x + 10*y
        if current_num in primes:
            img.putpixel((x,y),1)
filename = 'prime_square_' + str(side_length) + '.png'
img.save(filename)

print("Image File Generated")
