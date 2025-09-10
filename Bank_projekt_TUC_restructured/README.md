🏦 Bank Workflow – Automatiserat Arbetsflöde
Detta projekt automatiserar validering, bearbetning och lagring av banktransaktioner.
Workflow hanteras med Prefect, data hanteras med Pandas, och rapporter kan visas med Streamlit.

🚀 Funktioner
✅ Läsa kund- och transaktionsdata från CSV

✅ Validera transaktioner (konton och belopp)

✅ Lagra data i databas (PostgreSQL / SQLite)

✅ Generera rapporter från CSV och databas

✅ Felhantering med rollback vid databasoperationer

✅ Automatiserat arbetsflöde med Prefect

🗂️ Filstruktur
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
scripts/ # Hjälpskript, t.ex. för migrering och databearbetning
notebooks/ # Jupyter notebooks
README.md # Projektbeskrivning


⚙️ Installation och Snabbstart

1️⃣ Klona repot
git clone https://github.com/Marcidata/Bank_projekt_TUC_restructured.git
cd Projekt-bank_workflow


2️⃣ Skapa och aktivera Conda-miljö
conda create -n bank_project python=3.12 -y
conda activate bank_project


3️⃣ Installera beroenden
pip install -r requirements.txt


🧰 Köra projektet / Lokal körning (utan Docker)

1.Förbered databasen:
Se till att din databasanslutning är korrekt inställd i alembic.ini. Kör sedan:
alembic upgrade head


2.Förbered data:
python scripts/create_valid_transactions.py


3.Kör arbetsflödet:
export PYTHONPATH=$(pwd)
python -m app.workflows.prefect_flow


4.Starta rapporten:
streamlit run app_report.py


Docker

1.Bygg Docker-image:
docker build -t bank_workflow:latest .


2.Kör arbetsflödet:
docker run -it --rm -e PYTHONPATH=/usr/src/app bank_workflow:latest python -m app.workflows.prefect_flow


3.Kör rapporten:
docker run -it --rm -p 8501:8501 -e PYTHONPATH=/usr/src/app bank_workflow:latest streamlit run app_report.py

🔧 Verktyg & Bibliotek
Bibliotek	Beskrivning
Python 3.12	Programmeringsspråk.
Pandas	Databehandling och analys.
NumPy	Numeriska beräkningar.
Prefect >= 3.15	Workflow management.
SQLAlchemy	Databas ORM (Object-Relational Mapper).
psycopg2-binary	PostgreSQL-anslutning.
Alembic	Migrationshantering för databaser.
Great Expectations	Datavalidering.
Streamlit	Rapporter och visualisering.
pytest & pytest-mock	Testning.