from PIL import Image, ImageOps
import os,sys
import glob

fruits = ["귤", "한라봉", "레몬"]
for fruit_name in fruits:
    image_dir = "../"+fruit_name+"/"
    target_resize_dir = "../"+fruit_name+"/resize/"
    target_rotate_dir = "../"+fruit_name+"/rotate/"
    if not os.path.isdir(target_resize_dir):
        os.mkdir(target_resize_dir)
    if not os.path.isdir(target_rotate_dir):
        os.mkdir(target_rotate_dir)        
    files = glob.glob(image_dir+"*.*")
    print(len(files))
    count = 1;
    size = (224, 224)
    for file in files:
        im = Image.open(file)
        im = im.convert('RGB')
        print("i: ", count, im.format, im.size, im.mode, file.split("/")[-1])
        #width, height = im.size
        count+=1
        #left = width/2 - 112
        #top = height/2 - 112
        #right = width/2 + 112
        #bottom = height/2 + 112
        #im.crop((left, top, right, bottom))
        im = ImageOps.fit(im, size, Image.ANTIALIAS, 0, (0.5, 0.5))
        im.save(target_resize_dir+file.split("/")[-1], quality=100)
        im.rotate(90).save(target_rotate_dir+file.split("/")[-1], quality=100)

        #imageNew = Image.new("RGB", (224, 224))
        #imageNew = im.resize((224, 224), resample=3)
        #im.thumbnail(size, Image.ANTIALIAS)
        #imageNew.paste(image.resize((32, 32), 3))
        
    #im = Image.open("./한라봉/000001.jpg")
    #im.show()

