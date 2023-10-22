#proste operacje odczytu/zapisu
# from PIL import Image
# img = Image.open("corgi.jpg")
# img_small = img.resize((100,200))
# img_small.save("corgi_small.jpg")
# img_small.show()


#zmina rozmiaru z zastosowaniem skali
# from PIL import Image
# img = Image.open("corgi.jpg")
# width, height = img.width, img.height
# print(width, height)
# scale = 0.25
# img_small = img.resize((int(scale*width), int(scale*height)))
# img_small.save("corgi_small.jpg")
# img_small.show()


#obrót obrazka
# from PIL import Image
# img = Image.open("corgi.jpg")
## img = img.rotate(45)    #obrót bez zmiany rozmiaru(obcięte rogi)
# img = img.rotate(45, expand = True) #obrót ze zmianą rozmiaru
# img.show()


#wklejenie obrazka na obrazek
# from PIL import Image
# img = Image.open("corgi.jpg")
# imgicon = Image.open("corgi_icon.png")
# img.paste(imgicon, (20,30))
# img.show()


#rysowanie obiektów w obrazku
# from PIL import Image, ImageDraw, ImageFont
# img = Image.open("corgi.jpg")
# imgdraw = ImageDraw.Draw(img)
# imgdraw.rectangle((10,10,300,500), fill="red")
# imgdraw.line((50,50,400,500), width=5, fill="Green")
# imgdraw.ellipse((10,10,400,400), fill = "purple")
# imgdraw.arc((200,200,400,400), start = 10, end=180, width=5,fill ="blue")
# font = ImageFont.truetype("arial", 100)
# imgdraw.text((10,10), "Hello World", font=font, fill="white")
# img.show()


# konwersja obrazka
# from PIL import Image
# img = Image.open("corgi_poster.png")
# img = img.convert("1") #np. 1- obraz binarny, RGB -konwersja na RGB
# img.show()


# stosowanie filtrów
# from PIL import Image, ImageFilter
# img = Image.open("corgi.jpg")
##img = img.filter(ImageFilter.GaussianBlur(radius=2)) #przykładowy filtr rozmycie gausowskie o promieniu 2
# img = img.filter(ImageFilter.MedianFilter(size=7)) #filtr medianowy z maska 7x7
# img.show()


# pobieranie wartości kolorów z modelu HTML
# from PIL import ImageColor
# print(ImageColor.getrgb("lime")) #html lime = green 255
# print(ImageColor.getcolor("pink", "RGBA"))


# odczyt wartości pikseli z obrazka
# from PIL import Image
# img = Image.open("corgi_greenscreen.jpg")
##print(img.getpixel( (5,10) )) #kolor konkretnego pixela
# for x in range(img.width):
#     for y in range(img.height):
#         print(img.getpixel( (x,y) ))


#reczna zmiana na skalę szarości
# from PIL import Image
# img = Image.open("corgi.jpg")
# for x in range(img.width):
#     for y in range(img.height):
#         r,g,b = img.getpixel( (x,y) )
#         grey = int( (r+g+b)/3 ) #średnia kanałów
#         img.putpixel((x,y), (grey, grey, grey))
# img.show()


#zmiana na obraz binarny
# from PIL import Image, ImageColor
# img = Image.open("corgi_poster.png")
# threshold = 200
# for x in range(img.width):
#     for y in range(img.height):
#         r,g,b = img.getpixel((x,y))
#         grey = int((r+g+b)/3)
          ##pixele powyżej progu będą białe a poniżej czarne:
#         val = ImageColor.getrgb("white") if grey > threshold else ImageColor.getrgb("black")
#         img.putpixel((x,y), val)
# img.show()


#ręczna zamiana na sepię
# from PIL import Image
# img = Image.open("corgi.jpg")
# width, height = img.width, img.height
# for x in range(width):
#     for y in range(height):
#         r,g,b = img.getpixel( (x,y) )
        ## algorytm zamiany na sepie od Microsoftu
#         rs = int(0.393*r + 0.769*g + 0.189*b)
#         gs = int(0.349*r + 0.686*g + 0.168*b)
#         bs = int(0.272*r + 0.534*g + 0.131*b)
#         img.putpixel( (x,y), (rs,gs,bs) )
# img.show()


#zliczanie występowania kolorów(kolor dominujący)
# from PIL import Image
# img = Image.open("corgi_greenscreen_mini.jpg") #obrazek niewielki bo operacja czasochłonna
# width, height = img.width, img.height


##pobieranie wszystkich kolorów obrazka do listy:
# all_colors = []
# for x in range(width):
#     for y in range(height):
#         all_colors.append(img.getpixel( (x,y) ))
##inny zapis - list comprehension:
##all_colors = [img.getpixel((x,y)) for y in range(height) for x in range(width)]

# unique_colors = set(all_colors)
# color_counts = dict()
# for color in unique_colors:
#     if all_colors.count(color) > 20:
#         color_counts[color] = all_colors.count(color)
# print(color_counts)


#zamiana koloru dominującego(tła)
# from PIL import Image, ImageColor
# img = Image.open("corgi_greenscreen.jpg")
# width, height = img.width, img.height
# for x in range(width):
#     for y in range(height):
        ##zamina koloru dominujacego na czerowny
#         if img.getpixel( (x,y) ) == (85, 255, 133): #zamiana koloru dominującego na czerwony
#             img.putpixel( (x,y), ImageColor.getrgb("red") )
# img.show()


#zamiana koloru dominującego(tła) z tolerancją
from PIL import Image, ImageColor
img = Image.open("corgi_greenscreen.jpg")
width, height = img.width, img.height
r0,g0,b0 = (85,255,133)
tol = 50

for x in range(width):
    for y in range(height):
        r,g,b = img.getpixel( (x,y) )
        if abs(r-r0) < tol and abs(g-g0) < tol and abs(b-b0) < tol:
            img.putpixel( (x,y), ImageColor.getrgb("red") )
img.show()
