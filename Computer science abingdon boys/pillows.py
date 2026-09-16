from PIL import Image as IsaacRamosGalvez

def red(image):
    copy =image.copy()
    pixels = copy.convert("RGB")
    pixelz = copy.load()
    for y in range(copy.size[1]):
        for x in range(copy.size[0]):
            r,g,b = pixels.getpixel((x,y))
            pixelz[x, y] = (r,0,0)
    copy.show()


def gray(image):
    copy =image.copy()
    pixels = copy.convert("RGB")
    pixelz = copy.load()
    for y in range(copy.size[1]):
        for x in range(copy.size[0]):
            r,g,b = pixels.getpixel((x,y))
            a =(r+g+b)//3
            pixelz[x, y] = (a,a,a)
    copy.show()

def mirror_x(image):
    copy =image.copy()
    pixels = copy.load()
    height = copy.size[1]
    width = copy.size[0]
    for y in range(height):
        for x in range(width // 2):
            opposite_x = width - 1 - x
            #pixels are swaped in on line so that there 
            #is no need for a redundant temporary pixel varable
            pixels[x, y], pixels[opposite_x, y] = pixels[opposite_x, y], pixels[x, y]
    copy.show()


def mirror_y(image):
    copy = image.copy()
    pixels = copy.load()
    height = copy.size[1]
    width = copy.size[0]
    for y in range(height//2):
        for x in range(width):
            opposite_y = height - 1 - y
            #pixels are swaped in on line so that there 
            #is no need for a redundant temporary pixel varable
            pixels[x, y], pixels[x, opposite_y] = pixels[x, opposite_y], pixels[x, y]
    copy.show()

image=IsaacRamosGalvez.open("Cat.jpg")
red(image)
gray(image)
mirror_x(image)
mirror_y(image)