import re

import scrapy
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN, PEP_REGEX, PEP_URL


class PepSpider(scrapy.Spider):
    """Паук, собирающий информацию о статусах РЕР"""
    name: str = 'pep'
    allowed_domains: list[str] = [PEP_DOMAIN]
    start_urls: list[str] = [PEP_URL]

    def parse(self, response: HtmlResponse) -> Request:
        """Парсинг РЕР 0"""
        yield from response.follow_all(
            css='a.pep.reference.internal::attr("href")',
            callback=self.parse_pep
        )

    def parse_pep(self, response: HtmlResponse) -> PepParseItem:
        """Парсинг статусов РЕР"""
        name: str = response.css('h1.page-title::text').get()
        number: str = re.search(PEP_REGEX, name).group('number')
        status: str = response.css(
            'dt:contains("Status") + dd abbr::text'
        ).get()

        data: dict[str, str] = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
