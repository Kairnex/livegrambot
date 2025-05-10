from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config import ADMIN_ID

def broadcast(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_ID:
        return update.message.reply_text("Unauthorized.")

    message = ' '.join(context.args)
    if not message:
        return update.message.reply_text("Usage: /broadcast <message>")

    try:
        with open("users.txt", "r") as f:
            user_ids = f.read().splitlines()
    except FileNotFoundError:
        return update.message.reply_text("No users found.")

    success = 0
    failed = 0
    for uid in user_ids:
        try:
            context.bot.send_message(chat_id=int(uid), text=message)
            success += 1
        except:
            failed += 1

    update.message.reply_text(f"Broadcast done.\nSuccess: {success}\nFailed: {failed}")

def get_handler():
    return CommandHandler("broadcast", broadcast)
