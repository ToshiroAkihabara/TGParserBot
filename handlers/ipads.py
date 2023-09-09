from aiogram import types, Router, F
from aiogram.utils.markdown import hlink
from create_bot import bot
from markups import user_markups
from parser.content_data import get_content_ipads
from handlers.sendcards import send_cards_to_user
from dataclasses import dataclass
from typing import TypeAlias


MessageBot: TypeAlias = str


@dataclass(slots=True, frozen=True)
class BotMessageMarkup:
    message: str
    keyboard: user_markups


@dataclass(slots=True, frozen=True)
class MessageCard:
    title: str
    url: str
    available: str
    price: int


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


@router.callback_query(F.data == "ipad")
async def ipad(event: types.CallbackQuery) -> BotMessageMarkup:
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id, f"Выберите модель📲:", reply_markup=user_markups.ipad()
    )


@router.callback_query(lambda event: event.data.startswith("ipad_"))
async def ipad_models(event: types.CallbackQuery) -> MessageBot:
    model = event.data
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        f"Ориентировочное время сбора данных ⏳1-2 мин.\nПожалуйста, дождитесь завершения..",
    )
    if model == "ipad_":
        get_content_ipads.ipad()
        await send_cards_to_user(event, model)

    elif model == "ipad_pro":
        get_content_ipads.ipad_pro()
        await send_cards_to_user(event, model)

    elif model == "ipad_air":
        get_content_ipads.ipad_air()
        await send_cards_to_user(event, model)

    elif model == "ipad_mini":
        get_content_ipads.ipad_mini()
        await send_cards_to_user(event, model)

    else:
        await bot.send_message(
            event.from_user.id, "Упс..Что-то пошло не так.\nПопробуйте снова."
        )
