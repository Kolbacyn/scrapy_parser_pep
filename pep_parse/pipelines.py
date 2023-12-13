import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, DATE_FORMAT, TABLE_FOOTER,
                                TABLE_HEADER)


class PepParsePipeline:
    """Обработчик информации от паука PepSpider"""
    def open_spider(self, spider):
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.pep_statuses[status] += 1
        return item

    def close_spider(self, spider):
        current_time = dt.datetime.now().strftime(DATE_FORMAT)
        filename = f'results/status_summary_{current_time}.csv'
        filepath = BASE_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect
            ).writerows([
                TABLE_HEADER,
                *self.pep_statuses.items(),
                (TABLE_FOOTER, sum(self.pep_statuses.values()))
            ])
