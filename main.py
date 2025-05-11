import time
import telebot
from flask import Flask, jsonify, request
from settings import config
from llm import ai

bot = telebot.TeleBot(config.TELEGRAM_TOKEN, threaded = False, skip_pending = True)
webhook_info = bot.get_webhook_info()
if webhook_info.url != config.WEBHOOK_URL:
    bot.remove_webhook()
    time.sleep(1)  # brief pause to avoid 429
    bot.set_webhook(url=config.WEBHOOK_URL)

app = Flask(__name__)

@app.route('/'+config.SECRET, methods=['POST'])
def webhook():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@bot.message_handler(commands = ['start'])
def start(m):
    if m.from_user.id not in config.ALLOWED_USERS:
        bot.send_message(m.chat.id, f"Access denied. Your id is: {m.from_user.id}")
        return
    bot.send_message(m.chat.id, 'Hello, welcome to test')

@bot.message_handler(commands = ['help'])
def help(m):
    if m.from_user.id not in config.ALLOWED_USERS:
        bot.send_message(m.chat.id, f"Access denied. Your id is: {m.from_user.id}")
        return
    bot.send_message(m.chat.id, 'Contact admin.')

@bot.message_handler(content_types = ['text'])
def echo(m):
    if m.from_user.id not in config.ALLOWED_USERS:
        bot.send_message(m.chat.id, f"Access denied. Your id is: {m.from_user.id}")
        return
    res = ai.chat(m.text)
    bot.send_message(m.chat.id, res)

@bot.message_handler(content_types = ['photo'])
def photo(m):
    if m.from_user.id not in config.ALLOWED_USERS:
        bot.send_message(m.chat.id, f"Access denied. Your id is: {m.from_user.id}")
        return
    bot.send_message(m.chat.id, 'Nice photo!')


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Server is running."})



if __name__ == '__main__':
    app.run(
        host=config.BIND_HOST,
        port=config.BIND_PORT,
        debug=True,
    )
