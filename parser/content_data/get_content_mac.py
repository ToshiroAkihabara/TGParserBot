from parser.pages_data import get_pages_mac
from parser.handlers.get_content_handlers import upload_content_to_files
from typing import TypeAlias

LinksOfPages: TypeAlias = list


@upload_content_to_files("mac")
def macbook_pro() -> LinksOfPages:
    return get_pages_mac.page_macbook_pro()


@upload_content_to_files("mac")
def macbook_air() -> LinksOfPages:
    return get_pages_mac.page_macbook_air()


@upload_content_to_files("mac")
def imac() -> LinksOfPages:
    return get_pages_mac.page_imac()


@upload_content_to_files("mac")
def mac_mini() -> LinksOfPages:
    return get_pages_mac.page_mac_mini()


@upload_content_to_files("mac")
def mac_studio() -> LinksOfPages:
    return get_pages_mac.page_mac_studio()
