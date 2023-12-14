from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

PEP_DOMAIN = 'peps.python.org'
PEP_URL = f'https://{PEP_DOMAIN}/'
RES_DIR = 'results/'

ROBOTSTXT_OBEY = True

# Table constants:
TABLE_HEADER = ('Status', 'Quantity')
TABLE_FOOTER = 'Total'

# File constants:
ENCODING_UTF = 'utf-8'
FORMAT_CSV = 'csv'

# Date formats:
DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'

# regular expressions:
PEP_REGEX = r'(?P<number>\d+)'

FEEDS = {
    f'{RES_DIR}pep_%(time)s.csv': {
        'format': FORMAT_CSV,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300
}
