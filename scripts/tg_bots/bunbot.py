from telegram.ext import Updater, MessageHandler, Filters


def bun(bot, update):
    bot.kick_chat_member(update.effective_chat.id, update.effective_user.id)


def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, bun))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()