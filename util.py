import os
import const


def makedir(*dirs):
    path = os.path.join(const.FULL_PATH, *dirs)
    if not os.path.isdir(path):
        os.mkdir(path)


def get_image_crop_info(width, height):
    if width >= height:
        base = height
        top = 0
        left = (width - base) / 2
        return base, top, left
    else:
        base = width
        top = (height - base) / 2
        left = 0
        return base, top, left
