# http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC
from PIL import Image
import os
import const
import util


# 이미지 리사이징 폴더 생성
for word in const.TARGET_WORD:
    util.makedir('redata', word)


# 이미지 리사이징
for service in const.CRAWLER_TARGET_SERVICE:
    for word in const.TARGET_WORD:
        path = os.path.join(const.FULL_PATH, 'data', service, word)

        for filename in os.listdir(path):
            re_filename = service + '_' + filename
            full_file_path = os.path.join(const.FULL_PATH, 'data', service, word, filename)
            im = Image.open(full_file_path)
            width, height = im.size
            out_file_path = os.path.join(const.FULL_PATH, 'redata', word, re_filename)

            try:
                # 4:3 이하 비율이면 리사이징
                # 가로 비율이 큰 경우와 세로 비율이 큰 경우 나누어 계산
                if (width >= height and width / height <= const.RESIZE_BASE) \
                        or (width < height and height / width <= const.RESIZE_BASE):
                    rim = im.resize(size=const.OUTPUT_SIZE, resample=Image.ANTIALIAS)
                    rim.save(out_file_path)
                    print(filename, "none", width, height)

                # 비정상 비율이면 가운데 기준 crop 후 리사이징
                else:
                    base, top, left = util.get_image_crop_info(width, height)
                    cropImage = im.crop((left, top, left + base, top + base))
                    # cropImage.save(out_file_path)  # debug
                    rim = cropImage.resize(size=const.OUTPUT_SIZE, resample=Image.ANTIALIAS)
                    rim.save(out_file_path)
                    print(filename, "crop", width, height)

            except IOError as e:
                print("IOError! ", e)
            except SystemError as e:
                print("SystemError! ", e)
            except UserWarning as e:
                print("UserWarning! ", e)
