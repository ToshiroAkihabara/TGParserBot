from aiogram import types, Router, F
from aiogram.filters import Command
from create_bot import dp, bot, admin
from markups import user_markups
from handlers import ipads, iphones, mac
from typing import TypeAlias
import logging
import asyncio

logger = logging.getLogger(__name__)
log_level = logging.INFO

MessageFromBot: TypeAlias = str


async def on_startup() -> MessageFromBot:
    logging.basicConfig(
        level=logging.INFO,
        format=u"%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    await bot.set_my_commands(
        [
            types.BotCommand(command="/help", description="Список команд"),
            types.BotCommand(command="/start", description="Запуск бота"),
        ]
    )
    await bot.send_message(admin, "Бот запущен🔋")


async def shutdown() -> MessageFromBot:
    await bot.send_message(admin, "Бот отключен🪫")


async def main() -> None:
    try:

        router = Router()

        @router.message(F.text == "Запустить")
        async def start(message: types.Message):
            await message.answer(
                "Добро пожаловать в парсер актуальных цен сайта https://pitergsm.ru/\nВыберите интересующий каталог:",
                reply_markup=user_markups.catalogs(),
            )
            await message.delete()

        @router.message(Command("start"))
        async def start(message: types.Message):
            await message.answer(
                "Добро пожаловать в парсер актуальных цен сайта https://pitergsm.ru/\nВыберите интересующий каталог:",
                reply_markup=user_markups.catalogs(),
            )

        @router.message(Command("help"))
        async def help(message: types.Message):
            await message.answer_sticker(
                "CAACAgIAAxkBAAEKC-lk3T7zeZwNYao4LRNikgdLI87O7AAClyAAAt88OUtsjjyKWQ5bXjAE"
            )
            await message.answer(
                "Список команд:\n/start - запустить бота;\n/help - помощь."
            )

        @router.callback_query(F.data == "other")
        async def other(call: types.CallbackQuery):
            await bot.send_message(
                call.from_user.id,
                "Остальные каталоги по аналогии с открытым исходным кодом, вы сможете добавить сами.\nПриведенный функционал служит всего лишь примером интеграции простого парсера данных в чат-бота телеграм.",
                reply_markup=user_markups.back(),
            )

        @router.message()
        async def empty(message: types.Message):
            await message.answer(
                'Нажмите "Запустить" для начала работы или напишите /help',
                reply_markup=user_markups.starts(),
            )

        dp.startup.register(on_startup)
        dp.shutdown.register(shutdown)

        dp.include_routers(iphones.router, ipads.router, mac.router, router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, on_startup=on_startup)
        await dp.run_polling(bot, allowed_updates=dp.resolve_used_update_types())

    except Exception as ex:
        logger.error(ex)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        logging.error(ex)
