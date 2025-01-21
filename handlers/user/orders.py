from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import Order


async def process_order(update: Update, context: CallbackContext):
    user = get_user_by_phone(update.message.from_user.phone)
    if not user or not user.cart:
        await update.message.reply_text("سبد خرید شما خالی است یا شما ثبت‌نام نکرده‌اید.")
        return

    total_price = sum([product.price for product in user.cart])
    order = Order(user_id=user.id, total_price=total_price)
    session = Session()
    session.add(order)
    session.commit()
    session.close()

    await update.message.reply_text(
        f"سفارش شما با موفقیت ثبت شد. مبلغ قابل پرداخت: {total_price} IRR. لطفاً فیش پرداختی را ارسال کنید.")
    user.cart.clear()  # پاک‌سازی سبد خرید پس از ثبت سفارش
