import requests
import telebot
from telebot import types

token = '5150601694:AAGd1pwlMAZxCCLMR9H5QcP-kjIRy-KUESI'
chat_id = '-1001677064857'

bot = telebot.TeleBot(token)

def delete_webhook():
    url = "https://api.telegram.org/bot" + token + "/deleteWebhook"
    response = requests.request("POST", url, headers={}, data={})
    print(response.text)

def fat():
    list_of_result = {'Right':'I got the info', 'Wrong':'This is not what I am looking for'}
    markup = types.InlineKeyboardMarkup()
    for key, value in list_of_result.items():
        markup.add(types.InlineKeyboardButton(text=value, callback_data=key))

    return markup

def milk():
    list_of_result = {'Question1':'Can I drink milk?', 'Question2':'Facts about milk!'}
    markup = types.InlineKeyboardMarkup()
    for key, value in list_of_result.items():
        markup.add(types.InlineKeyboardButton(text=value, callback_data=key))

    return markup

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(chat_id = message.chat.id, text="Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if ('milk' in message.text):
        bot.send_message(chat_id = message.chat.id, text="Select one", reply_markup=milk(), parse_mode="HTML")
    if ('fat' in message.text):
        bot.send_message(chat_id = message.chat.id, text="A small amount of fat is an essential part of a healthy, balanced diet. Fat is a source of essential fatty acids, which the body cannot make itself. Fat helps the body absorb vitamin A, vitamin D and vitamin E. These vitamins are fat-soluble, which means they can only be absorbed with the help of fats.", reply_markup=fat(), parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if (call.data == 'Right'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Thank you!")
    if (call.data == 'Wrong'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="We will contact you shortly!")
    if (call.data == 'Question1'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Yes")
    if (call.data == 'Question2'):
        bot.send_message(chat_id = chat_id, text="Is drinking milk good for you?\nImage result for milk\nIt's packed with important nutrients like calcium, phosphorus, B vitamins, potassium and vitamin D. Plus, it's an excellent source of protein. Drinking milk and dairy products may prevent osteoporosis and bone fractures and even help you maintain a healthy weight.", parse_mode="HTML")

delete_webhook()
bot.infinity_polling()