from telegram import Update
from telegram.ext import CallbackContext


async def update_profile(update: Update, context: CallbackContext):
    await update.message.reply_text("لطفاً اطلاعات جدید پروفایل را وارد کنید.")


