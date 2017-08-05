import scrapy
import logging
from datetime import date
from scrapy.linkextractors import LinkExtractor
import crawler.items.html_item as item
import crawler.utils.common as common
from datetime import datetime
from scrapy import log


class MyCrawler(scrapy.Spider):

    name = "my_crawler"

    def start_requests(self):

        urls = self.get_seed_urls()

#Sending request for seed urls
        for url in urls:
            try:
                request = scrapy.Request(url=url, callback=self.crawl_page)
                request.meta['depth'] = 1
                request.meta['parent_url'] = None
                request.meta['anchor_text'] = None
                request.meta['seed_url'] = url

                yield request

            except Exception as ex:
                log.msg("Exception on start request %s" %(ex), level=log.ERROR)


#Load seed url from file
    def get_seed_urls(self):

        try:
            seed_file = open(self.settings['SEED_URL_FILE_NAME'], 'rb')
            urls = []

            for line in seed_file.readlines():
                urls.append(common.addHttpWithUrl(line.strip()))

            return urls
        except Exception as ex:
            log.msg("Exception on Seed File loading %s" % (ex), level=log.ERROR)

#This function is used to fetch item and store them
    def crawl_page(self, response):

        html_page_item = item.HtmlItem()

        html_page_item['html_content'] = response.body
        html_page_item['url'] = response.url
        html_page_item['crawled_time'] = datetime.now()
        html_page_item['parent_url'] = response.meta['parent_url']
        html_page_item['anchor_text'] = response.meta['anchor_text']
        html_page_item['depth'] = response.meta['depth']

        yield html_page_item
#Extract link from the page and send request for the next depth
        links = LinkExtractor(unique=True, allow_domains=common.get_domain_name(response.meta["seed_url"])).extract_links(response)

        for link in links:

            try:
                new_request = scrapy.Request(url=link.url, callback=self.crawl_page)
                new_request.meta['depth'] = response.meta['depth'] + 1
                new_request.meta['anchor_text'] = link.text
                new_request.meta['parent_url'] = response.url
                new_request.meta['seed_url'] = response.meta['seed_url']

                yield new_request

            except Exception as ex:
                log.msg("Exception on New Request %s" % (ex), level=log.ERROR)

