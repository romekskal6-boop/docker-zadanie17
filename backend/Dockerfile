# Wybieram obraz Pythona.
FROM python:3.12-slim
# Ustawiam katalog roboczy.
WORKDIR /app
# Kopiuję zależności.
COPY requirements.txt .
# Instaluję biblioteki.
RUN pip install --no-cache-dir -r requirements.txt
# Kopiuję kod aplikacji.
COPY . .
# Dokumentuję port API.
EXPOSE 8000
# Uruchamiam aplikację.
CMD ["python", "app.py"]
