# http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC
from PIL import Image
import os
import const


# 이미지 리사이징 폴더 생성
for service in const.CRAWLER_TARGET_SERVICE:
    path = os.path.join(const.FULL_PATH, 'redata', service)
    if not os.path.isdir(path):
        os.mkdir(path)


# 이미지 리사이징
for service in const.CRAWLER_TARGET_SERVICE:
    path = os.path.join(const.FULL_PATH, 'data', service)

    for filename in os.listdir(path):
        full_filename = os.path.join(const.FULL_PATH, 'data', filename)
        im = Image.open(full_filename)
        width, height = im.size
        outfile = os.path.join(const.FULL_PATH, 'redata', filename)
        print(filename, width, height, width / height <= 4/3) # 이미지 크기 출력

        # 4:3 이하 비율이면 리사이징
        if width / height <= 4/3:
            im.thumbnail(const.OUTPUT_SIZE)
            im.save(outfile)
        # 비정상 비율이면 crop 후 리사이징
        # else:
            # cropImage = im.crop((100, 100, 150, 150)) # TODO, 위치잡기
            # cropImage.thumbnail(size)
            # cropImage.save(thumpDir + '/' + filename)