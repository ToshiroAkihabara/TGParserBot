from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def starts() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Запустить", callback_data="start"))

    return builder.as_markup()


def catalogs() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Айфоны", callback_data="iphone"),
        InlineKeyboardButton(text="Айпады", callback_data="ipad"),
        InlineKeyboardButton(text="Макбуки", callback_data="mac"),
        InlineKeyboardButton(text="Другое", callback_data="other"),
        InlineKeyboardButton(text="Закрыть", callback_data="close"),
    )
    builder.adjust(2)

    return builder.as_markup()


def iphones() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Iphone 14 Pro Max", callback_data="iphone_14_pro_max"
        ),
        InlineKeyboardButton(text="Iphone 14 Pro", callback_data="iphone_14_pro"),
        InlineKeyboardButton(text="Iphone 14 Plus", callback_data="iphone_14_plus"),
        InlineKeyboardButton(text="Iphone 14", callback_data="iphone_14"),
        InlineKeyboardButton(
            text="Iphone 13 Pro Max", callback_data="iphone_13_pro_max"
        ),
        InlineKeyboardButton(text="Iphone 13 Pro", callback_data="iphone_13_pro"),
        InlineKeyboardButton(text="Iphone 13", callback_data="iphone_13"),
        InlineKeyboardButton(text="Iphone 13 Mini", callback_data="iphone_13_mini"),
        InlineKeyboardButton(
            text="Iphone 12 Pro Max", callback_data="iphone_12_pro_max"
        ),
        InlineKeyboardButton(text="Iphone 12 Pro", callback_data="iphone_12_pro"),
        InlineKeyboardButton(text="Iphone 12", callback_data="iphone_12"),
        InlineKeyboardButton(text="Iphone 12 Mini", callback_data="iphone_12_mini"),
        InlineKeyboardButton(
            text="Iphone 11 Pro Max", callback_data="iphone_11_pro_max"
        ),
        InlineKeyboardButton(text="Iphone 11 Pro", callback_data="iphone_11_pro"),
        InlineKeyboardButton(text="Iphone 11", callback_data="iphone_11"),
        InlineKeyboardButton(text="Iphone SE 2020", callback_data="iphone_se_2020"),
        InlineKeyboardButton(text="Iphone SE 2022", callback_data="iphone_se_2022"),
        InlineKeyboardButton(text="Назад", callback_data="back"),
    )
    builder.adjust(2)

    return builder.as_markup()


def ipad() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Ipad", callback_data="ipad_"),
        InlineKeyboardButton(text="Ipad Mini", callback_data="ipad_mini"),
        InlineKeyboardButton(text="Ipad Air", callback_data="ipad_air"),
        InlineKeyboardButton(text="Ipad Pro", callback_data="ipad_pro"),
        InlineKeyboardButton(text="Назад", callback_data="back"),
    )
    builder.adjust(2)

    return builder.as_markup()


def mac() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Macbook Pro", callback_data="mac_book_pro"),
        InlineKeyboardButton(text="Macbook Air", callback_data="mac_book_air"),
        InlineKeyboardButton(text="iMac", callback_data="mac_"),
        InlineKeyboardButton(text="Mac Mini", callback_data="mac_mini"),
        InlineKeyboardButton(text="Mac Studio", callback_data="mac_studio"),
        InlineKeyboardButton(text="Назад", callback_data="back"),
    )
    builder.adjust(2)

    return builder.as_markup()


def back() -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Назад", callback_data="back"))
    builder.adjust(1)

    return builder.as_markup()
