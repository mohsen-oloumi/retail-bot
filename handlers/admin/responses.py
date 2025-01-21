from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import User


async def respond_to_feedback(update: Update, context: CallbackContext):
    message = update.message.text.split(" ", 1)
    if len(message) < 2:
        await update.message.reply_text("لطفاً پیشنهاد یا انتقاد مورد نظر را مشخص کنید.")
        return

    feedback_id = message[0]
    response = message[1]
    session = Session()
    feedback = session.query(User).filter(User.id == feedback_id).first()
    if feedback:
        feedback.response = response
        session.commit()
        await update.message.reply_text("پاسخ شما با موفقیت ارسال شد.")
    else:
        await update.message.reply_text("پیشنهاد یا انتقاد مورد نظر یافت نشد.")
    session.close()
