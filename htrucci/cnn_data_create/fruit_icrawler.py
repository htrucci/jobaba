from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=10,
    parser_threads=10,
    downloader_threads=10,
    storage={'root_dir': 'your_image_dir'})
filters = dict(
    type='photo')
google_crawler.crawl(keyword='한라봉', filters=filters, max_num=700, file_idx_offset=0)
#filters = dict(
#               type='photo')
#google_crawler.crawl(keyword='레몬', filters=filters, max_num=700, file_idx_offset=0)
#filters = dict(
#               type='photo')
#google_crawler.crawl(keyword='레몬', filters=filters, max_num=700, file_idx_offset=0)

