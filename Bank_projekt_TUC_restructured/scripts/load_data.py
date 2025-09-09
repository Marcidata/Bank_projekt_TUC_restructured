import os
import csv
from sqlalchemy import create_engine, text

# Använd DATABASE_URL från miljövariabler om den finns, annars fallback
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg2://bankuser:bankpass@localhost:5432/bankdb"
)
engine = create_engine(DATABASE_URL)

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "valid_transactions.csv")

def main():
    if not os.path.exists(CSV_PATH):
        raise SystemExit(f"CSV-fil saknas: {CSV_PATH}")

    with engine.begin() as conn:
        with open(CSV_PATH, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sql = text("""
                    INSERT INTO transactions (tx_id, timestamp, amount, currency, from_account, to_account)
                    VALUES (:tx_id, :timestamp, :amount, :currency, :from_account, :to_account)
                    ON CONFLICT (tx_id) DO NOTHING
                """)
                conn.execute(sql, {
                    "tx_id": row.get("transaction_id"),
                    "timestamp": row.get("timestamp"),
                    "amount": row.get("amount"),
                    "currency": row.get("currency"),
                    "from_account": row.get("sender_account"),
                    "to_account": row.get("receiver_account"),
                })
    print("Data loaded successfully.")

if __name__ == "__main__":
    main()

