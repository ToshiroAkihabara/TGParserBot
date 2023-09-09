from parser.handlers.get_catalogs_handler import get_catalog
from typing import TypeAlias

SliceOfPage: TypeAlias = int


@get_catalog("mac")
def macbook_pro() -> SliceOfPage:
    return 0


@get_catalog("mac")
def macbook_air() -> SliceOfPage:
    return 1


@get_catalog("mac")
def imac() -> SliceOfPage:
    return 2


@get_catalog("mac")
def mac_mini() -> SliceOfPage:
    return 3


@get_catalog("mac")
def mac_studio() -> SliceOfPage:
    return 5
