from aiogram import types, Router, F
from aiogram.utils.markdown import hbold, hlink
from create_bot import bot
from markups import user_markups
from parser.content_data import get_content_mac

import json
import os

router = Router()

@router.callback_query(F.data == 'back') 
async def back(event: types.CallbackQuery):
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(event.from_user.id, 'Выберите интересующий каталог:', reply_markup=user_markups.catalogs())

@router.callback_query(F.data == 'close') 
async def close(event: types.CallbackQuery):
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(event.from_user.id, f"Please, send your suggestions and wishes in {hlink('telegram', 'https://t.me/ToshiroAi')}")

@router.callback_query(F.data == 'mac')
async def mac(event: types.CallbackQuery):
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(event.from_user.id, f'Выберите модель💻:', reply_markup=user_markups.mac())

@router.callback_query(lambda event: event.data.startswith('mac_'))
async def mac_models(event: types.CallbackQuery):
    value = event.data
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(event.from_user.id, f'Ориентировочное время сбора данных ⏳1-2 мин.\nПожалуйста, дождитесь завершения..')
    if value == 'mac_book_pro':
        get_content_mac.macbook_pro()
        value = 'macbook_pro'
        await bot.send_message(event.from_user.id, 'Сбор данных завершен, подгружаю..')
        with open(f'{value}.json', encoding='utf-8') as file:
            data = json.load(file)
        if len(data) > 0:
            try:
                for item in data:
                    card = f"{hlink(item.get('title'), item.get('url'))}\n" \
                        f"{hbold('Доступность: ')} {item.get('available')}🔥\n" \
                        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
                    await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.mac())
   
    elif value == 'mac_book_air':
        get_content_mac.macbook_air()
        value = 'macbook_air'
        await bot.send_message(event.from_user.id, 'Сбор данных завершен, подгружаю..')
        with open(f'{value}.json', encoding='utf-8') as file:
            data = json.load(file)
        if len(data) > 0:
            try:
                for item in data:
                    card = f"{hlink(item.get('title'), item.get('url'))}\n" \
                        f"{hbold('Доступность: ')} {item.get('available')}🔥\n" \
                        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
                    await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.mac())

    elif value == 'mac_':
        get_content_mac.imac()
        value = 'imac'
        await bot.send_message(event.from_user.id, 'Сбор данных завершен, подгружаю..')
        with open(f'{value}.json', encoding='utf-8') as file:
            data = json.load(file)
        if len(data) > 0:
            try:
                for item in data:
                    card = f"{hlink(item.get('title'), item.get('url'))}\n" \
                        f"{hbold('Доступность: ')} {item.get('available')}🔥\n" \
                        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
                    await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.mac())

    elif value == 'mac_mini':
        get_content_mac.mac_mini()
        await bot.send_message(event.from_user.id, 'Сбор данных завершен, подгружаю..')
        with open(f'{value}.json', encoding='utf-8') as file:
            data = json.load(file)
        if len(data) > 0:
            try:
                for item in data:
                    card = f"{hlink(item.get('title'), item.get('url'))}\n" \
                        f"{hbold('Доступность: ')} {item.get('available')}🔥\n" \
                        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
                    await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.mac())

    elif value == 'mac_studio':
        get_content_mac.mac_studio()
        await bot.send_message(event.from_user.id, 'Сбор данных завершен, подгружаю..')
        with open(f'{value}.json', encoding='utf-8') as file:
            data = json.load(file)
        if len(data) > 0:
            try:
                for item in data:
                    card = f"{hlink(item.get('title'), item.get('url'))}\n" \
                        f"{hbold('Доступность: ')} {item.get('available')}🔥\n" \
                        f"{hbold('Стоимость: ')} {item.get('price')} рублей💸"
                    await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.mac())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.mac())

    else:
        await bot.send_message(event.from_user.id, 'Упс..Что-то пошло не так.\nПопробуйте снова.')


  