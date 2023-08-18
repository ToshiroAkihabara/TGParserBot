from parser.parser_data import get_all_catalogs, get_pagination

def apple():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[0]):
        dict[catalog_name] = last_page
    return dict

def samsung():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[1]):
        dict[catalog_name] = last_page
    return dict

def amazfit():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[2]):
        dict[catalog_name] = last_page
    return dict

def honor():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[3]):
        dict[catalog_name] = last_page
    return dict


def huawei():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[5]):
        dict[catalog_name] = last_page
    return dict

def garmin():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[6]):
        dict[catalog_name] = last_page
    return dict

def xiaomi():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[7]):
        dict[catalog_name] = last_page
    return dict

def realme():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[8]):
        dict[catalog_name] = last_page
    return dict

def child():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[9]):
        dict[catalog_name] = last_page
    return dict

def fitness():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[10]):
        dict[catalog_name] = last_page
    return dict

def suunto():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[11]):
        dict[catalog_name] = last_page
    return dict

def pixel():
    catalog = get_all_catalogs.watch()
    dict = {}
    for catalog_name, last_page in get_pagination.pagination_(catalog[12]):
        dict[catalog_name] = last_page
    return dict