from parser.pages_data import get_pages_iphones
from parser.handlers.get_content_handlers import upload_content_to_files
from typing import TypeAlias

LinksOfPages: TypeAlias = list


@upload_content_to_files("iphone")
def iphone_14_pro_max() -> LinksOfPages:
    return get_pages_iphones.page_iphone_14_pro_max()


@upload_content_to_files("iphone")
def iphone_14_pro() -> LinksOfPages:
    return get_pages_iphones.page_iphone_14_pro()


@upload_content_to_files("iphone")
def iphone_14_plus() -> LinksOfPages:
    return get_pages_iphones.page_iphone_14_plus()


@upload_content_to_files("iphone")
def iphone_14() -> LinksOfPages:
    return get_pages_iphones.page_iphone_14()


@upload_content_to_files("iphone")
def iphone_13_pro_max() -> LinksOfPages:
    return get_pages_iphones.page_iphone_13_pro_max()


@upload_content_to_files("iphone")
def iphone_13_pro() -> LinksOfPages:
    return get_pages_iphones.page_iphone_13_pro()


@upload_content_to_files("iphone")
def iphone_13() -> LinksOfPages:
    return get_pages_iphones.page_iphone_13()


@upload_content_to_files("iphone")
def iphone_13_mini() -> LinksOfPages:
    return get_pages_iphones.page_iphone_13_mini()


@upload_content_to_files("iphone")
def iphone_12_pro_max() -> LinksOfPages:
    return get_pages_iphones.page_iphone_12_pro_max()


@upload_content_to_files("iphone")
def iphone_12_pro() -> LinksOfPages:
    return get_pages_iphones.page_iphone_12_pro()


@upload_content_to_files("iphone")
def iphone_12() -> LinksOfPages:
    return get_pages_iphones.page_iphone_12()


@upload_content_to_files("iphone")
def iphone_12_mini() -> LinksOfPages:
    return get_pages_iphones.page_iphone_12_mini()


@upload_content_to_files("iphone")
def iphone_11_pro_max() -> LinksOfPages:
    return get_pages_iphones.page_iphone_11_pro_max()


@upload_content_to_files("iphone")
def iphone_11_pro() -> LinksOfPages:
    return get_pages_iphones.page_iphone_11_pro()


@upload_content_to_files("iphone")
def iphone_11() -> LinksOfPages:
    return get_pages_iphones.page_iphone_11()


@upload_content_to_files("iphone")
def iphone_se_2020() -> LinksOfPages:
    return get_pages_iphones.page_iphone_se_2020()


@upload_content_to_files("iphone")
def iphone_se_2022() -> LinksOfPages:
    return get_pages_iphones.page_iphone_se_2022()


@upload_content_to_files("iphone")
def iphone_xr() -> LinksOfPages:
    return get_pages_iphones.page_iphone_xr()
