from bs4 import BeautifulSoup as BS
from parser.requests_info import cookies, headers

import requests
import json

def get_all_catalogs() -> json:
    try:
        url = 'https://pitergsm.ru/catalog/'
        response = requests.get(url=url, cookies=cookies, headers=headers)
        if response.status_code == 200:
            soup = BS(response.text, 'lxml')
            catalogs_href = soup.find_all('div', class_="catalog__item")
            catalog_list = []
            for catalog in catalogs_href:
                catalog_href = catalog.get('href')
                catalog_list.append(catalog_href)
            with open('catalogs.json', 'w', encoding='utf-8') as file:
                json.dump(catalog_list, file, indent=4, ensure_ascii=False)
        else:
            return 'HTTP 400 Bad Request!'
    except Exception as ex:
        print(f'Error: {ex}')

def get_catalog_list(range: int) -> list:
    try:
        with open('catalogs.json', encoding='utf-8') as file:
            catalogs = json.load(file)
        url = f'https://pitergsm.ru{catalogs[range]}'
        responce = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BS(responce.text, 'lxml')
        catalogs_href = soup.find_all('li', class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        return catalog_list
    except FileNotFoundError:
        get_all_catalogs()
        with open('catalogs.json', encoding='utf-8') as file:
            catalogs = json.load(file)
        url = f'https://pitergsm.ru{catalogs[range]}'
        responce = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BS(responce.text, 'lxml')
        catalogs_href = soup.find_all('li', class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        return catalog_list
    except Exception as ex:
        print(f'Error: {ex}')

def iphones() -> list:
    return get_catalog_list(range = 0)

def ipad() -> list:
    return get_catalog_list(range = 1)

def mac() -> list:
    return get_catalog_list(range = 2)



