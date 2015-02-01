# -*- coding: utf-8 -*-

# Scrapy settings for whykol project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'whykol'

SPIDER_MODULES = ['whykol.spiders']
NEWSPIDER_MODULE = 'whykol.spiders'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/nirmal/whykol'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'whykol (+http://www.yourdomain.com)'