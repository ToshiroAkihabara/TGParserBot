from parser.catalogs_data import get_catalogs_mac
from parser.handlers.get_pages_handlers import get_pages
from typing import TypeAlias, TypedDict

LinksOfPages: TypeAlias = list


class Collection(TypedDict):
    catalog_name: str
    last_page: int


@get_pages
def page_macbook_pro() -> Collection:
    return get_catalogs_mac.macbook_pro().items()


@get_pages
def page_macbook_air() -> Collection:
    return get_catalogs_mac.macbook_air().items()


@get_pages
def page_imac() -> Collection:
    return get_catalogs_mac.imac().items()


@get_pages
def page_mac_mini() -> Collection:
    return get_catalogs_mac.mac_mini().items()


@get_pages
def page_mac_studio() -> Collection:
    return get_catalogs_mac.mac_studio().items()
