# Importuję testowaną funkcję.
from app import add
# Sprawdzam dodawanie.
def test_add():
    # Weryfikuję oczekiwany wynik.
    assert add(2, 3) == 5
