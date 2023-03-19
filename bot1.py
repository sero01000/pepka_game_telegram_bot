import logging
from datetime import datetime
from time import time
from random import randint
from aiogram import Bot, Dispatcher, executor, types
import db1


API_TOKEN = ''
cooldawn = 3600#8 hours
support_message = "@pavel_durov сапорт."

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Говори.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(support_message)

@dp.message_handler(commands=['stats','stat'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    if db1.check_table(chat_id)==[]:
        await message.reply("Ни одного игрока в этом чате.")
    else:
        str_answer="Топ пепок:"
        leaders=db1.get_leaders_by(chat_id)
        for i in leaders:
            str_answer=f"{str_answer}\n{i[1]}: {i[2]}см"
        await message.reply(str_answer)

@dp.message_handler(commands=['d','p'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_link = message.from_user.username
    chat_id = message.chat.id
    if db1.check_table(chat_id)==[]:
        db1.create_table(chat_id)
    user_in_db=db1.get_row(chat_id,user_id)
    if user_in_db==[]:
        dick_resize=randint(-10,10)
        new_dick=dick_resize
        db1.add_user_to_game(chat_id,user_id,user_name,new_dick,int(time()))
    last_time_played=db1.get_row(chat_id,user_id)[0][3]
    if time() > last_time_played:
        dick_resize=randint(-10,10)
        new_dick=db1.get_row(chat_id,user_id)[0][2]+dick_resize
        db1.update_by_user(chat_id,user_id,new_dick,int(time()+cooldawn))

        if new_dick>0:
            dick_type="Пэпка"
            if dick_resize>0:
                bolshe="Увеличилась"
            else:
                bolshe="Увеличилась"
        else:
            dick_type="Ваджина"
            if dick_resize>0:
                bolshe="Затянулась"
            else:
                bolshe="Углубилась"

        await message.reply(f"@{user_link},ваша {dick_type} {bolshe} на {dick_resize}см\nРазмер:{new_dick}см")
    else:
        await message.reply(f"@{user_link},вы сможете поиграть {datetime.fromtimestamp(last_time_played)}.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
