from bs4 import BeautifulSoup as BS

import requests
import json
import time
import logging

cookies = {
    'PHPSESSID': 'eueq05i6v3r5u50g4l8ritd86j',
    'BITRIX_SM_CLEARED_CURRENT_CITY_ID': 'Y',
    'BITRIX_SM_CURRENT_CITY_ID': '85',
    'BITRIX_SM_SALE_UID': '00df953a17eb33935432b35ab1ee6893',
    '_gid': 'GA1.2.581852796.1678623940',
    '__utma': '135143152.577129358.1678623940.1678623940.1678623940.1',
    '__utmc': '135143152',
    '__utmz': '135143152.1678623940.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '_ym_uid': '1678623940685676400',
    '_ym_d': '1678623940',
    '_ym_isad': '1',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A21%2C%22EXPIRE%22%3A1678654740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    '_ym_visorc': 'w',
    'tmr_lvid': 'befefedc1320dd6cb5796e3c60b60e1b',
    'tmr_lvidTS': '1678623945086',
    'adtech_uid': 'ab81c140-794a-40bb-9331-4c0e2cb3ac9d%3Apitergsm.ru',
    'top100_id': 't1.6394010.783547749.1678623945151',
    '_gat_%2Fcatalog%2Fphones%2Fiphone%2F': '1',
    '_gat_gtag_UA_106821143_2': '1',
    '_ga_SB0GW1QX9E': 'GS1.1.1678623939.1.1.1678624072.60.0.0',
    '_ga': 'GA1.2.577129358.1678623940',
    '_gat_UA-250083750-1': '1',
    '__utmb': '135143152.9.10.1678623940',
    'tmr_detect': '1%7C1678624075219',
    'last_visit': '1678613275246%3A%3A1678624075246',
    't3_sid_6394010': 's1.678590365.1678623945152.1678624078578.1.15',
}

headers = {
    'authority': 'pitergsm.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'PHPSESSID=eueq05i6v3r5u50g4l8ritd86j; BITRIX_SM_CLEARED_CURRENT_CITY_ID=Y; BITRIX_SM_CURRENT_CITY_ID=85; BITRIX_SM_SALE_UID=00df953a17eb33935432b35ab1ee6893; _gid=GA1.2.581852796.1678623940; __utma=135143152.577129358.1678623940.1678623940.1678623940.1; __utmc=135143152; __utmz=135143152.1678623940.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _ym_uid=1678623940685676400; _ym_d=1678623940; _ym_isad=1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A21%2C%22EXPIRE%22%3A1678654740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_visorc=w; tmr_lvid=befefedc1320dd6cb5796e3c60b60e1b; tmr_lvidTS=1678623945086; adtech_uid=ab81c140-794a-40bb-9331-4c0e2cb3ac9d%3Apitergsm.ru; top100_id=t1.6394010.783547749.1678623945151; _gat_%2Fcatalog%2Fphones%2Fiphone%2F=1; _gat_gtag_UA_106821143_2=1; _ga_SB0GW1QX9E=GS1.1.1678623939.1.1.1678624072.60.0.0; _ga=GA1.2.577129358.1678623940; _gat_UA-250083750-1=1; __utmb=135143152.9.10.1678623940; tmr_detect=1%7C1678624075219; last_visit=1678613275246%3A%3A1678624075246; t3_sid_6394010=s1.678590365.1678623945152.1678624078578.1.15',
    'referer': 'https://pitergsm.ru/catalog/phones/iphone/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

logger = logging.getLogger(__name__)
log_level = logging.INFO
logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

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
        logging.error(ex)
        
def iphones() -> list:
    try:
        with open('catalogs.json', encoding='utf-8') as file:
            catalogs = json.load(file)
        url = f'https://pitergsm.ru{catalogs[0]}'
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
        url = f'https://pitergsm.ru{catalogs[0]}'
        responce = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BS(responce.text, 'lxml')
        catalogs_href = soup.find_all('li', class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        return catalog_list
    except Exception as ex:
        logging.error(ex)

def ipad() -> list:
    try:
        with open('catalogs.json', encoding='utf-8') as file:
            catalogs = json.load(file)
        url = f'https://pitergsm.ru{catalogs[1]}'
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
        url = f'https://pitergsm.ru{catalogs[1]}'
        responce = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BS(responce.text, 'lxml')
        catalogs_href = soup.find_all('li', class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        return catalog_list
    except Exception as ex:
        logging.error(ex)

def mac() -> list:
    try:
        with open('catalogs.json', encoding='utf-8') as file:
            catalogs = json.load(file)
        url = f'https://pitergsm.ru{catalogs[2]}'
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
        url = f'https://pitergsm.ru{catalogs[2]}'
        responce = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BS(responce.text, 'lxml')
        catalogs_href = soup.find_all('li', class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        return catalog_list
    except Exception as ex:
        logging.error(ex)

def watch() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[3]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        try:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        except AttributeError:
            continue
    print(catalog_list)
    return catalog_list

def audio() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[4]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        try:
            catalog_href = catalog.find('a', class_='button-line__btn').get('href')
            catalog_list.append(catalog_href)
        except AttributeError:
            continue
    print(catalog_list)
    return catalog_list

def elektronika() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[6]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        catalog_href = catalog.find('a', class_='button-line__btn').get('href')
        catalog_list.append(catalog_href)
    print(catalog_list)
    return catalog_list

def pristavki_i_igry() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[7]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        catalog_href = catalog.find('a', class_='button-line__btn').get('href')
        catalog_list.append(catalog_href)
    print(catalog_list)
    return catalog_list

def tekhnika_dlya_doma() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[8]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        catalog_href = catalog.find('a', class_='button-line__btn').get('href')
        catalog_list.append(catalog_href)
    print(catalog_list)
    return catalog_list

def gadzhety() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[9]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        catalog_href = catalog.find('a', class_='button-line__btn').get('href')
        catalog_list.append(catalog_href)
    print(catalog_list)
    return catalog_list

def tv() -> list:
    
    with open('catalogs.json', encoding='utf-8') as file:
        catalogs = json.load(file)
    url = f'https://pitergsm.ru{catalogs[10]}'
    responce = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BS(responce.text, 'lxml')
    catalogs_href = soup.find_all('li', class_="button-line__item")
    catalog_list = []
    for catalog in catalogs_href:
        catalog_href = catalog.find('a', class_='button-line__btn').get('href')
        catalog_list.append(catalog_href)
    print(catalog_list)
    return catalog_list



