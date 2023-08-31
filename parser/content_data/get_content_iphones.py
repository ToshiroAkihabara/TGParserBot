from parser.pages_data import get_pages_iphones
from bs4 import BeautifulSoup as BS
from parser.requests_info import cookies, headers

import requests
import json

def get_content_iphone(func) -> json:
    def wrapper():
        content = []
        for url in func():
            name = url.split('/')[6].replace('-', '_')
            response = requests.get(url=url, cookies=cookies, headers=headers)
            scr = response.text
            soup = BS(scr, 'lxml')
            data = soup.find_all('div', class_="catalog__list like-cards")
            for item in data:
                cards = item.find_all('div', class_="catalog__item")
                for card in cards:
                    content.append(
                        {
                        'title': card.find('div', class_="prod-card__title").text,
                        'available': card.find('div', class_="prod-card__count icon-check-green nodesktop").text,
                        'price': card.find('div', class_="price__now").text.replace('a', ' ').strip(),
                        'url': 'https://pitergsm.ru' + card.find('div', class_="prod-card").find('a', class_="prod-card__link").get('href')
                        }
                    )
        with open(f'{name}.json', 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4, ensure_ascii=False)
    return wrapper
        # if len(list(func())) == 1:
        #     content = []
        #     for url in func():
        #         name = url.split('/')[6].replace('-', '_')
        #         response = requests.get(url=url, cookies=cookies, headers=headers)
        #         scr = response.text
        #         soup = BS(scr, 'lxml')
        #         data = soup.find_all('div', class_="catalog__list like-cards")
        #         # content = []
        #         for item in data:
        #             cards = item.find_all('div', class_="catalog__item")
        #             for card in cards:
        #                 content.append(
        #                     {
        #                     'title': card.find('div', class_="prod-card__title").text,
        #                     'available': card.find('div', class_="prod-card__count icon-check-green nodesktop").text,
        #                     'price': card.find('div', class_="price__now").text.replace('a', ' ').strip(),
        #                     'url': 'https://pitergsm.ru' + card.find('div', class_="prod-card").find('a', class_="prod-card__link").get('href')
        #                     }
        #                 )
        #     with open(f'{name}.json', 'w', encoding='utf-8') as file:
        #         json.dump(content, file, indent=4, ensure_ascii=False)

        # else:
        #     content = []
        #     for url in func():
        #         name = url.split('/')[6].replace('-', '_')
        #         response = requests.get(url=url, cookies=cookies, headers=headers)
        #         scr = response.text
        #         soup = BS(scr, 'lxml')
        #         data = soup.find_all('div', class_="catalog__list like-cards")
        #         # all_data = []
        #         for item in data:
        #             cards = item.find_all('div', class_="catalog__item")
        #             for card in cards:
        #                 content.append(
        #                     {
        #                     'title': card.find('div', class_="prod-card__title").text,
        #                     'available': card.find('div', class_="prod-card__count icon-check-green nodesktop").text,
        #                     'price': card.find('div', class_="price__now").text.replace('a', ' ').strip(),
        #                     'url': 'https://pitergsm.ru' + card.find('div', class_="prod-card").find('a', class_="prod-card__link").get('href')
        #                     }
        #                 )
        #         # content.append(all_data)    
            
        #     with open(f'{name}.json', 'w', encoding='utf-8') as file:
        #         json.dump(content, file, indent=4, ensure_ascii=False)
        
    # return wrapper
    
@get_content_iphone
def iphone_14_pro_max() -> list:
    return get_pages_iphones.page_iphone_14_pro_max()

@get_content_iphone
def iphone_14_pro_max() -> list:
    return get_pages_iphones.page_iphone_14_pro_max()
    
@get_content_iphone
def iphone_14_pro() -> list:
    return get_pages_iphones.page_iphone_14_pro()

@get_content_iphone
def iphone_14_plus() -> list:
    return get_pages_iphones.page_iphone_14_plus()

@get_content_iphone
def iphone_14() -> list:
    return get_pages_iphones.page_iphone_14()

@get_content_iphone
def iphone_13_pro_max() -> list:
    return get_pages_iphones.page_iphone_13_pro_max()

@get_content_iphone
def iphone_13_pro() -> list:
    return get_pages_iphones.page_iphone_13_pro()
       
@get_content_iphone
def iphone_13() -> list:
    return get_pages_iphones.page_iphone_13()

@get_content_iphone   
def iphone_13_mini() -> list:
    return get_pages_iphones.page_iphone_13_mini()

@get_content_iphone
def iphone_12_pro_max() -> list:
    return get_pages_iphones.page_iphone_12_pro_max()

@get_content_iphone
def iphone_12_pro() -> list:
    return get_pages_iphones.page_iphone_12_pro()

@get_content_iphone
def iphone_12() -> list:
    return get_pages_iphones.page_iphone_12()
        
@get_content_iphone
def iphone_12_mini() -> list:
    return get_pages_iphones.page_iphone_12_mini()
        
@get_content_iphone
def iphone_11_pro_max() -> list:
    return get_pages_iphones.page_iphone_11_pro_max()

@get_content_iphone      
def iphone_11_pro() -> list:
    return get_pages_iphones.page_iphone_11_pro()
        
@get_content_iphone
def iphone_11() -> list:
    return get_pages_iphones.page_iphone_11()

@get_content_iphone      
def iphone_se_2020() -> list:
    return get_pages_iphones.page_iphone_se_2020()

@get_content_iphone       
def iphone_se_2022() -> list:
    return get_pages_iphones.page_iphone_se_2022()

@get_content_iphone       
def iphone_xr() -> list:
    return get_pages_iphones.page_iphone_xr()