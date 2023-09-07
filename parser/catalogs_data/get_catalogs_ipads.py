from parser.handlers.get_catalogs_handler import get_catalog
from typing import TypeAlias

SliceOfPage: TypeAlias = int

@get_catalog("ipad")
def ipad_pro() -> SliceOfPage:
    return 0

@get_catalog("ipad")
def ipad_air() -> SliceOfPage:
    return 1

@get_catalog("ipad")
def ipad_mini() -> SliceOfPage:
    return 2

@get_catalog("ipad")
def ipad() -> SliceOfPage:
    return 3