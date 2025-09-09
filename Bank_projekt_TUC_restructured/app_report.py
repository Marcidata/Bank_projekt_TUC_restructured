import os
import pandas as pd
import streamlit as st
import great_expectations as gx
from great_expectations.dataset import PandasDataset

# --- Hitta data-mappen ---
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "data")

# --- Läs CSV-filer ---
transactions_file = os.path.join(data_path, "valid_transactions.csv")  # Byt om du vill analysera annan fil
transactions = pd.read_csv(transactions_file)

invalid_file = os.path.join(data_path, "invalid_transactions.csv")
invalid_transactions = pd.read_csv(invalid_file)

accounts_file = os.path.join(data_path, "accounts.csv")
accounts = pd.read_csv(accounts_file)

# --- Streamlit-app ---
st.title("Bank Transaktionsrapport")
st.write("Här kan du se data från olika filer och validera transaktioner.")

# Visa transaktioner
st.subheader("Giltiga transaktioner")
st.dataframe(transactions.head())

st.subheader("Ogiltiga transaktioner")
st.dataframe(invalid_transactions.head())

st.subheader("Konton")
st.dataframe(accounts.head())

# --- Great Expectations validering ---
st.subheader("Validering av transaktioner")

# Skapa en GE-PandasDataset
class TransactionData(PandasDataset):
    pass

tx_data = TransactionData(transactions)

# Exempel på validering: Belopp ska vara större än 0
expectation_result = tx_data.expect_column_values_to_be_between(
    "amount", min_value=0, max_value=1000000  # ändra max efter behov
)

st.write("Valideringsresultat för 'amount' > 0:")
st.json(expectation_result)

# Kontrollera om valideringen gick bra
if expectation_result["success"]:
    st.success("Alla transaktioner är giltiga enligt beloppsregeln ✅")
else:
    st.error("Vissa transaktioner bryter mot beloppsregeln ❌")


