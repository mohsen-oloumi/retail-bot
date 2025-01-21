from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import add_user

async def register_user(update: Update, context: CallbackContext):
    message = update.message.text
    parts = message.split(" ")
    if len(parts) < 4:
        await update.message.reply_text("لطفاً اطلاعات کامل (نام، نام خانوادگی، شماره موبایل) را وارد کنید.")
        return

    first_name, last_name, phone = parts[1:4]
    referral_code = parts[4] if len(parts) > 4 else None
    add_user(first_name, last_name, phone, referral_code)
    await update.message.reply_text("ثبت‌نام با موفقیت انجام شد!")
