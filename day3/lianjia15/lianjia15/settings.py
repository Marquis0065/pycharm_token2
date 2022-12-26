# Scrapy settings for lianjia15 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia15'

SPIDER_MODULES = ['lianjia15.spiders']
NEWSPIDER_MODULE = 'lianjia15.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia15 (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
LOG_FILE = 'logdemo.log'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     #'Accept-Encoding':' gzip, deflate, br',
#     'Accept-Language':' zh-CN,zh;q=0.9',
#     'Cache-Control':' max-age=0',
#     'Connection':' keep-alive',
#     #'Cookie':' lianjia_uuid=2a135598-9a63-48b1-a81d-6baaa29f02dd; _smt_uid=63905e45.62fefabb; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22184ebf03e111077-01219892b856dd-26021151-921600-184ebf03e125ed%22%2C%22%24device_id%22%3A%22184ebf03e111077-01219892b856dd-26021151-921600-184ebf03e125ed%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.220963272.1670405703; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1670813807; lianjia_ssid=ae205c4f-b676-4016-b5a4-a1bff13f4a5f; select_city=440300; _jzqa=1.1724933739435236400.1670405701.1670942332.1671066871.11; _jzqc=1; _jzqckmp=1; _qzja=1.1772569271.1670405701126.1670942332353.1671066870969.1670942332353.1671066870969.0.0.0.18.11; _qzjc=1; _qzjto=1.1.0; _jzqb=1.1.10.1671066871.1; _qzjb=1.1671066870969.1.0.0.0; _gid=GA1.2.1815679230.1671066873; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiM2JmNzA3ZDk1OGIxNTU5ZWM0YzUzMzQyMjNhNzQwMzNlYmQ2ZDhmZTYzY2Y0M2YyYjNiOGIwNGQ2ZTkwZmY3MmMxYzljZjBmOWY1ZTMwMjY0ZDZkNWNmZmU1MzFmZGJlYjcxOTVlOWZlMGFiMGM5ZDc0ZTdkMmI4MjEyY2UxMjUzODlhMmE2OGUwYjkwZmJkMWY4MmNiZjViYTcyMmFhMmUzNjY1MDNlNzg5ZTU2NzUyYjZmMGIyOWFiNmI5Y2VkN2ExZjcwNDc0NjgyMGFkMDUwYTViZjZkYmY5M2QzZTA1ZjQ1MzhiMTA3OWYyYmQ4MDQyYjhlYTY0MGRiOGNkN1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0NmZiYTUwZFwifSIsInIiOiJodHRwczovL3N6LmxpYW5qaWEuY29tL3p1ZmFuZy9mdXRpYW5xdS9wZzFydDIwMDYwMDAwMDAwMWwxLyNjb250ZW50TGlzdCIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
#     'Host':' sz.lianjia.com',
#     #'Referer': 'https://sz.lianjia.com/zufang/futianqu/rt200600000001l1/',
#     'sec-ch-ua':' "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile':' ?0',
#     'sec-ch-ua-platform':' "Windows"',
#     'Sec-Fetch-Dest':' document',
#     'Sec-Fetch-Mode':' navigate',
#     'Sec-Fetch-Site':' same-origin',
#     'Sec-Fetch-User':' ?1',
#     'Upgrade-Insecure-Requests':' 1',
#     'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
# }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia15.middlewares.Lianjia15SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lianjia15.middlewares.Lianjia15DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'lianjia15.pipelines.Lianjia15Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
