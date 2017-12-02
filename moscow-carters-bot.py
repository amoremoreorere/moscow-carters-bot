# -*- coding: utf-8 -*-
import telebot
import requests
from telebot import types
import logging
import os

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', добро пожаловать! Здесь ты можешь подобрать одежду своему малышу.\nКому ищешь? \nЕсли мальчику, то жми /boy. \nЕсли девочке, то жми /girl. \nраспродажа флисовых слипов - /flic \n Хочешь узнать историю бренда Carters, жми /history \nЧтобы узнать о доставке, жми /dostavka \nУзнать о размерах Картер, жми /size_chart \nКоманда /help ознакомит тебя со всеми моими возможностями и командами \nЕсли живешь в Строгино, жми /strogino')

@bot.message_handler(commands=['help'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', я помогу тебе здесь разобраться. Вот команды, которые я знаю: \n \start - чтобы начать выбор одежды  \n/zakaz - чтобы сделать заказ \n/dostavka - узнать о доставке \n/history - узнать историю бренда Картерс \n/size_chart - определить размер одежды малыша')

#этот хендлер удобен в групповом чате, где сидят все и наш бот в том числе.
greeting=["привет", "всем привет", "здравствуйте", "привет!", "хеллоу", "приветики", "Привет", "Привет!"]
@bot.message_handler(func=lambda message: message.text in greeting)
def handle_message(message):
    bot.send_message(message.chat.id, 'Привет! Я робот! Добро пожалось в наш чатик! Чтобы ознакомится с ассортиментом одежды Картерс, жми /start')

@bot.message_handler(commands=['boy'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика!\n'
                                        'Знаешь ли ты размер по размерной сетке Carters? \n'
                                        'Если да, то просто жми на нужный размер. Если нет, то жми /size\n'
                                        '/boy_newborn\n'
                                        '/boy_3m\n'
                                        '/boy_6m\n'
                                        '/boy_9m\n'
                                        '/boy_12m\n'
                                        '/boy_18m\n'
                                        '/boy_24m\n'
                                        '/boy2t\n')

@bot.message_handler(commands=['boy_newborn'])
def default_test(message):
    bot.send_message(message.chat.id, 'К сожалению, сейчас в наличии нет одежды такого маленького размера :( Но не расстраивайся. Ты можешь заказать вещи\n Чтобы узнать об этом подробнее \nжми /zakaz')

@bot.message_handler(commands=['boy_3m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 3m!\n'
    'По размерной сетке Carters - рост 55-61 см, вес 4,1-5,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/115G181_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'этот слип стоит 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G357-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из 4-х вещей - 1150 рублей ')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/2526818-1-300x300.jpeg')
    bot.send_message(message.chat.id, 'Комплект из пяти боди - 1100 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект слюнявчиков - 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/GB13838_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'две пары носков - 300 рублей')

@bot.message_handler(commands=['boy_6m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 6m!\n'
    'По размерной сетке Carters - рост 61-67 см, вес 5,7-7,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G628-240x300.jpg')
    bot.send_message(message.chat.id, 'этот комплект из 4-х вещей стоит 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G583-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из 4-х вещей - 990 рублей ')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/126G262_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G286_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из четырех слюнявчиков - 550 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['boy_9m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 9m!\n'
    'По размерной сетке Carters - рост 67-72 см, вес 7,7-9,5 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/118G965_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'боди стоит 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/243G791_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/115G238_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'слип - 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G326_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/118H003_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'худи - 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118H001_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'худи - 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G289_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G287_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G248_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G333_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G713-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей (из махера) - 990 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['boy_12m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 12m!\n'
    'По размерной сетке Carters - рост 72-78 см, вес 9,5-11,3 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/243G774_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка стоит 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G976_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'боди - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G959_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'боди - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/243G807_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка стоит 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H134_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/121H160_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/121H154_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H698-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G916-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект с тиграми - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/126G262_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/126G534_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H176_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G814_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G592_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G402_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G761_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G753-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/127G214_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект джинсы и рубашка - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G333_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/341G277_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'пижама - 990 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['boy_18m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 18m!\n'
    'По размерной сетке Carters - рост 78-83 см, вес 11,3-12,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/243G521_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом стоит 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H142_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник стоит 750 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/225G790_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'рубашка стоит 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G853-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G916-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H165-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 900 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/121H150_Default-1-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 900 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G346_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 900 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G401_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/121H290_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/249G401_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/249G397_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/248G322_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'джинсы на подтяжках - 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/121H273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из четырех слюнявчиков - 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/121G899_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект из плотного трикотажа с пингвином - 1300 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['boy_24m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на мальчика размера 24m!\n'
    'По размерной сетке Carters - рост 83-86 см, вес 12,7-13,6 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/341G312-240x300.jpg')
    bot.send_message(message.chat.id, 'пижама стоит 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G619_Mint-240x300.jpg')
    bot.send_message(message.chat.id, 'свитшот из флиса - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/225G656_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'рубашка - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/343G072_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'пижама - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H170-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 900 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/127G397_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комлект из трех вещей - 1250 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из четырех слюнявчиков - 550 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

#здесь начинаются команды для одежды для девочки
@bot.message_handler(commands=['girl'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку!\n'
                                        'Знаешь ли ты размер по размерной сетке Carters? \n'
                                        'Если да, то просто жми на нужный размер. Если нет, то жми /size\n'
                                        '/girl_newborn\n'
                                        '/girl_3m\n'
                                        '/girl_6m\n'
                                        '/girl_9m\n'
                                        '/girl_12m\n'
                                        '/girl_18m\n'
                                        '/girl_24m\n'
                                        '/girl2t\n')

@bot.message_handler(commands=['girl_newborn'])
def default_test(message):
    bot.send_message(message.chat.id, 'К сожалению, сейчас в наличии нет одежды такого маленького размера :( Но не расстраивайся. Ты можешь заказать вещи\n Чтобы узнать об этом подробнее \nжми /zakaz')

@bot.message_handler(commands=['girl_3m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 3m!\n'
    'По размерной сетке Carters - рост 55-61 см, вес 4,1-5,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/115G181_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'этот слип стоит 650 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/2526818-1-300x300.jpeg')
    bot.send_message(message.chat.id, 'комплект из пяти боди 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/GB13838_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'две пары носочков стоят 300 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G271_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект слюнявчиков - 700 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_6m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 6m!\n'
    'По размерной сетке Carters - рост 61-67 см, вес 5,7-7,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/119G175_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'этот комплект с зайкой стоит 700  рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G353-240x300.jpg')
    bot.send_message(message.chat.id, 'этот комплект из 4-х вещей стоит 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H275-240x300.jpg')
    bot.send_message(message.chat.id, 'этот комплект стоит 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/c88d1d05f9df1ca36d0d642b50563da1-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G271_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект слюнявчиков - 700 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_9m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочкe размера 9m!\n'
    'По размерной сетке Carters - рост 67-72 см, вес 7,7-9,5 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/258G458_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'леггинсы стоят 450 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/118G997_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'штанишки - 600 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/258G456_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'леггинсы стоят 500 рубле')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118H230_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'боди стоит 600 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G326_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект с барашками 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G260_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G330_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'набор из пяти боди стоит 1100 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G598_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'набор из пяти боди стоит 1100 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G911-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/118G994_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'худи - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H252_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G890-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из шести боди с длинным рукавом стоит 1550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G271_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект слюнявчиков - 700 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_12m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 12m!\n'
    'По размерной сетке Carters - рост 72-78 см, вес 9,5-11,3 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/118G949_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 450 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/258G316_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'леггинсы - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/243G774_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G807_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом - 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G932_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка - 450 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G934_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка - 490 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/258G545_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'леггинсы - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G809_Default-1-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом - 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G959_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'боди - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G867_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/118H058_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'боди - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H105-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G281_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'пижама - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G257_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'пижама - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G276_Default-1-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G843-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/2527655-300x300.jpeg')
    bot.send_message(message.chat.id, 'комплект из трех вещей - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G598_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект из 5 боди - 1150 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G247_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект из 5 боди - 1150 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G759_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект из 5 боди - 1150 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G749-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G246_Default-1-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект из 5 боди - 1150 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G711-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из трех вещей махеровый - 1250 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G266_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект их двух пижам - 1350 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_18m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 18m!\n'
    'По размерной сетке Carters - рост 78-83 см, вес 11,3-12,7 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/258G354_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'леггинсы стоят 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/253G935_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'футболка - 380 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G634_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с длинным рукавом - 450 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/118G956_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/118G949_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/235G758_Default-240x300.jpg')
    bot.send_message(message.chat.id, ' футболка - 450 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/118H093_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'штанишки - 600 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/259G234_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121G766-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/259G333_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/127G178_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'две пары леггинсов - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/121H228_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/121G793_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/259G343_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 850 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H225_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H095_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/121H691-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/259G342-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/259G332_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/121H120_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G169_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект из двух пижам - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/259G337_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G589_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G247_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 1150 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G842-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/11/126G548-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H253_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/127G313_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/121G899_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект из плотного трикотажа с пингвинами - 1250 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/351G245_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект их двух пижам - 1350 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/21837011_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект их двух пижам OshKosh - 1350 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G165_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект их двух пижам OshKosh - 1400 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G271_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект слюнявчиков - 700 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_24m'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 24m!\n'
    'По размерной сетке Carters - рост 83-86 см, вес 12,7-13,6 кг\n Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/22011320_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с коротким рукавом - 490 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/253G792_Mint-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка с коротким рукавом - 490 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/253G795_Navy-240x300.jpg')
    bot.send_message(message.chat.id, 'футболка сдлинным рукавом - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G918_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комбинезон - 600 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/22259013_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'джеггинсы OshKosh - 500 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H230_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'песочник - 700 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G840_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'худи из плотного материала - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G366_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комлпект - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/03/351G161_Default-300x300.jpg')
    bot.send_message(message.chat.id, 'комплект из двух пижам - 1200 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/118G928_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комбинезон - 800 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G631_Default-1-240x300.jpg')
    bot.send_message(message.chat.id, 'худи из флиса - 1350 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/119G186_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'платье - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H288_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'платье - 550 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G331_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из пяти боди - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/126G337_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из 4-х боди с длинным рукавом - 990 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/259G373_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 1050 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H122_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 900 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/121H409_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект - 990 рублей')
    bot.send_photo(message.chat.id, photo='')
    bot.send_message(message.chat.id, 'рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/126G273_Default-240x300.jpg')
    bot.send_message(message.chat.id, 'комплект из четырех слюнявчиков - 550 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['girl_2t'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, тебя интересует одежда на девочку размера 2t!\n'
    'Вот, что есть')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/357G140_Default.jpg')
    bot.send_message(message.chat.id, 'флисовый слип - 1100 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/253G879_Default.jpg')
    bot.send_message(message.chat.id, 'худи - 800 рублей')
    bot.send_message(message.chat.id, 'Если тебе что-нибудь понравилось, тогди жми /zakaz? \n Если ничего не понравилось, можешь ознакомиться со всеми командами, которые я знаю - /help')

@bot.message_handler(commands=['zakaz'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Сделать заказ', url='t.me/missekler'
       )
   )
   bot.send_message(
       message.chat.id,
       'Если вам что-то понравилось, то пишите об этом @missekler. Вы перейдете на страницу чата автоматически, нажав кнопку ниже :)',
       reply_markup=keyboard
   )

@bot.message_handler(commands=['strogino'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Канал для мам из Строгино', url='t.me/strogino_mama_papa'
       )
   )
   bot.send_message(
       message.chat.id,
       'Присоединяйся к каналу для мам из Строгино! Там интересно и весело! И много полезного!',
       reply_markup=keyboard
   )

@bot.message_handler(commands=['history'])
def default_test(message):
    bot.send_message(message.chat.id, 'Эпоха Carter’s начинается в 1865 году в штате Массачюсетс. Да, да, это не опечатка! Уже больше 100 лет назад. Основал ее англичанин по происхождению Вильям Картер. Он успешно развил свой бизнес и до 1990 года компания Carter’s принадлежала его потомкам. Затем ее продали и бренд начал новую историю. Не менее интересна история бренда OshKosh B’Gosh, который присоединился к корпорации Carter’s в 2005 году. А до этого времени это была самостоятельная американская марка, существующая с 1895 года. OshKosh назван в честь одноименного американского города, в котором и зародился этот бренд. Изначально компания занималась одеждой для рабочих, но потом перешла и на детские вещи. Прославился OshKosh благодаря своим комбинезончикам, в которых малыши были похожи на своих пап. Carter’s продолжает покупать ведущие бренды — вот совсем недавно, в феврале 2017 года, корпорация Carter’s приобрела марку Skip Hop.')

@bot.message_handler(commands=['dostavka'])
def default_test(message):
    bot.send_message(message.chat.id, 'Самовывоз - м. Строгино, ул. Таллинская, дом 7, магазин Перекресток \nПо Москве в пределах МКАД работает курьер. Ориентировочные цены: \n курьер до квартиры — 350 рублей \n курьер до метро — 250 рублей \n курьер по Строгино — 150 рублей \n Почта России или другая курьерская служба: \n только после 100% предоплаты')

@bot.message_handler(content_types=["сайт"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на официальный сайт Carters", url="https:carters.com")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на официальный сайт Картерс", reply_markup=keyboard)

@bot.message_handler(content_types=["непонятно", "не понятно", "не понимаю", "непонимаю"])
def default_test(message):
    bot.send_message(message.chat.id, "Если ничего не понятно, жми /help")

@bot.message_handler(content_types=["дура", "сука", "блядь", "хуй"])
def default_test(message):
    bot.send_message(message.chat.id, "Не надо материться!")

@bot.message_handler(content_types=["дура", "сука", "блядь", "хуй"])
def default_test(message):
    bot.send_message(message.chat.id, "Не надо материться!")

@bot.message_handler(content_types=["размер"])
def default_test(message):
    bot.send_message(message.chat.id, "Если не можешь определиться с размером Картерс, жми /size_chart")

@bot.message_handler(commands=['size'])
def default_test(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('до 55 см', '55-61 см', '61-67 см')
    markup.row('67-72 см', '72-78 см ', '78-83 см')
    markup.row('83-86 см', 'выше')
    bot.send_message(message.chat.id, "Какой рост у вашего малыша?", reply_markup=markup)

@bot.message_handler(regexp="55-61 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 3М. \nЧтобы увидеть, что есть на мальчика 3m, жми /boy_3m \nна девочку - жми /girl_3m")

@bot.message_handler(regexp="до 55 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер NB новорожденный. \nЧтобы увидеть, что есть на мальчика NB, жми /boy_newborn \nна девочку - жми /girl_newborn")

@bot.message_handler(regexp="61-67 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 6М. \nЧтобы увидеть, что есть на мальчика 6m, жми /boy_6m \nна девочку - жми /girl_6m")

@bot.message_handler(regexp="67-72 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 9М. \nЧтобы увидеть, что есть на мальчика 9m, жми /boy_9m \nна девочку - жми /girl_9m")

@bot.message_handler(regexp="72-78 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 12М. \nЧтобы увидеть, что есть на мальчика 12m, жми /boy_12m \nна девочку - жми /girl_12m")

@bot.message_handler(regexp="78-83 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 18М. \nЧтобы увидеть, что есть на мальчика 18m, жми /boy_18m \nна девочку - жми /girl_18m")

@bot.message_handler(regexp="выше")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 2Т и выше. \nНа мальчика 2T размера пока нет в наличии,\nна девочку - жми /girl_2t")

@bot.message_handler(regexp="83-86 см")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, "Скорее всего вам нужен размер 24М. \nЧтобы увидеть, что есть на мальчика 24m, жми /boy_24m \nна девочку - жми /girl_24m")

@bot.message_handler(commands=['size_chart'])
def default_test(message):
    bot.send_message(message.chat.id, 'Размерная сетка Carter’s немного отличается от нашей российской. Чаще всего их одежда маломерит, особенно до 24 месяцев. На самом сайте размеры для малышей разделяются так. Сначала идут размеры для совсем маленьких (BABY) — от 0 до 24 месяцев (0-24М). \nЗатем идут размеры для деток постарше, у них они называются TODDLER — от 24 месяцев до 4-х лет (2T-5T) \nИ потом уже идет одежда на детей от 4-х до 8-ми лет (KID). В этом разделе размерная сетка представлена по-разному: для повседневной одежды, для одежды свободного кроя и для верхней.')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/2017-05-14-13-13-47-Item-0.png')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/05/2017-05-14-13-19-51-Item-0-1.png')
    bot.send_message(message.chat.id, 'Ознакомится с ассортиментом: \nна мальчика - жми /boy \n для девочки - жми /girl')

@bot.message_handler(commands=['flic'])
def default_test(message):
    bot.send_message(message.chat.id, 'Итак, перед вами флисовые слипы')
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/91-acbhT3QBamr')
    bot.send_message(message.chat.id, 'флисовый слип американской марки Garanimals с пингвинами \nразмер: 60-66 см, 5,6-7,3 кг \n990 рублей ')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/118G631_Default-1-240x300.jpg')
    bot.send_message(message.chat.id, 'Carter флисовый комбинезон с ушками \nразмер 24М \n1350 рублей')
    bot.send_photo(message.chat.id, photo='http://miss-ekler.ru/wp-content/uploads/2017/04/357G140_Default.jpg')
    bot.send_message(message.chat.id, 'Carter флисовый комбинезон с сердечками \nразмер 2Т \n1350 рублей')
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/lPn734g63QBaRd')
    bot.send_message(message.chat.id, "Child Of Mine By Carter's с машинками \nразмер 61-67 см, 5,7-7,5 кг \n1100 рублей ")
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/0h_rMAmI3QBa65')
    bot.send_message(message.chat.id, "Child Of Mine By Carter's с оленями \nразмеры: \n55-61 см, 4-5,7 кг \n61-67 см, 5,7-7,5 кг \n1100 рублей")
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/ubEUW--d3QBaT9')
    bot.send_message(message.chat.id, "Child Of Mine By Carter's с собачками \nразмер 67-72 см, 7,5-9,3 кг \n61-67 см, 5,7-7,5 кг \n1100 рублей")
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/INI1TVjg3QBa9e')
    bot.send_message(message.chat.id, "Child Of Mine By Carter's с сердечками \nразмер 67-72 см, 7,5-9,3 кг \n61-67 см, 5,7-7,5 кг \n1100 рублей")
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/1ebUWU003QBbB5')
    bot.send_photo(message.chat.id, photo='https://yadi.sk/i/zmwrMEJd3QBbCk')
    bot.send_message(message.chat.id, "Новый велюрово-флисовый новогодний слип от американской марки Little Me без бирки \nразмер 67-72 см, 7,5-9,3 кг \n61-67 см, 5,7-7,5 кг \n950 рублей")



if __name__ == '__main__':
    bot.polling(none_stop=True)
