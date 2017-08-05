import os
# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

###################################
#
#  This File Contains the all settings of the crawler
#
###################################

BOT_NAME = 'crawler'


SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'


# General Config

CRAWLER_BASE_DIRECTORY = "/home/tushar/python_project/scrapy/crawler/crawler"

SEED_URL_FILE_NAME = CRAWLER_BASE_DIRECTORY + '/seeds.txt'

# Resume/Pause Request
JOBDIR = CRAWLER_BASE_DIRECTORY + "/JOB_DIR"

#defalut local time zone
DEFAULT_TIME_ZONE = 'America/New_York'

# Logger file configuration
# if dont need to log on file just off the line
# LOG_FILE = CRAWLER_BASE_DIRECTORY + '/logs.log'

# Depth Control scrapy internal configuration attribute
# Maximum depth to crawl

DEPTH_LIMIT = 3

# REDIS Config
# used for url seen middleware and stat collection

REDIS_HOST = "localhost"
REDIS_PORT = 6379

# URL Seen Middleware Config
# from which depth the middleware will be activated

URL_SEEN_MAX_ALLOWED_DEPTH = 2

#MONGO DB CONFIG
#data will be saved on mongodb
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_NAME = 'data'
COLLECTION_NAME = 'documents'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
}

# Enable or disable downloader middlewares
# This will be used for url seen
# already crawled urls will not be crawled again
DOWNLOADER_MIDDLEWARES = {
   'crawler.middlewares.url_seen_middleware.URLSeenMiddleWare': 544,
}

#Custom extension for crawling stat collection

EXTENSIONS = {
   'crawler.extensions.crawler_stat_collection_extension.CrawlerStatCollection': 544
}

# Enable or disable extensions
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
ITEM_PIPELINES = {
   'crawler.pipelines.mongoPipeline.MongoPipeline': 300
   # 'crawler.pipelines.pipelines.CrawlerPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
