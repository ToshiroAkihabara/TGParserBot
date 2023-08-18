from parser.catalogs_data import get_catalogs_mac

def page_macbook_pro():
    for key, count in get_catalogs_mac.macbook_pro().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_macbook_air():
    for key, count in get_catalogs_mac.macbook_air().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_imac():
    for key, count in get_catalogs_mac.imac().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_mac_mini():
    for key, count in get_catalogs_mac.mac_mini().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_mac_studio():
    for key, count in get_catalogs_mac.mac_studio().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links