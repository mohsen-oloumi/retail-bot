from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    CallbackContext
)
from config import TOKEN
from handlers.user.registration import register_user
from handlers.user.profile import update_profile
from handlers.user.cart import handle_cart
from handlers.user.orders import process_order
from handlers.user.feedback import handle_feedback
from handlers.admin.products import manage_products
from handlers.admin.responses import respond_to_feedback
from handlers.admin.reports import generate_report

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("به ربات ما خوش آمدید! لطفاً با ثبت‌نام شروع کنید.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # تعریف دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register_user))
    app.add_handler(CommandHandler("profile", update_profile))
    app.add_handler(CommandHandler("cart", handle_cart))
    app.add_handler(CommandHandler("order", process_order))
    app.add_handler(CommandHandler("feedback", handle_feedback))
    app.add_handler(CommandHandler("manage_products", manage_products))
    app.add_handler(CommandHandler("respond_feedback", respond_to_feedback))
    app.add_handler(CommandHandler("report", generate_report))

    print("ربات راه‌اندازی شد.")
    app.run_polling()

if __name__ == "__main__":
    main()
