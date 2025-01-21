from database.models import Product
from database.db_manager import Session

def seed_products():
    session = Session()
    products = [
        Product(title="عسل طبیعی", price=500000, stock=100, unit="کیلو"),
        Product(title="برنج ایرانی", price=1200000, stock=50, unit="کیلو")
    ]
    session.add_all(products)
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_products()
