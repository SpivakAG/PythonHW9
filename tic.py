from random import randint
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def polePrint(update: Update, context: CallbackContext) -> None:
    for i in range(0, len(pole)):
        update.message.reply_text(f'{pole[i][0]} {pole[i][1]} {pole[i][2]} \n')
        #update.message.reply_text('')

def WinCheck():
    if pole[0][0] == pole[0][1] == pole[0][2] != '_' or pole[0][0] == pole[1][1] == pole[2][2] != '_' or pole[0][0] == pole[1][0] == pole[2][0] != '_' or pole[0][0] == pole[1][0] == pole[2][0] != '_' or pole[0][2] == pole[1][2] == pole[2][2] != '_' or pole[0][0] == pole[1][1] == pole[2][2] != '_' or pole[0][2] == pole[1][1] == pole[2][0] != '_' or pole[2][0] == pole[2][1] == pole[2][2] != '_'or pole[0][0] == pole[1][0] == pole[2][0] != '_' or pole[0][2] == pole[1][2] == pole[2][2] != '_' or pole[0][0] == pole[1][1] == pole[2][2] != '_' or pole[0][2] == pole[1][1] == pole[2][0] != '_' or pole[0][1] == pole[1][1] == pole[2][1] != '_':
        return True
    else:
        return False

def opponent(update: Update, context: CallbackContext) -> None:
    x = randint(0, 2)
    y = randint(0, 2)
    while pole[x][y] != '_':
        x = randint(0, 2)
        y = randint(0, 2)
    update.message.reply_text(f'Противник ходит на {x+1}, {y+1}')
    pole[x][y] = 'O'
    update.message.reply_text('Ход противника принят')

def player(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Введите номер строки')
    x= update.message.text
    update.message.reply_text('Введите номер столбца')
    y= update.message.text
    x -= 1
    y -= 1
    update.message.reply_text(f'Игрок ходит на {x}, {y}')
    while pole[x][y] != '_':
        update.message.reply_text('Поле уже занято, заново введите номер строки')
        x =update.message.text+1
        update.message.reply_text('Введите номер столбца')
        y =update.message.text+1
        update.message.reply_text(f'Игрок ходит на {x}, {y}')
    pole[x][y] = 'X'
    update.message.reply_text('Ход игрока принят')

def draw_check():
    empty=0
    for i in range(0,3):
        for j in range(0,3):
            if pole[i][j]=='_':
                empty=+1
    if empty == 0:
        return True
    else: return False

def game(update: Update, context: CallbackContext) -> None:
    global pole
    pole = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
    count = randint(0, 3)
    update.message.reply_text('Игра начинается')
    if count%2==0:
        update.message.reply_text('Первым ходит игрок')
    else:
        update.message.reply_text('Первым ходит бот')
    polePrint(update, context)

    while WinCheck()!=True:
        if count%2==0:
            player(update, context)
            polePrint(update, context)
            count+=1
            if WinCheck()==True:
                update.message.reply_text('Игра окончена! Победил игрок')
                break
        else:
            opponent(update, context)
            polePrint(update, context)
            count+=1
            if WinCheck()==True:
                update.message.reply_text('Игра окончена! Победил бот')
        if draw_check() ==True:
            update.message.reply_text('Игра окончена, ничья')
            break