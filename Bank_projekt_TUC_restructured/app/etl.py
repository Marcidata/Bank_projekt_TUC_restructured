import pandas as pd
from .schemas import TransactionIn
from .db import SessionLocal
from .models import Transaction
from sqlalchemy.exc import IntegrityError
from decimal import Decimal

def process_csv(path):
    print(f"Läser CSV: {path}")
    df = pd.read_csv(path)
    processed = []
    session = SessionLocal()
    try:
        for i, row in df.iterrows():
            try:
                tx = TransactionIn(
                    tx_id=str(row.get('tx_id') or f"row-{i}"),
                    from_account=row.get('from_account'),
                    to_account=row.get('to_account'),
                    amount=row.get('amount'),
                    currency=row.get('currency') or "SEK",
                    timestamp=row.get('timestamp')
                )
            except Exception as e:
                print("Valideringsfel för rad", i, e)
                continue

            db_tx = Transaction(
                tx_id=tx.tx_id,
                from_account=tx.from_account,
                to_account=tx.to_account,
                amount=tx.amount,
                currency=tx.currency,
                timestamp=tx.timestamp,
                validated=True
            )
            session.add(db_tx)
            processed.append(tx.tx_id)
        session.commit()
        print("Commit lyckades för", len(processed), "transaktioner")
    except IntegrityError as ie:
        session.rollback()
        print("Integritetsfel, rollback", ie)
    finally:
        session.close()

if __name__ == '__main__':
    print("Testkör ETL lokalt")
