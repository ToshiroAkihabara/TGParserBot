from parser.parser_data import get_all_catalogs, get_pagination

def catalogs_ipad(range: int) -> dict:
    catalog = get_all_catalogs.ipad()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination(catalog[range]):
        dict[catalog_name] = last_page
    return dict

def ipad_pro() -> dict:
    return catalogs_ipad(0)

def ipad_air() -> dict:
    return catalogs_ipad(1)

def ipad_mini() -> dict:
    return catalogs_ipad(2)

def ipad() -> dict:
    return catalogs_ipad(3)

