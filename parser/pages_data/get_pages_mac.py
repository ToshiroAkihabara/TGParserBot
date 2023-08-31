from parser.catalogs_data import get_catalogs_mac

def get_pages_mac(func) -> list:
    def wrapper():
        links = []
        for key, count in func():
            for count in range(1, count+1):
                url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
                links.append(url)
        return links
    return wrapper
    
@get_pages_mac
def page_macbook_pro() -> dict:
    return get_catalogs_mac.macbook_pro().items()

@get_pages_mac
def page_macbook_air() -> dict:
    return get_catalogs_mac.macbook_air().items()

@get_pages_mac
def page_imac() -> dict:
    return get_catalogs_mac.imac().items()

@get_pages_mac
def page_mac_mini() -> dict:
    return get_catalogs_mac.mac_mini().items()

@get_pages_mac
def page_mac_studio() -> dict:
    return get_catalogs_mac.mac_studio().items()