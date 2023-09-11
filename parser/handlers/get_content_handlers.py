from parser.config import headers
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass
from typing import TypeAlias
from requests.exceptions import RequestException
import requests
import json

Category: TypeAlias = str
Urls: TypeAlias = list


@dataclass(slots=True, frozen=True)
class CardOfGoods:
    title: str
    available: str
    price: int
    url: str


def upload_content_to_files(category: Category) -> CardOfGoods:
    def wrapper_content(func: Urls):
        def wrapper():
            cards = []
            for url in func():
                category_getters = {
                    "iphone": url.split("/")[6].replace("-", "_"),
                    "imac": url.split("/")[6].replace("-", "_"),
                    "mac": url.split("/")[6].replace("-", "_"),
                    "ipad": url.split("/")[7].replace("-", "_"),
                }
                if not (getter := category_getters[category]):
                    raise AttributeError(f"Unknown value: {category}")
                name = getter
                if name == "ipad":
                    name = "ipad_"

                response = requests.get(url=url, headers=headers)
                if response.status_code == 200:
                    html_code = response.text
                    parse = BS(html_code, "lxml")
                    catalogs = parse.find_all("div", class_="catalog__list like-cards")
                    get_catalogs_cards(cards, catalogs)
                else:
                    raise RequestException(f"404 Not Found: {url}")

            upload_to_json(name, cards)

        return wrapper

    return wrapper_content


def get_catalogs_cards(cards, catalogs):

    for catalog in catalogs:
        items = catalog.find_all("div", class_="catalog__item")
        for card in items:
            try:
                cards.append(
                    {
                        "title": card.find("div", class_="prod-card__title").text,
                        "available": card.find(
                            "div", class_="prod-card__count icon-check-green nodesktop",
                        ).text,
                        "price": card.find("div", class_="price__now")
                        .text.replace("a", " ")
                        .strip(),
                        "url": "https://pitergsm.ru"
                        + card.find("div", class_="prod-card")
                        .find("a", class_="prod-card__link")
                        .get("href"),
                    }
                )
            except AttributeError:
                continue


def upload_to_json(name, cards):

    with open(f"{name}.json", "w", encoding="utf-8") as file:
        json.dump(cards, file, indent=4, ensure_ascii=False)
