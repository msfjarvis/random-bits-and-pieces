"""
Module to auto-ban every user who sends a message to a chat
this bot is in.
"""

from telegram.ext import Updater, MessageHandler, Filters


def bun(bot, update):
    """Kicks the member"""
    bot.kick_chat_member(update.effective_chat.id, update.effective_user.id)


def main():
    """The meat and potatoes of all"""
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, bun))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
