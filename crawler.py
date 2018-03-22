# http://icrawler.readthedocs.io/en/latest/index.html
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import os
import const


# 크롤링 담을 폴더 생성
for service in const.CRAWLER_TARGET_SERVICE:
    path = os.path.join(const.FULL_PATH, 'data', service)
    if not os.path.isdir(path):
        os.mkdir(path)


# 크롤링
for service in const.CRAWLER_TARGET_SERVICE:
    for word in const.TARGET_WORD:
        path = os.path.join(const.FULL_PATH, 'data', service)
        crawler = None

        if service == 'google':
            crawler = GoogleImageCrawler(storage={'root_dir': path})
        elif service == 'bing':
            crawler = BaiduImageCrawler(storage={'root_dir': path})
        elif service == 'bing':
            crawler = BingImageCrawler(storage={'root_dir': path})

        crawler.crawl(keyword=word, filters=const.CRAWLER_TARGET_SERVICE_FILTER[service], offset=0, max_num=1000)