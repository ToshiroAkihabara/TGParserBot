from parser.handlers.headers import headers
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass
from typing import TypeAlias
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
            all_data = []
            for url in func():
                if category == "iphone" or "mac":
                    name = url.split("/")[6].replace("-", "_")
                elif category == "ipad":
                    name = url.split("/")[7].replace("-", "_")
                    if name == "ipad":
                        name = "ipad_"
                else:
                    raise AttributeError("Unknown value")
                response = requests.get(url=url, headers=headers)
                scr = response.text
                soup = BS(scr, "lxml")
                data = soup.find_all("div", class_="catalog__list like-cards")
                for item in data:
                    cards = item.find_all("div", class_="catalog__item")
                    for card in cards:
                        try:
                            all_data.append(
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
                json.dump(all_data, file, indent=4, ensure_ascii=False)
        return wrapper
    return wrapper_content















