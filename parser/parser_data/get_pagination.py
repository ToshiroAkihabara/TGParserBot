from bs4 import BeautifulSoup as BS
from parser.config import headers
from requests.exceptions import RequestException
from dataclasses import dataclass
from typing import TypeAlias

import requests
import time

CatalogName: TypeAlias = str


@dataclass(slots=True, frozen=True)
class Pagination:
    catalog_name = str
    last_page = int


def get_pagination(catalog: CatalogName) -> Pagination:
    try:
        count = 1
        while True:
            url = f"https://pitergsm.ru{catalog}?PAGEN_1={count}"
            time.sleep(2)
            try:
                response = requests.get(url=url, headers=headers)
            except RequestException:
                raise RequestException(f"Bad url: {url}.")
            parse = BS(response.text, "lxml")
            pagination_next = parse.find("div", class_="page-paging").find(
                "a", class_="paging__next"
            )
            if pagination_next:
                count += 1
            else:
                last_page = count
                catalog_name = catalog
                yield catalog_name, last_page
                break
    except AttributeError:
        last_page = count
        catalog_name = catalog
        yield catalog_name, last_page
