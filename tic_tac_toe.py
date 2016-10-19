"""
Witamy ;-)

Twoim zadaniem jest napisanie funkcji,
która na podstawie informacji o planszy
obliczy bieżący stan gry "kółko i krzyżyk".

Nie chcemy stworzyć całej gry!

Napisaną funkcję będzie można wykorzystać do sprawdzania w grze:
  czy gra powinna toczyć się dalej
  czy ktoś wygrał
  czy mamy remis

Powodzenia!
"""


def state(board):
    """Funkcja sprawdzająca stan gry w 'kółko i krzyżyk'.

    Wejście:
      board
        Lista ciągów znaków reprezentujących planszę.
        Dozwolone znaki:
          '.' - niezajęte pole
          'X' - pole zajęte przez gracza X
          'O' - pole zajęte przez gracza O
        Przykład:
          board = [
              'XO.",
              '.0X',
              '.X.',
          ]

    Wyjście:
      '.' jeśli nikt nie wygrywa
      'X' jeśli X wygrywa
      'Y' jeśli Y wygrywa
      'XY' jeśli jest remis

    Zadania dodatkowe:
      Zwróć False jeśli plansza jest niepoprawna.
      Napisz funkcję tak by działała niezależnie od rozmiaru planszy.
    """
