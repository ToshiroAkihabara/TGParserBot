from bs4 import BeautifulSoup as BS
from parser.config import headers
from typing import TypeAlias
from requests.exceptions import RequestException
import requests
import json
import time

Catalogs: TypeAlias = list
SliceOfUrl: TypeAlias = int


def upload_catalogs_to_file() -> Catalogs:
    try:
        url = "https://pitergsm.ru/catalog/"
        try:
            response = requests.get(url=url, headers=headers)
        except RequestException:
            raise RequestException(f"Bad url: {url}.")
        if response.status_code == 200:
            parse = BS(response.text, "lxml")
            catalogs_href = parse.find_all("div", class_="catalog__item")
            catalog_list = []
            for catalog in catalogs_href:
                catalog_href = catalog.get("href")
                catalog_list.append(catalog_href)
            with open("catalogs.json", "w", encoding="utf-8") as file:
                json.dump(catalog_list, file, indent=4, ensure_ascii=False)
        else:
            return "HTTP 400 Bad Request!"
    except Exception as ex:
        print(f"Error: {ex}")


def open_catalogs_from_file(range: SliceOfUrl) -> Catalogs:
    try:
        with open("catalogs.json", encoding="utf-8") as file:
            catalogs = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("catalogs.json wasn't found")

    url = f"https://pitergsm.ru{catalogs[range]}"
    try:
        response = requests.get(url=url, headers=headers)
    except RequestException:
        raise RequestException(f"Bad url: {url}.")
    if response.status_code == 200:
        parse = BS(response.text, "lxml")
        catalogs_href = parse.find_all("li", class_="button-line__item")
        catalog_list = []
        for catalog in catalogs_href:
            catalog_href = catalog.find("a", class_="button-line__btn").get("href")
            catalog_list.append(catalog_href)
        return catalog_list


def get_catalogs_list(range: SliceOfUrl) -> Catalogs:
    try:
        return open_catalogs_from_file(range)
    except FileNotFoundError:
        upload_catalogs_to_file()
        time.sleep(2)
        return open_catalogs_from_file(range)
    except TypeError:
        raise TypeError("Unknown type")


def iphones() -> Catalogs:
    return get_catalogs_list(0)


def ipad() -> Catalogs:
    return get_catalogs_list(1)


def mac() -> Catalogs:
    return get_catalogs_list(2)
