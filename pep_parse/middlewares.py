from typing import Generator as Gen

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.http import Request, Response
from scrapy.spiders import Spider
from typing_extensions import Self


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        s = cls()
        crawler.signals.connect(
            s.spider_opened,
            signal=signals.spider_opened
        )
        return s

    def process_spider_input(self,
                             response: Response,
                             spider: Spider) -> None:
        return None

    def process_spider_output(self,
                              response: Response,
                              result: Request,
                              spider: Spider) -> Gen[Request, None, None]:
        for i in result:
            yield i

    def process_spider_exception(self,
                                 response: Response,
                                 exception: Exception,
                                 spider: Spider) -> None:
        pass

    def process_start_requests(self,
                               start_requests: Request,
                               spider: Spider) -> Gen[Request, None, None]:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        s = cls()
        crawler.signals.connect(
            s.spider_opened,
            signal=signals.spider_opened
        )
        return s

    def process_request(self,
                        request: Request,
                        spider: Spider) -> None:
        return None

    def process_response(self,
                         request: Request,
                         response: Response,
                         spider: Spider) -> Response:
        return response

    def process_exception(self,
                          request: Request,
                          exception: Exception,
                          spider: Spider) -> None:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
