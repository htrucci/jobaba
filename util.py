import os
import const


def makedir(*dirs):
    path = os.path.join(const.FULL_PATH, *dirs)
    if not os.path.isdir(path):
        os.mkdir(path)


def get_image_crop_info(width, height):
    cent_x = width / 2
    cent_y = height / 2
    base = (width if width <= height else height) / 2
    top = cent_y - base
    left = cent_x - base
    return base, top, left
