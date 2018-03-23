import os

CRAWLER_TARGET_SERVICE = ['google', 'bing', 'baidu']

CRAWLER_TARGET_SERVICE_FILTER = {
    'google': {'type': 'photo'},
    'bing': {'type': 'photo'},
    'baidu': {'type': 'static'}
}

OUTPUT_SIZE = (32, 32)

RESIZE_BASE = 4/3

FULL_PATH = os.path.abspath('')

TARGET_WORD = ['strawberry', 'cherry', 'raspberry']

