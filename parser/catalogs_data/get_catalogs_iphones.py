from parser.parser_data import get_all_catalogs, get_pagination

def get_catalogs_iphone(range: int) -> dict:
    catalog = get_all_catalogs.iphones()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination(catalog[range]):
        dict[catalog_name] = last_page
    return dict

def iphone_14_pro_max() -> dict:
    return get_catalogs_iphone(0)

def iphone_14_pro() -> dict:
    return get_catalogs_iphone(1)

def iphone_14_plus() -> dict:
    return get_catalogs_iphone(2)

def iphone_14() -> dict:
    return get_catalogs_iphone(3)

def iphone_13_pro_max() -> dict:
    return get_catalogs_iphone(4)

def iphone_13_pro() -> dict:
    return get_catalogs_iphone(5)

def iphone_13() -> dict:
    return get_catalogs_iphone(6)

def iphone_13_mini() -> dict:
    return get_catalogs_iphone(7)

def iphone_12_pro_max() -> dict:
    return get_catalogs_iphone(8)

def iphone_12_pro() -> dict:
    return get_catalogs_iphone(9)

def iphone_12() -> dict:
    return get_catalogs_iphone(10)

def iphone_12_mini() -> dict:
    return get_catalogs_iphone(11)

def iphone_11_pro_max() -> dict:
    return get_catalogs_iphone(12)

def iphone_11_pro() -> dict:
    return get_catalogs_iphone(13)

def iphone_11() -> dict:
    return get_catalogs_iphone(14)

def iphone_se_2020() -> dict:
    return get_catalogs_iphone(15)

def iphone_se_2022() -> dict:
    return get_catalogs_iphone(16)

def iphone_xr() -> dict:
    return get_catalogs_iphone(17)
