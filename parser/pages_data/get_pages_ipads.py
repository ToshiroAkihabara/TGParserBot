from parser.catalogs_data import get_catalogs_ipads
from parser.handlers.get_pages_handlers import get_pages
from typing import TypeAlias, TypedDict

LinksOfPages: TypeAlias = list


class Collection(TypedDict):
    catalog_name: str
    last_page: int


@get_pages
def page_ipad_pro() -> Collection:
    return get_catalogs_ipads.ipad_pro().items()


@get_pages
def page_ipad_air() -> Collection:
    return get_catalogs_ipads.ipad_air().items()


@get_pages
def page_ipad_mini() -> Collection:
    return get_catalogs_ipads.ipad_mini().items()


@get_pages
def page_ipad() -> Collection:
    return get_catalogs_ipads.ipad().items()
