from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from app.core.config import settings
from app.services import zerodha

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your SmartTradeAI bot.')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def get_holdings_command(update: Update, context: CallbackContext) -> None:
    """Get holdings from Zerodha."""
    try:
        kite = zerodha.get_kite()
        holdings = zerodha.get_holdings(kite)
        update.message.reply_text(str(holdings))
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    """Start the bot."""
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("holdings", get_holdings_command))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
