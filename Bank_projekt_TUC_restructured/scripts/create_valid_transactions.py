import pandas as pd
import os

try:
    # Definiera sökvägen till in- och utdatafiler
    input_path = os.path.join('data', 'transactions_with_valid_flag.csv')
    output_path = os.path.join('data', 'valid_transactions.csv')

    # Läs in den ursprungliga filen
    df = pd.read_csv(input_path)

    # Filtrera data där 'is_valid' är True
    valid_transactions_df = df[df['is_valid'] == True].copy()

    # Ta bort kolumnen 'is_valid' från de giltiga transaktionerna
    valid_transactions_df.drop('is_valid', axis=1, inplace=True)

    # Spara den nya filen i 'data'-mappen
    valid_transactions_df.to_csv(output_path, index=False)

    print(f"Filen {output_path} har skapats.")
    print("Du hittar den i 'data'-mappen.")

except FileNotFoundError:
    print(f"Ett fel uppstod: Filen '{input_path}' kunde inte hittas. Kontrollera att sökvägen är korrekt.")
except Exception as e:
    print(f"Ett oväntat fel uppstod: {e}")