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
            catalog_getters = {
                "ipad": get_all_catalogs.ipad,
                "iphone": get_all_catalogs.iphones,
                "mac": get_all_catalogs.mac,
            }
            if not (getter := catalog_getters[name]):
                raise ValueError(f"Unknown value: {name}")
            catalog = getter()

            collection = {}
            for catalog_name, last_page in get_pagination.get_pagination(
                catalog[number]
            ):
                collection[catalog_name] = last_page
            return collection

        return wrapper

    return wrapper_catalogs
