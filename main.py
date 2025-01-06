
import telebot
import os

# قراءة التوكن من متغير البيئة
BOT_TOKEN = os.getenv('BOT_TOKEN')

# التأكد من وجود التوكن
if not BOT_TOKEN:
    raise ValueError("لم يتم العثور على التوكن في متغيرات البيئة!")

# إنشاء كائن البوت
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أنا بوت Telegram بسيط.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# تشغيل البوت
bot.polling()
