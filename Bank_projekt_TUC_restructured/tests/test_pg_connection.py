import psycopg2

try:
    conn = psycopg2.connect(
        dbname="bankdb",
        user="bankuser",
        password="bankpass",
        host="localhost",
        port=5432
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
