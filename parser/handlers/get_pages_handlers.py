from typing import TypeAlias, TypedDict

LinksOfPages: TypeAlias = list

class Collection(TypedDict):
    catalog_name: str
    last_page: int

def get_pages(func: Collection) -> LinksOfPages:
    def wrapper():
        links = []
        for key, count in func():
            for count in range(1, count + 1):
                url = f"https://pitergsm.ru{key}?PAGEN_1={count}"
                links.append(url)
        return links
    return wrapper
