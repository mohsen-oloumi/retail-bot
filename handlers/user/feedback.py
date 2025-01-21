from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import User


async def handle_feedback(update: Update, context: CallbackContext):
    message = update.message.text
    user = get_user_by_phone(update.message.from_user.phone)
    if not user:
        await update.message.reply_text("برای ارسال پیشنهاد یا انتقاد ابتدا ثبت‌نام کنید.")
        return

    feedback = message.split(" ", 1)[1] if len(message.split(" ", 1)) > 1 else None
    if feedback:
        session = Session()
        session.add(feedback)
        session.commit()
        session.close()
        await update.message.reply_text("پیشنهاد یا انتقاد شما با موفقیت ارسال شد. پاسخ به آن به زودی ارسال خواهد شد.")
    else:
        await update.message.reply_text("لطفاً پیشنهاد یا انتقاد خود را وارد کنید.")
