from aiogram import types, Router, F
from aiogram.utils.markdown import hbold, hlink
from create_bot import bot
from markups import user_markups
from parser.content_data import get_content_iphones

import json
import os
import logging


router = Router()

logger = logging.getLogger(__name__)
log_level = logging.INFO


@router.callback_query(F.data == 'start')       
async def start(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, 'Выберите интересующий каталог:', reply_markup=user_markups.catalogs())

@router.callback_query(F.data == 'back')        
async def back(call: types.CallbackQuery,):
    await bot.answer_callback_query(call.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, 'Выберите интересующий каталог:', reply_markup=user_markups.catalogs())

@router.callback_query(F.data == 'close')        
async def close(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, f"Please, send your suggestions and wishes in {hlink('telegram', 'https://t.me/ToshiroAi')}")

@router.callback_query(F.data == 'iphone')
async def iphone(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, f'Выберите модель📱:', reply_markup=user_markups.iphones())

@router.callback_query(lambda event: event.data.startswith('iphone_'))
async def iphone_models(event: types.callback_query.CallbackQuery):
    value = event.data
    await bot.answer_callback_query(event.id)
    await bot.delete_message(event.from_user.id, event.message.message_id)
    await bot.send_message(event.from_user.id, f'Ориентировочное время сбора данных ⏳1-2 мин.\nПожалуйста, дождитесь завершения..')
    if value == 'iphone_14_pro_max':
        get_content_iphones.iphone_14_pro_max()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())
            

    elif value == 'iphone_14_pro':
        get_content_iphones.iphone_14_pro()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_14_plus':
        get_content_iphones.iphone_14_plus()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_14':
        get_content_iphones.iphone_14()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_13_pro_max':
        get_content_iphones.iphone_13_pro_max()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_13_pro':
        get_content_iphones.iphone_13_pro()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_13':
        get_content_iphones.iphone_13()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_13_mini':
        get_content_iphones.iphone_13_mini()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_12_pro_max':
        get_content_iphones.iphone_12_pro_max()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_12_pro':
        get_content_iphones.iphone_12_pro()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
                
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    
    elif value == 'iphone_12':
        get_content_iphones.iphone_12()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
                
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_12_mini':
        get_content_iphones.iphone_12_mini()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_11_pro_max':
        get_content_iphones.iphone_11_pro_max()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_11_pro':
        get_content_iphones.iphone_11_pro()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_11':
        get_content_iphones.iphone_11()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_se_2020':
        get_content_iphones.iphone_se_2020()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())

    elif value == 'iphone_se_2022':
        get_content_iphones.iphone_se_2022()
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
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())       
            
            except AttributeError:
                for item in data:
                    for i in item:
                        card = f"{hlink(i.get('title'), i.get('url'))}\n" \
                            f"{hbold('Доступность: ')} {i.get('available')}🔥\n" \
                            f"{hbold('Стоимость: ')} {i.get('price')} рублей💸"
                        await bot.send_message(event.from_user.id, card)
                os.remove(f'{value}.json')
                await bot.send_message(event.from_user.id, 'Спасибо за Ваше терпение!\nМожет Вас заинтересует другая модель?☺️', reply_markup=user_markups.iphones())
        else:
            os.remove(f'{value}.json')
            await bot.send_message(event.from_user.id, f'В настоящий момент, все модели {value} распроданы☹️\nВыберите другую модель:', reply_markup=user_markups.iphones())
    else:
        await bot.send_message(event.from_user.id, 'Упс..Что-то пошло не так.\nПопробуйте снова.')

# def register_handlers_user(dp : Dispatcher):
#     dp.register_callback_query_handler(back, Text(startswith='back'))
#     dp.register_callback_query_handler(close, Text(startswith='close'))
#     dp.register_callback_query_handler(iphone, Text(startswith='iphone'))
#     dp.register_callback_query_handler(iphone_models, Text(startswith='iphone_'))
