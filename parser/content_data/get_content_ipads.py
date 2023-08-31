from parser.pages_data import get_pages_ipads
from bs4 import BeautifulSoup as BS
from parser.requests_info import cookies, headers

import requests
import json

def get_content_ipads(func) -> json:
    def wrapper():
        all_data = []
        for url in func():
            name = url.split('/')[7].replace('-', '_')
            if name == 'ipad':
                name = 'ipad_'
            response = requests.get(url=url, cookies=cookies, headers=headers)
            scr = response.text
            soup = BS(scr, 'lxml')
            data = soup.find_all('div', class_="catalog__list like-cards")
            for item in data:
                cards = item.find_all('div', class_="catalog__item")
                for card in cards:
                    try:
                        all_data.append(
                            {
                            'title': card.find('div', class_="prod-card__title").text,
                            'available': card.find('div', class_="prod-card__count icon-check-green nodesktop").text,
                            'price': card.find('div', class_="price__now").text.replace('a', ' ').strip(),
                            'url': 'https://pitergsm.ru' + card.find('div', class_="prod-card").find('a', class_="prod-card__link").get('href')
                            }
                        )
                    except AttributeError: 
                        continue
        with open(f'{name}.json', 'w', encoding='utf-8') as file:
            json.dump(all_data, file, indent=4, ensure_ascii=False)
    return wrapper

@get_content_ipads
def ipad_pro() -> list:
    return get_pages_ipads.page_ipad_pro()

@get_content_ipads
def ipad_air() -> list:
    return get_pages_ipads.page_ipad_air()

@get_content_ipads
def ipad_mini() -> list:
    return get_pages_ipads.page_ipad_mini()

@get_content_ipads
def ipad() -> list:
    return get_pages_ipads.page_ipad()