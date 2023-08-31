from parser.catalogs_data import get_catalogs_ipads

def get_pages_ipad(func) -> list:
    def wrapper():
        links = []
        for key, count in func():
            for count in range(1, count+1):
                url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
                links.append(url)
        return links
    return wrapper

@get_pages_ipad
def page_ipad_pro() -> dict:
    return get_catalogs_ipads.ipad_pro().items()

@get_pages_ipad
def page_ipad_air() -> dict:
    return get_catalogs_ipads.ipad_air().items()

@get_pages_ipad
def page_ipad_mini() -> dict:
    return get_catalogs_ipads.ipad_mini().items()
    
@get_pages_ipad
def page_ipad() -> dict:
    return get_catalogs_ipads.ipad().items()
       