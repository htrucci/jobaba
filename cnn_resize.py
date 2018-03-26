from PIL import Image
import os,sys
import glob

image_dir = "./한라봉/"
target_dir = "./한라봉/resize/"
files = glob.glob(image_dir+"*.*")
print(len(files))
count = 1;
size = (224, 224)
for file in files:
    im = Image.open(file)
    im = im.convert('RGB')
    print("i: ", count, im.format, im.size, im.mode, file.split("/")[-1])
    count+=1
    #imageNew = Image.new("RGB", (224, 224))
    #imageNew = im.resize((224, 224), resample=3)
    im.thumbnail(size, Image.ANTIALIAS)
    #imageNew.paste(image.resize((32, 32), 3))
    im.save(target_dir+file.split("/")[-1], quality=100)
#im = Image.open("./한라봉/000001.jpg")
#im.show()

