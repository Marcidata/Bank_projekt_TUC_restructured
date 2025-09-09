# 🏦 Bank Workflow – Automatiserat Arbetsflöde

Detta projekt automatiserar **validering, bearbetning och lagring av banktransaktioner**.  
Workflow hanteras med **Prefect**, data hanteras med **Pandas**, och rapporter kan visas med **Streamlit**.

---

## 🚀 Funktioner

- ✅ Läsa kund- och transaktionsdata från CSV
- ✅ Validera transaktioner (konton och belopp)
- ✅ Lagra data i databas (PostgreSQL / SQLite)
- ✅ Generera rapporter från CSV och databas
- ✅ Felhantering med rollback vid databasoperationer
- ✅ Automatiserat arbetsflöde med Prefect

---

## 🗂️ Filstruktur

app/ # Applikation
├── workflows/ # Prefect-flöden
├── db.py # Databasanslutning
├── etl.py # ETL-funktioner
├── models.py # Databasmodeller
├── schemas.py # Pydantic-scheman
app_report.py # Streamlit-rapport
Dockerfile # Docker-miljö
requirements.txt # Paketberoenden
tests/ # Testfall
data/ # CSV-data
notebooks/ # Jupyter notebooks
scripts/ # Hjälpskript, t.ex. migration
README.md # Projektbeskrivning


---

## ⚙️ Installation och Snabbstart

### 1️⃣ Klona repo

```bash
git clone https://github.com/angelbra/Projekt-bank_workflow.git
cd Projekt-bank_workflow

2️⃣ Skapa och aktivera Conda-miljö
conda create -n bank_project python=3.12 -y
conda activate bank_project

3️⃣ Installera beroenden
pip install -r requirements.txt

🧰 Köra projektet
#Lokal körning (utan Docker)
1.Sätt PYTHONPATH till projektets root:
export PYTHONPATH=$(pwd)
2.Kör Prefect workflow:
python -m app.workflows.prefect_flow

3.Starta Streamlit-rapport:
streamlit run app_report.py
💡 Om du får portfel på 8501, välj annan port, t.ex.:

streamlit run app_report.py --server.port 8502

4.Testa projektet:
pytest


Docker
1.Bygg Docker-image:
docker build -t bank_workflow:latest .

2.Kör Streamlit via Docker:
docker run -it --rm -p 8501:8501 -e PYTHONPATH=/usr/src/app bank_workflow:latest streamlit run app_report.py
*Om port 8501 redan används, ändra lokalt:

docker run -it --rm -p 8502:8501 -e PYTHONPATH=/usr/src/app bank_workflow:latest streamlit run app_report.py


3.Kör Prefect workflow via Docker:
docker run -it --rm -e PYTHONPATH=/usr/src/app bank_workflow:latest python -m app.workflows.prefect_flow

🧾 Viktig data
Filnamn	Beskrivning
valid_transactions.csv	Alla giltiga transaktioner
invalid_transactions.csv	Ogiltiga transaktioner
transactions_with_valid_flag.csv	Alla transaktioner med giltighetsflagga
accounts.csv	Kundkonton
kunder_utan_account.csv	Kunder utan konto

🔧 Verktyg & Bibliotek
Python 3.12

Pandas – databehandling

NumPy – numeriska beräkningar

Prefect >= 3.15 – workflow management

SQLAlchemy – databas ORM

psycopg2-binary – PostgreSQL-anslutning

Alembic – migrationshantering

Great Expectations – datavalidering

Streamlit – rapporter och visualisering

pytest & pytest-mock – testning

⚠️ Tips
*Streamlit och PYTHONPATH: alltid sätt PYTHONPATH=$(pwd) i projektets root innan du kör streamlit run.

*Portproblem: kontrollera att porten inte redan används:
lsof -i :8501
kill -9 <PID>

*Docker: kör endast en container per port, annars får du "port already allocated".