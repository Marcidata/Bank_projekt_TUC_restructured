FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt .

# Installera dependencies inklusive streamlit
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Sätt PYTHONPATH
ENV PYTHONPATH=/usr/src/app

# CMD standard: kan ändras vid körning
CMD ["bash", "-c", "streamlit run app_report.py"]
