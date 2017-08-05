import scrapy
from urlparse import urlparse

def get_domain_name(url):

    url_tokens = urlparse(url)
    return url_tokens.netloc

def addHttpWithUrl(url):

    if url.startswith('http:'):
        return url
    if url.startswith('https:'):
        return url
    if url.startswith('www.'):
        return 'http://' + url
    if not url.startswith('http://'):
        return 'http://' + url
    return url
