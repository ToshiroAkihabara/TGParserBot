from aiogram import types, Router, F
from aiogram.utils.markdown import hlink
from create_bot import bot
from markups import user_markups
from parser.content_data import get_content_mac
from handlers.sendcards import send_cards_to_user
from dataclasses import dataclass
from typing import TypeAlias


MessageBot: TypeAlias = str


@dataclass(slots=True, frozen=True)
class BotMessageMarkup:
    message: str
    keyboard: user_markups


router = Router()


@router.callback_query(F.data == "back")
async def back(event: types.CallbackQuery) -> BotMessageMarkup:
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        "Выберите интересующий каталог:",
        reply_markup=user_markups.catalogs(),
    )


@router.callback_query(F.data == "close")
async def close(event: types.CallbackQuery) -> MessageBot:
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        f"Please, send your suggestions and wishes in {hlink('telegram', 'https://t.me/ToshiroAi')}",
    )


@router.callback_query(F.data == "mac")
async def mac(event: types.CallbackQuery) -> BotMessageMarkup:
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id, f"Выберите модель💻:", reply_markup=user_markups.mac()
    )


@router.callback_query(lambda event: event.data.startswith("mac_"))
async def mac_models(event: types.CallbackQuery) -> MessageBot:
    model = event.data
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        f"Ориентировочное время сбора данных ⏳1-2 мин.\nПожалуйста, дождитесь завершения..",
    )
    if model == "mac_book_pro":
        get_content_mac.macbook_pro()
        model = "macbook_pro"
        await send_cards_to_user(event, model)

    elif model == "mac_book_air":
        get_content_mac.macbook_air()
        model = "macbook_air"
        await send_cards_to_user(event, model)

    elif model == "mac_":
        get_content_mac.imac()
        model = "imac"
        await send_cards_to_user(event, model)

    elif model == "mac_mini":
        get_content_mac.mac_mini()
        await send_cards_to_user(event, model)

    elif model == "mac_studio":
        get_content_mac.mac_studio()
        await send_cards_to_user(event, model)

    else:
        await bot.send_message(
            event.from_user.id, "Упс..Что-то пошло не так.\nПопробуйте снова."
        )
