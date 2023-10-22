# ad1
# from PIL import ImageColor

# def rgb2cmyk(rgb):
#     r = rgb[0]/255
#     g = rgb[1]/255
#     b = rgb[2]/255
#     k = int(1-max(r,g,b))
#     one_minus_k = 1-k if 1-k > 0 else 1
#     c = int((1-r-k)/one_minus_k * 100)
#     m = int((1-g-k)/one_minus_k * 100)
#     y = int((1-b-k)/one_minus_k * 100)
#     cmyk = (c, m, y, k)
#     return cmyk

# def rgb2hsv(rgb):
#     r = rgb[0]/255
#     g = rgb[1]/255
#     b = rgb[2]/255
#     c_max = max(r, g, b)
#     c_min = min(r, g, b)
#     delta = c_max - c_min
#     if delta==0:
#         h = 0
#     elif c_max==r:
#         h = round(60 * ((g-b/delta) % 6))
#     elif c_max==g:
#         h = round(60 * ((b-r/delta) + 2))
#     elif c_max==b:
#         h = round(60 * ((r-g/delta) + 4))
#     if c_max==0:
#         s = 0
#     elif c_max!=0:
#         s = int((delta/c_max)*100)
#     v = int(c_max*100)
#     hsv = (h,s,v)
#     return hsv

# color = input("Podaj kolor do konwersji: ")
# try:
#     color = ImageColor.getrgb(color)
#     print("RGB: " + str(color))
#     cmyk = rgb2cmyk(color)
#     print("CMYK [%]: " + str(cmyk))
#     hsv = rgb2hsv(color)
#     print("HSV [deg,%,%]: " + str(hsv))
# except ValueError:
#     print("Podałeś błędną warość koloru do konwersji!")


# ad2

from PIL import Image

path = "E:\GIT\python_projects\PYTHON\hc_course\zajecia11\\"
name = "2corgi"
extension = ".jpg"

full_path = path + name + extension
# print(full_path)

img = Image.open(full_path)
width, height = img.width, img.height

print(width, height)

name_medium = name + "_medium" + extension
name_small = name + "_small" + extension
name_tiny = name + "_tiny" + extension
print(name_medium)


scale_medium = 0.50
img_small = img.resize((int(scale_medium*width), int(scale_medium*height)))
img_small.save(name_medium)



scale_small = 0.25
img_small = img.resize((int(scale_small*width), int(scale_small*height)))
img_small.save(name_small)


height_tiny = 100
width_tiny = width
print(height_tiny)
print(width_tiny)

width_tiny = int((height_tiny*width)/height_tiny)

print(width_tiny)
# img_small = img.resize(width, height_tiny)

img_small = img.resize(size=(width_tiny, height_tiny), resample=Image.Resampling.NEAREST)

img_small.save(name_tiny)


# ValueError: Unknown resampling filter (100). Use Image.Resampling.NEAREST (0),
# Image.Resampling.LANCZOS (1), Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3),
# Image.Resampling.BOX (4) or Image.Resampling.HAMMING (5)



# img_small.show()

















