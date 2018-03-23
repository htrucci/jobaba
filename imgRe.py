# http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC
from PIL import Image
import os
import const
import util


# 이미지 리사이징 폴더 생성
for service in const.CRAWLER_TARGET_SERVICE:
    util.makedir('redata', service)


# 이미지 리사이징
for service in const.CRAWLER_TARGET_SERVICE:
    path = os.path.join(const.FULL_PATH, 'data', service)

    for filename in os.listdir(path):
        full_filename = os.path.join(const.FULL_PATH, 'data', filename)
        im = Image.open(full_filename)
        width, height = im.size
        outfilepath = os.path.join(const.FULL_PATH, 'redata', filename)

        print(filename, width, height, width / height <= 4/3) # 이미지 크기 출력

        # 4:3 이하 비율이면 리사이징
        if width / height <= 4/3:
            im.thumbnail(const.OUTPUT_SIZE)
            im.save(outfilepath)
        # 비정상 비율이면 crop 후 리사이징
        else:
            base, top, left = util.get_image_crop_info(width, height)
            cropImage = im.crop((top, left, base, base))
            cropImage.thumbnail(const.OUTPUT_SIZE) # TODO, test 필요
            cropImage.save(outfilepath)