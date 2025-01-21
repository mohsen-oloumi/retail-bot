from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import Session
from database.models import Product


async def manage_products(update: Update, context: CallbackContext):
    message = update.message.text.split(" ", 1)
    if len(message) < 2:
        await update.message.reply_text("لطفاً دستور مورد نظر خود را وارد کنید.")
        return

    command = message[0].lower()
    data = message[1]

    session = Session()

    if command == "add":
        title, price, stock = data.split(", ")
        price, stock = float(price), int(stock)
        product = Product(title=title, price=price, stock=stock, unit="کیلو")
        session.add(product)
        session.commit()
        await update.message.reply_text(f"محصول {title} با قیمت {price} و موجودی {stock} اضافه شد.")

    elif command == "update":
        product_name, price, stock = data.split(", ")
        product = session.query(Product).filter(Product.title == product_name).first()
        if product:
            product.price = float(price)
            product.stock = int(stock)
            session.commit()
            await update.message.reply_text(f"محصول {product_name} به‌روز شد.")
        else:
            await update.message.reply_text(f"محصول {product_name} یافت نشد.")

    elif command == "remove":
        product_name = data
        product = session.query(Product).filter(Product.title == product_name).first()
        if product:
            session.delete(product)
            session.commit()
            await update.message.reply_text(f"محصول {product_name} حذف شد.")
        else:
            await update.message.reply_text(f"محصول {product_name} یافت نشد.")

    session.close()
