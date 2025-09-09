import os
from app.db import engine, SessionLocal
from app.main import create_db
from app.etl import process_csv
from app.models import Transaction

def test_create_and_etl():
    print("Kör test_create_and_etl")
    create_db()
    import pandas as pd
    df = pd.DataFrame([{
        'tx_id': 't_test_1',
        'from_account': '12345',
        'to_account': '54321',
        'amount': 100,
        'currency': 'SEK'
    }])
    tmp = 'data/test_transactions.csv'
    df.to_csv(tmp, index=False)
    process_csv(tmp)
    session = SessionLocal()
    tx = session.query(Transaction).filter_by(tx_id='t_test_1').first()
    assert tx is not None
    session.close()
    print("Test klar")
