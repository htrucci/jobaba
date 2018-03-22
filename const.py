import os

CRAWLER_TARGET_SERVICE = ['google', 'bing', 'baidu']

CRAWLER_TARGET_SERVICE_FILTER = {
    'google': {'type': 'photo'},
    'baidu': {'type': 'static'}
}

OUTPUT_SIZE = (32, 32)


# FULL_PATH = "C:/Users/201210108/Desktop/working/jobaba/"
FULL_PATH = os.path.abspath('')

TARGET_WORD = ['strawberry', 'cherry', 'raspberry']

