from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config import ADMIN_ID

def total_users(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_ID:
        return update.message.reply_text("Unauthorized.")

    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
        count = len(users)
    except FileNotFoundError:
        count = 0

    update.message.reply_text(f"Total users: {count}")

def get_handler():
    return CommandHandler("total", total_users)
