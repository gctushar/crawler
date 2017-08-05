import scrapy

#Html Page item

class HtmlItem(scrapy.Item):

    url = scrapy.Field()
    html_content = scrapy.Field()
    crawled_time = scrapy.Field()
    depth = scrapy.Field()
    parent_url = scrapy.Field()
    anchor_text = scrapy.Field()