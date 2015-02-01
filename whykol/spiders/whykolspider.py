from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from whykol.items import WhykolItem
from scrapy.http import Request
import urlparse

class WhyKol(CrawlSpider):

    name = 'whykol'
    allowed_domains = ['whykol.com']
    filename=""
    start_urls = ['http://www.whykol.com/category/malayalam-movies-comedy-dialogues/']
    rules = (Rule(LinkExtractor(allow=[],restrict_xpaths = ("//h2[@class='post-title']") ), 'parse_page'),Rule(LinkExtractor(allow=[],restrict_xpaths = ("//a[@class='nextpostslink']")),'next_page', follow=True))

    def parse_page(self, response):
          whykol=WhykolItem()
          whykol['image_urls']=response.xpath("//img[@class='attachment-large wp-post-image']/@src").extract()
          yield whykol

    


    
            