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
                if category == "iphone":
                    name = url.split("/")[6].replace("-", "_")
                elif category == "imac":
                    name = url.split("/")[6].replace("-", "_")
                elif category == "mac":
                    name = url.split("/")[6].replace("-", "_")
                elif category == "ipad":
                    name = url.split("/")[7].replace("-", "_")
                    if name == "ipad":
                        name = "ipad_"
                else:
                    raise AttributeError("Unknown value")
                try:
                    response = requests.get(url=url, headers=headers)
                except RequestException:
                    raise RequestException(f"Bad url: {url}.")
                html_code = response.text
                parse = BS(html_code, "lxml")
                catalogs = parse.find_all("div", class_="catalog__list like-cards")
                for catalog in catalogs:
                    items = catalog.find_all("div", class_="catalog__item")
                    for card in items:
                        try:
                            cards.append(
                                {
                                    "title": card.find(
                                        "div", class_="prod-card__title"
                                    ).text,
                                    "available": card.find(
                                        "div",
                                        class_="prod-card__count icon-check-green nodesktop",
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
            with open(f"{name}.json", "w", encoding="utf-8") as file:
                json.dump(cards, file, indent=4, ensure_ascii=False)

        return wrapper

    return wrapper_content
