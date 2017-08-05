from datetime import datetime
from scrapy import signals
from crawler.utils import common
import redis
from pytz import timezone

#################################################
#
# this is the extension for stat collection of the spider
# this store the stat on redis database
# so any kind of stat can be provided online or ofline
#
#################################################
class CrawlerStatCollection(object):

    def __init__(self,redis_host, redis_port):

        self.redisClient = redis.StrictRedis(redis_host, redis_port)

    @classmethod
    def from_crawler(cls, crawler):

        redis_host = crawler.settings.get('REDIS_HOST')
        redis_port = crawler.settings.get('REDIS_PORT')
        extension = cls(redis_host, redis_port)

        crawler.signals.connect(extension.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(extension.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(extension.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(extension.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(extension.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(extension.request_dropped, signal=signals.request_dropped)
        crawler.signals.connect(extension.response_received, signal=signals.response_received)
        crawler.signals.connect(extension.response_downloaded, signal=signals.response_downloaded)

        return extension

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        pass

    def item_scraped(self, item, response, spider):

        if 'seed_url' in response.meta:
            domain = common.get_domain_name(response.meta['seed_url'])
        else:
            domain = common.get_domain_name(response.url)

        domain_key = domain + ':stats:item_scraped'

        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:item_scraped", amount=1)

        self.redisClient.sadd("domains", domain)

    def item_dropped(self,item, response, exception, spider):

        if 'seed_url' in response.meta:
            domain = common.get_domain_name(response.meta['seed_url'])
        else:
            domain = common.get_domain_name(response.url)

        domain_key =  domain + ':stats:item_dropped'

        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:item_dropped", amount=1)

    def request_scheduled(self,request, spider):

        if 'seed_url' in request.meta:
            domain = common.get_domain_name(request.meta['seed_url'])
        else:
            domain = common.get_domain_name(request.url)

        domain_key =  domain +':stats:request_scheduled'

        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:request_scheduled", amount=1)

    def request_dropped(self, request, spider):

        if 'seed_url' in request.meta:
            domain = common.get_domain_name(request.meta['seed_url'])
        else:
            domain = common.get_domain_name(request.url)

        domain_key =  domain +':stats:request_dropped'

        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:request_dropped", amount=1)

    def response_received(self,response, request, spider):

        if 'seed_url' in response.meta:
            domain = common.get_domain_name(response.meta['seed_url'])
        else:
            domain = common.get_domain_name(response.url)

        domain_key = domain + ':stats:response_received'

        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:response_received", amount=1)

    def response_downloaded(self, response, request, spider):

        if 'seed_url' in request.meta:
            domain = common.get_domain_name(request.meta['seed_url'])
        else:
            domain = common.get_domain_name(request.url)

        domain_key = domain + ':stats:response_downloaded'
        self.redisClient.incr(domain_key, amount=1)

        self.redisClient.incr("all:stats:response_downloaded", amount=1)

        local_time = timezone(spider.settings.get('DEFAULT_TIME_ZONE'))
        loc_dt = datetime.now(local_time)

        domain_key = domain + ':stats:last_downloaded_at'
        self.redisClient.set(domain_key, loc_dt)

        self.redisClient.set("all:stats:last_downloaded_at", loc_dt)
