from parser.parser_data import get_all_catalogs, get_pagination

def macbook_pro():
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[0]):
        dict[catalog_name] = last_page
    return dict

def macbook_air():
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[1]):
        dict[catalog_name] = last_page
    return dict

def imac():
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[2]):
        dict[catalog_name] = last_page
    return dict

def mac_mini():
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[3]):
        dict[catalog_name] = last_page
    return dict


def mac_studio():
    catalog = get_all_catalogs.mac()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[5]):
        dict[catalog_name] = last_page
    return dict