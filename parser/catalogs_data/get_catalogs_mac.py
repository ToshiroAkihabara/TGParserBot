from parser.parser_data import get_all_catalogs, get_pagination

def catalogs_macbook(range: int) -> dict:
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination(catalog[range]):
        dict[catalog_name] = last_page
    return dict

def macbook_pro() -> dict:
    return catalogs_macbook(0)

def macbook_air() -> dict:
    return catalogs_macbook(1)

def imac() -> dict:
    return catalogs_macbook(2)

def mac_mini() -> dict:
    return catalogs_macbook(3)

def mac_studio() -> dict:
    return catalogs_macbook(5)