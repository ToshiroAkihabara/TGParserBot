from parser.parser_data import get_all_catalogs, get_pagination
from typing import TypeAlias, TypedDict

ModelName: TypeAlias = str
SliceOfUrl: TypeAlias = int


class Collection(TypedDict):
    catalog_name: str
    last_page: int


def get_catalog(name: ModelName) -> Collection:
    def wrapper_catalogs(func: SliceOfUrl):
        def wrapper():
            number = func()
            if name == "ipad":
                catalog = get_all_catalogs.ipad()
            elif name == "iphone":
                catalog = get_all_catalogs.iphones()
            elif name == "mac":
                catalog = get_all_catalogs.mac()
            else:
                raise ValueError("Unknown value")
            collection = {}
            for catalog_name, last_page in get_pagination.get_pagination(
                catalog[number]
            ):
                collection[catalog_name] = last_page
            return collection

        return wrapper

    return wrapper_catalogs
