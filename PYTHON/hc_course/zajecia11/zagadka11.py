from PIL import Image, ImageColor

def transform(img):
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = img.getpixel( (i,j) )
            if (r,g,b) == ImageColor.getrgb("#ed1c24"):
                img.putpixel( (i,j), ImageColor.getrgb("black") )
            elif (r,g,b) == ImageColor.getrgb("#3f48cc"):
                img.putpixel( (i,j), (0,0,0) )
    return img

img = Image.open("obraz.tif")
transform(img)
img.show()
