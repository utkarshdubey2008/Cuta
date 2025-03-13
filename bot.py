import telebot

TOKEN = "7763337585:AAHe6Pp3WvpU-bSBpTQgwi3Sg8J_1R-f7Fk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}!")

if __name__ == "__main__":
    bot.polling()
