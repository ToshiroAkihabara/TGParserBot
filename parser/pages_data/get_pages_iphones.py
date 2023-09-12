from parser.catalogs_data import get_catalogs_iphones
from parser.handlers.get_pages_handlers import get_pages
from typing import TypeAlias, TypedDict

LinksOfPages: TypeAlias = list


class Collection(TypedDict):
    catalog_name: str
    last_page: int


@get_pages
def page_iphone_14_pro_max() -> Collection:
    return get_catalogs_iphones.iphone_14_pro_max().items()


@get_pages
def page_iphone_14_pro() -> Collection:
    return get_catalogs_iphones.iphone_14_pro().items()


@get_pages
def page_iphone_14_plus() -> Collection:
    return get_catalogs_iphones.iphone_14_plus().items()


@get_pages
def page_iphone_14() -> Collection:
    return get_catalogs_iphones.iphone_14().items()


@get_pages
def page_iphone_13_pro_max() -> Collection:
    return get_catalogs_iphones.iphone_13_pro_max().items()


@get_pages
def page_iphone_13_pro() -> Collection:
    return get_catalogs_iphones.iphone_13_pro().items()


@get_pages
def page_iphone_13() -> Collection:
    return get_catalogs_iphones.iphone_13().items()


@get_pages
def page_iphone_13_mini() -> Collection:
    return get_catalogs_iphones.iphone_13_mini().items()


@get_pages
def page_iphone_12_pro_max() -> Collection:
    return get_catalogs_iphones.iphone_12_pro_max().items()


@get_pages
def page_iphone_12_pro() -> Collection:
    return get_catalogs_iphones.iphone_12_pro().items()


@get_pages
def page_iphone_12() -> Collection:
    return get_catalogs_iphones.iphone_12().items()


@get_pages
def page_iphone_12_mini() -> Collection:
    return get_catalogs_iphones.iphone_12_mini().items()


@get_pages
def page_iphone_11_pro_max() -> Collection:
    return get_catalogs_iphones.iphone_11_pro_max().items()


@get_pages
def page_iphone_11_pro() -> Collection:
    return get_catalogs_iphones.iphone_11_pro().items()


@get_pages
def page_iphone_11() -> Collection:
    return get_catalogs_iphones.iphone_11().items()


@get_pages
def page_iphone_se_2020() -> Collection:
    return get_catalogs_iphones.iphone_se_2020().items()


@get_pages
def page_iphone_se_2022() -> Collection:
    return get_catalogs_iphones.iphone_se_2022().items()


@get_pages
def page_iphone_xr() -> Collection:
    return get_catalogs_iphones.iphone_xr().items()
