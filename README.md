[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Scrapy](https://img.shields.io/badge/scrapy-%14fa1c.svg?style=for-the-badge&logo=scrapy&logoColor=white)](https://scrapy.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=SQLAlchemy)](https://www.sqlalchemy.org/)
## Асинхронный парсер официальной документации с сайта python.org
![Workflow](https://github.com/Kolbacyn/scrapy_parser_pep/actions/workflows/scrapy_workflow.yml/badge.svg?event=push)

## Технологии:

- Python 3.9
- Scrapy

## Описание

Парсер позволяет получить актуальную информацию о версиях Python, авторах версий, о нововведениях в каждой из версий и получить информацию о PEP (Python Enhancement Proposal). Информацию также можно скачать в различных форматах.

## Установка

Для начала работы необходимо клонировать репозиторий:

```bash
git clone git@github.com:Kolbacyn/scrapy_parser_pep.git
```

Установить и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Запуск

В рабочей директории используйте команду

```bash
scrapy crawl pep
```

Результаты работы парсера будут храниться в папке results.

- pep_.csv хранит информацию о каждом РЕР (название, номер и статус);
- status_summary_.csv хранит сводную информацию о статусах PEP

## Разработчик

[Зольников Юрий](https://github.com/Kolbacyn/)
