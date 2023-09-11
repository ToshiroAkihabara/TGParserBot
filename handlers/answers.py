from create_bot import bot


async def answer_callback_query(id, from_user_id, message_id):
    await bot.answer_callback_query(id)
    await bot.delete_message(from_user_id, message_id)


async def advice_message():
    return "Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️"


async def choose_other_model_message():
    return "В настоящий момент, все экземпляры данной модели распроданы☹️\nВыберите другую модель:"
