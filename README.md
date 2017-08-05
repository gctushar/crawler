# README #

This an open source web crawler using scrapy, which provides a simple interface for crawling the Web. Using it, you can setup a multi-threaded web crawler in few minutes.

### What is this repository for? ###
* This repository is mainly for crawling the websites for multy depth and storing the HTML pages on mongodb.

### Quick Setup ###
* Download and install scrapy
* Setup mongodb on your environment
* Also need to setup redis server
* install mongodb and redis driver for python
* clone the project

### Configuration? ###
* Open the crawler/settings.py file and customize the cofiguration
* You have to put seed urls on seed.txt file separated with newline

### How to run  ###
* open terminal and navigate to the project folder
* On linux run command on terminal scrapy crawl my_crawler
  
