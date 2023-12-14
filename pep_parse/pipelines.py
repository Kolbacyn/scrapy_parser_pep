import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from scrapy import Item, Spider

from pep_parse.items import PepParseItem
from pep_parse.settings import (BASE_DIR, DATE_FORMAT, ENCODING_UTF,
                                FORMAT_CSV, RES_DIR,
                                TABLE_FOOTER, TABLE_HEADER)


class PepParsePipeline:
    """Обработчик информации от паука PepSpider"""
    def open_spider(self, spider: Spider) -> None:
        self.pep_statuses: defaultdict = defaultdict(int)

    def process_item(self, item: Item, spider: Spider) -> PepParseItem:
        status: str = item['status']
        self.pep_statuses[status] += 1
        return item

    def close_spider(self, spider: Spider) -> None:
        current_time: str = dt.datetime.now().strftime(DATE_FORMAT)
        filename: str = f'{RES_DIR}status_summary_{current_time}.{FORMAT_CSV}'
        filepath: Path = BASE_DIR / filename
        with open(filepath, 'w', encoding=ENCODING_UTF) as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect
            ).writerows([
                TABLE_HEADER,
                *self.pep_statuses.items(),
                (TABLE_FOOTER, sum(self.pep_statuses.values()))
            ])
