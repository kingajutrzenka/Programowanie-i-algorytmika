#!/usr/bin/env python3

"""W każdym wierszu pliku dane.txt znajdują się trzy liczby naturalne n, p, k gdzie 2 <= p <= 16 i 2 <= k <= 16, oddzielone spacją. Liczba n jest zapisana w systemie o podstawie p.

Przygotuj program w Pythonie, który dla każdego wiersza danych w pliku dane.txt wypisze na ekran (w nowych liniach) reprezentację liczby n w systemie o podstawie k.

Przykład: plik dane.txt zawiera:
5723 8 16
2019 10 2

wynik:
BD3
11111100011"""

def p_na_dziesietny(n,p):
    n_dec = int(n, p)
    return n_dec
  
def z_dziesietnego_na_k(n_dec):
    if n_dec == 0:
        return "0"

    cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    wynik = " "
    k = int(input("Podaj docelową podstawę k: ")); print()

    while n_dec > 0:
        reszta = n_dec % k
        wynik = cyfry[reszta] + wynik
        n_dec //= k

    return wynik

n = input("Podaj liczbę n: ").strip().upper()
p = int(input("Podaj podstawę p: "))
print(f"Wynik:{z_dziesietnego_na_k(p_na_dziesietny(n,p))}")
