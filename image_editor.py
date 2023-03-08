from PIL import ImageEnhance,ImageFilter,Image
import os

path = './imgs'
pathOut='/editImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit=img.filter(ImageFilter.SHARPEN).convert('L')

    factor=1.5

    enhancer=ImageEnhance.Contrast(edit)
    edit =enhancer.enhance(factor)

    clean_img_name=os.path.splitext(filename)[0]

    edit.save(f".{pathOut}/{clean_img_name}_edited.jpg")