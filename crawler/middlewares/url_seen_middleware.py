# coding: utf-8
from scrapy import exceptions
import redis
import crawler.utils.common as common
import hashlib
############################
#
# #This middleware is used for url seen
#if an url already crawled it will skip this url
#we can control the middleware from which depth it will be active
#
# ###########################

class URLSeenMiddleWare(object):

    def __init__(self, redis_host, redis_port, max_depth):

        self.redis_host = redis_host
        self.redis_port = redis_port
        self.max_depth = max_depth

        self.client = redis.StrictRedis(self.redis_host, self.redis_port)

    @classmethod
    def from_crawler(cls, crawler):

        return cls(
            redis_host = crawler.settings.get('REDIS_HOST'),
            redis_port = crawler.settings.get('REDIS_PORT'),
            max_depth =  crawler.settings.get('URL_SEEN_MAX_ALLOWED_DEPTH')
        )

    def process_request(self, request, spider):

        if 'seed_url' in request.meta:
            domain = common.get_domain_name(request.meta['seed_url'])
        else:
            domain = common.get_domain_name(request.url)

        domain_key = domain + ':urls'

        m = hashlib.md5()
        m.update(request.url.encode('utf-8'))
        url_digest = m.hexdigest()

        if 'depth' in request.meta and request.meta['depth'] > self.max_depth:

            if self.client.hexists(domain_key, url_digest):
                raise exceptions.IgnoreRequest
            else:
                self.client.hset(domain_key, url_digest, True)

        else:
            self.client.hset(domain_key, url_digest, True)
