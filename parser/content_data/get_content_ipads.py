from parser.pages_data import get_pages_ipads
from parser.handlers.get_content_handlers import upload_content_to_files
from typing import TypeAlias

LinksOfPages: TypeAlias = list

@upload_content_to_files("ipad")
def ipad_pro() -> LinksOfPages:
    return get_pages_ipads.page_ipad_pro()


@upload_content_to_files("ipad")
def ipad_air() -> LinksOfPages:
    return get_pages_ipads.page_ipad_air()


@upload_content_to_files("ipad")
def ipad_mini() -> LinksOfPages:
    return get_pages_ipads.page_ipad_mini()


@upload_content_to_files("ipad")
def ipad() -> LinksOfPages:
    return get_pages_ipads.page_ipad()


