from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import Product, User


async def handle_cart(update: Update, context: CallbackContext):
    message = update.message.text
    user = get_user_by_phone(update.message.from_user.phone)
    if not user:
        await update.message.reply_text("لطفاً ابتدا ثبت‌نام کنید.")
        return

    if message.startswith("/add"):
        product_name = message.split(" ", 1)[1]
        product = Session.query(Product).filter(Product.title == product_name).first()
        if product and product.stock > 0:
            user.cart.append(product)
            await update.message.reply_text(f"محصول {product_name} به سبد خرید شما اضافه شد.")
        else:
            await update.message.reply_text("محصول موجود نیست یا موجودی آن تمام شده است.")

    elif message == "/view_cart":
        if user.cart:
            cart_details = "\n".join([f"{product.title} - {product.price} IRR" for product in user.cart])
            await update.message.reply_text(f"سبد خرید شما:\n{cart_details}")
        else:
            await update.message.reply_text("سبد خرید شما خالی است.")

    elif message == "/checkout":
        total = sum([product.price for product in user.cart])
        await update.message.reply_text(
            f"مجموع سبد خرید شما: {total} IRR. برای نهایی کردن خرید شماره کارت خود را وارد کنید.")
