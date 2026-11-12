# Zadanie 17 – CI/CD pipeline

## Co zrobiłem
Przygotowałem GitHub Actions, który buduje obraz, testuje go i po push na main publikuje do Docker Hub. W repozytorium muszę ustawić sekrety DOCKERHUB_USERNAME i DOCKERHUB_TOKEN.

## Jak uruchamiam
```powershell
docker build -t demo-ci ./backend
docker run --rm demo-ci python -m pytest -q
# Umieszczam katalog zadania jako główny katalog repozytorium GitHub
```

Każdy plik ma komentarze po polsku tam, gdzie pozwala na to składnia. Polecenia wykonuję w katalogu tego zadania.
