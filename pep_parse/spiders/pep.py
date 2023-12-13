import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_REGEX


class PepSpider(scrapy.Spider):
    """Паук, собирающий информацию о статусах РЕР"""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсинг РЕР 0"""
        yield from response.follow_all(
            css='a.pep.reference.internal::attr("href")',
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        """Парсинг статусов РЕР"""
        name = response.css('h1.page-title::text').get()
        number = re.search(PEP_REGEX, name).group('number')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
