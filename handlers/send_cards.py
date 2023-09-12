from aiogram.utils.markdown import hbold, hlink
from handlers.answers import advice_message, choose_other_model_message
from dataclasses import dataclass
from create_bot import bot
from markups import user_markups

import json
import os


@dataclass(slots=True, frozen=True)
class MessageCard:
    title: str
    url: str
    available: str
    price: int


@dataclass(slots=True, frozen=True)
class BotMessageMarkup:
    message: str
    keyboard: user_markups


async def send_cards_to_user(event, model) -> MessageCard:
    await bot.send_message(event.from_user.id, "Сбор данных завершен, подгружаю..")
    with open(f"{model}.json", encoding="utf-8") as file:
        data = json.load(file)
    if len(data) > 0:
        for item in data:
            await sending_process(item, event)
        os.remove(f"{model}.json")
        await reply_choose_model(event, model)
    else:
        os.remove(f"{model}.json")
        await reply_sold_model(event, model)


async def sending_process(item, event):
    card = (
        f"{hlink(item.get('title'), item.get('url'))}\n"
        f"{hbold('Доступность: ')} {item.get('available')}🔥\n"
        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
    )
    await bot.send_message(event.from_user.id, card)


async def reply_choose_model(event, model) -> BotMessageMarkup:
    if model.split("_")[0] == "ipad":
        await bot.send_message(
            event.from_user.id,
            await advice_message(),
            reply_markup=user_markups.ipad(),
        )
    elif model.split("_")[0] == "iphone":
        await bot.send_message(
            event.from_user.id,
            await advice_message(),
            reply_markup=user_markups.iphones(),
        )
    elif model.split("_")[0] == "macbook":
        await bot.send_message(
            event.from_user.id, await advice_message(), reply_markup=user_markups.mac(),
        )
    elif model.split("_")[0] == "imac":
        await bot.send_message(
            event.from_user.id, await advice_message(), reply_markup=user_markups.mac(),
        )
    elif model.split("_")[0] == "mac":
        await bot.send_message(
            event.from_user.id, await advice_message(), reply_markup=user_markups.mac(),
        )


async def reply_sold_model(event, model: str) -> BotMessageMarkup:
    if model.split("_")[0] == "ipad":
        await bot.send_message(
            event.from_user.id,
            await choose_other_model_message(),
            reply_markup=user_markups.ipad(),
        )
    elif model.split("_")[0] == "iphone":
        await bot.send_message(
            event.from_user.id,
            await choose_other_model_message(),
            reply_markup=user_markups.iphones(),
        )
    elif model.split("_")[0] == "macbook":
        await bot.send_message(
            event.from_user.id,
            await choose_other_model_message(),
            reply_markup=user_markups.mac(),
        )
    elif model.split("_")[0] == "imac":
        await bot.send_message(
            event.from_user.id,
            await choose_other_model_message(),
            reply_markup=user_markups.mac(),
        )
    elif model.split("_")[0] == "mac":
        await bot.send_message(
            event.from_user.id,
            await choose_other_model_message(),
            reply_markup=user_markups.mac(),
        )
