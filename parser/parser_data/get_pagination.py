from bs4 import BeautifulSoup as BS
from parser.requests_info import cookies, headers

import requests
import time

def pagination(catalog: str) -> str | int: 
    try:
        count = 1
        while True:
            url = f'https://pitergsm.ru{catalog}?PAGEN_1={count}'
            time.sleep(2)
            responce = requests.get(url=url, cookies=cookies, headers=headers)
            soup = BS(responce.text, 'lxml')
            pagination_next = soup.find('div', class_="page-paging").find('a', class_="paging__next")
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
        


