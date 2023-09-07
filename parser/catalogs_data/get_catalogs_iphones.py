from parser.handlers.get_catalogs_handler import get_catalog
from typing import TypeAlias

SliceOfPage: TypeAlias = int

@get_catalog("iphone")
def iphone_14_pro_max() -> SliceOfPage:
    return 0


@get_catalog("iphone")
def iphone_14_pro() -> SliceOfPage:
    return 1


@get_catalog("iphone")
def iphone_14_plus() -> SliceOfPage:
    return 2


@get_catalog("iphone")
def iphone_14() -> SliceOfPage:
    return 3


@get_catalog("iphone")
def iphone_13_pro_max() -> SliceOfPage:
    return 4


@get_catalog("iphone")
def iphone_13_pro() -> SliceOfPage:
    return 5


@get_catalog("iphone")
def iphone_13() -> SliceOfPage:
    return 6


@get_catalog("iphone")
def iphone_13_mini() -> SliceOfPage:
    return 7


@get_catalog("iphone")
def iphone_12_pro_max() -> SliceOfPage:
    return 8


@get_catalog("iphone")
def iphone_12_pro() -> SliceOfPage:
    return 9


@get_catalog("iphone")
def iphone_12() -> SliceOfPage:
    return 10


@get_catalog("iphone")
def iphone_12_mini() -> SliceOfPage:
    return 11


@get_catalog("iphone")
def iphone_11_pro_max() -> SliceOfPage:
    return 12


@get_catalog("iphone")
def iphone_11_pro() -> SliceOfPage:
    return 13


@get_catalog("iphone")
def iphone_11() -> SliceOfPage:
    return 14


@get_catalog("iphone")
def iphone_se_2020() -> SliceOfPage:
    return 15


@get_catalog("iphone")
def iphone_se_2022() -> SliceOfPage:
    return 16


@get_catalog("iphone")
def iphone_xr() -> SliceOfPage:
    return 17
