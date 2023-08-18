from parser.catalogs_data import get_catalogs_ipads

def page_ipad_pro():
    for key, count in get_catalogs_ipads.ipad_pro().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links

def page_ipad_air():
    for key, count in get_catalogs_ipads.ipad_air().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_ipad_mini():
    for key, count in get_catalogs_ipads.ipad_mini().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links
    
def page_ipad():
    for key, count in get_catalogs_ipads.ipad().items():
        links = []
        for count in range(1, count+1):
            url = f'https://pitergsm.ru{key}?PAGEN_1={count}'
            links.append(url)
        return links