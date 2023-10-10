from PIL import Image,ImageEnhance,ImageFilter
import os

path = "./imgs"
pathout = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    enhancer = ImageEnhance.Contrast(img)
    factor = 1.5
    edit = enhancer.enhance(factor)
    edit = img.convert("L")
    edit = Image.new("RGB", img.size, "blue")
    edit.paste(img, (0,0), img)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit = edit.convert("RGB")
    
    edit.save(f"./{pathout}/{clean_name}_edited.jpg")