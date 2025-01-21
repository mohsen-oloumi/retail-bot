from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import Order, Product


async def generate_report(update: Update, context: CallbackContext):
    session = Session()

    total_orders = session.query(Order).count()
    total_sales = session.query(Order).filter(Order.status == "Completed").count()
    total_products = session.query(Product).count()

    report = f"گزارش کلی:\nتعداد سفارشات: {total_orders}\nتعداد فروش‌های تکمیل‌شده: {total_sales}\nتعداد محصولات موجود: {total_products}"

    await update.message.reply_text(report)

    session.close()
