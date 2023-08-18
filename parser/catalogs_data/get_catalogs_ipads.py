from parser.parser_data import get_all_catalogs, get_pagination

def ipad_pro():
    catalog = get_all_catalogs.ipad()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[0]):
        dict[catalog_name] = last_page
    return dict

def ipad_air():
    catalog = get_all_catalogs.ipad()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[1]):
        dict[catalog_name] = last_page
    return dict

def ipad_mini():
    catalog = get_all_catalogs.ipad()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[2]):
        dict[catalog_name] = last_page
    return dict

def ipad():
    catalog = get_all_catalogs.ipad()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[3]):
        dict[catalog_name] = last_page
    return dict


