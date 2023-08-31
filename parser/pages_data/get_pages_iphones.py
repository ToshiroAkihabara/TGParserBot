from parser.catalogs_data import get_catalogs_iphones

def get_pages_iphone(func) -> list:
    def wrapper():
        links = []
        for key, count in func():
            for count in range(1, count+1):
                url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
                links.append(url)
        return links
    return wrapper

@get_pages_iphone
def page_iphone_14_pro_max() -> dict:
    return get_catalogs_iphones.iphone_14_pro_max().items()

@get_pages_iphone
def page_iphone_14_pro() -> dict:
    return get_catalogs_iphones.iphone_14_pro().items()

@get_pages_iphone
def page_iphone_14_plus() -> dict:
    return get_catalogs_iphones.iphone_14_plus().items()

@get_pages_iphone
def page_iphone_14() -> dict:
    return get_catalogs_iphones.iphone_14().items()

@get_pages_iphone
def page_iphone_13_pro_max() -> dict:
    return get_catalogs_iphones.iphone_13_pro_max().items()
    
@get_pages_iphone
def page_iphone_13_pro() -> dict:
    return get_catalogs_iphones.iphone_13_pro().items()

@get_pages_iphone
def page_iphone_13() -> dict:
    return get_catalogs_iphones.iphone_13().items()

@get_pages_iphone
def page_iphone_13_mini() -> dict:
    return get_catalogs_iphones.iphone_13_mini().items()

@get_pages_iphone
def page_iphone_12_pro_max() -> dict:
    return get_catalogs_iphones.iphone_12_pro_max().items()

@get_pages_iphone
def page_iphone_12_pro() -> dict:
    return get_catalogs_iphones.iphone_12_pro().items()

@get_pages_iphone    
def page_iphone_12() -> dict:
    return get_catalogs_iphones.iphone_12().items()

@get_pages_iphone
def page_iphone_12_mini() -> dict:
    return get_catalogs_iphones.iphone_12_mini().items()

@get_pages_iphone
def page_iphone_11_pro_max() -> dict:
    return get_catalogs_iphones.iphone_11_pro_max().items()

@get_pages_iphone
def page_iphone_11_pro() -> dict:
    return get_catalogs_iphones.iphone_11_pro().items()

@get_pages_iphone
def page_iphone_11() -> dict:
    return get_catalogs_iphones.iphone_11().items()

@get_pages_iphone
def page_iphone_se_2020() -> dict:
    return get_catalogs_iphones.iphone_se_2020().items()
       
@get_pages_iphone
def page_iphone_se_2022() -> dict:
    return get_catalogs_iphones.iphone_se_2022().items()

@get_pages_iphone
def page_iphone_xr() -> dict:
    return get_catalogs_iphones.iphone_xr().items()
