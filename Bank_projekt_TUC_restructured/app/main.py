from app.db import engine, Base
from .models import *
import os

def create_db():
    print("Skapar tabeller om de inte finns")
    Base.metadata.create_all(bind=engine)
    print("Klar")

if __name__ == '__main__':
    create_db()
    print("Kör app - inget aktivt endpoint. Använd scripts i app/ för ETL och workflows.")
