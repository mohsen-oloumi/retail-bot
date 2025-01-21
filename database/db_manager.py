from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base, User, Product, Order

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_user(first_name, last_name, phone, referral_code=None):
    session = Session()
    user = User(first_name=first_name, last_name=last_name, phone=phone, referral_code=referral_code)
    session.add(user)
    session.commit()
    session.close()

def get_user_by_phone(phone):
    session = Session()
    user = session.query(User).filter_by(phone=phone).first()
    session.close()
    return user
