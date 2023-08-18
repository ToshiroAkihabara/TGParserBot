from parser.catalogs_data import get_catalogs_watch

def page_apple():
    for key, count in get_catalogs_watch.apple().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_samsung():
    for key, count in get_catalogs_watch.samsung().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_amazfit():
    for key, count in get_catalogs_watch.amazfit().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_honor():
    for key, count in get_catalogs_watch.honor().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_huawei():
    for key, count in get_catalogs_watch.huawei().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_garmin():
    for key, count in get_catalogs_watch.garmin().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_xiaomi():
    for key, count in get_catalogs_watch.xiaomi().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_realme():
    for key, count in get_catalogs_watch.realme().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_child():
    for key, count in get_catalogs_watch.child().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_suunto():
    for key, count in get_catalogs_watch.suunto().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_pixel():
    for key, count in get_catalogs_watch.pixel().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links