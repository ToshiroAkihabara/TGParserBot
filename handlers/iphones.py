from aiogram import types, Router, F
from aiogram.utils.markdown import hlink
from create_bot import bot
from markups import user_markups
from parser.content_data import get_content_iphones
from handlers.send_cards import send_cards_to_user
from handlers.answers import answer_callback_query
from dataclasses import dataclass
from typing import TypeAlias

MessageBot: TypeAlias = str


@dataclass(slots=True, frozen=True)
class BotMessageMarkup:
    message: str
    keyboard: user_markups


router = Router()


@router.callback_query(F.data == "start")
@router.callback_query(F.data == "back")
async def start_and_back(event: types.CallbackQuery) -> BotMessageMarkup:
    await answer_callback_query(event.id, event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        "Выберите интересующий каталог:",
        reply_markup=user_markups.catalogs(),
    )


@router.callback_query(F.data == "close")
async def close(event: types.CallbackQuery) -> MessageBot:
    await answer_callback_query(event.id, event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        f"Please, send your suggestions and wishes in {hlink('telegram', 'https://t.me/ToshiroAi')}",
    )


@router.callback_query(F.data == "iphone")
async def iphone(event: types.CallbackQuery) -> BotMessageMarkup:
    await answer_callback_query(event.id, event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id, f"Выберите модель📱:", reply_markup=user_markups.iphones()
    )


@router.callback_query(lambda event: event.data.startswith("iphone_"))
async def iphone_models(event: types.callback_query.CallbackQuery) -> MessageBot:
    model = event.data
    await answer_callback_query(event.id, event.from_user.id, event.message.message_id)
    await bot.send_message(
        event.from_user.id,
        f"Ориентировочное время сбора данных ⏳1-2 мин.\nПожалуйста, дождитесь завершения..",
    )
    if model == "iphone_14_pro_max":
        get_content_iphones.iphone_14_pro_max()
        await send_cards_to_user(event, model)

    elif model == "iphone_14_pro":
        get_content_iphones.iphone_14_pro()
        await send_cards_to_user(event, model)

    elif model == "iphone_14_plus":
        get_content_iphones.iphone_14_plus()
        await send_cards_to_user(event, model)

    elif model == "iphone_14":
        get_content_iphones.iphone_14()
        await send_cards_to_user(event, model)

    elif model == "iphone_13_pro_max":
        get_content_iphones.iphone_13_pro_max()
        await send_cards_to_user(event, model)

    elif model == "iphone_13_pro":
        get_content_iphones.iphone_13_pro()
        await send_cards_to_user(event, model)

    elif model == "iphone_13":
        get_content_iphones.iphone_13()
        await send_cards_to_user(event, model)

    elif model == "iphone_13_mini":
        get_content_iphones.iphone_13_mini()
        await send_cards_to_user(event, model)

    elif model == "iphone_12_pro_max":
        get_content_iphones.iphone_12_pro_max()
        await send_cards_to_user(event, model)

    elif model == "iphone_12_pro":
        get_content_iphones.iphone_12_pro()
        await send_cards_to_user(event, model)

    elif model == "iphone_12":
        get_content_iphones.iphone_12()
        await send_cards_to_user(event, model)

    elif model == "iphone_12_mini":
        get_content_iphones.iphone_12_mini()
        await send_cards_to_user(event, model)

    elif model == "iphone_11_pro_max":
        get_content_iphones.iphone_11_pro_max()
        await send_cards_to_user(event, model)

    elif model == "iphone_11_pro":
        get_content_iphones.iphone_11_pro()
        await send_cards_to_user(event, model)

    elif model == "iphone_11":
        get_content_iphones.iphone_11()
        await send_cards_to_user(event, model)

    elif model == "iphone_se_2020":
        get_content_iphones.iphone_se_2020()
        await send_cards_to_user(event, model)

    elif model == "iphone_se_2022":
        get_content_iphones.iphone_se_2022()
        await send_cards_to_user(event, model)

    else:
        await bot.send_message(
            event.from_user.id, "Упс..Что-то пошло не так.\nПопробуйте снова."
        )
