#!/usr/bin/env python3

def sortowanie_przez_scalanie(tablica):
    # Warunek zakończenia rekurencji - tablica z 1 elementem jest już posortowana
    if len(tablica) <= 1:
        return tablica
    
    # Znajdujemy środek tablicy
    srodek = len(tablica) // 2
    
    # Dzielimy tablicę na lewą i prawą część
    lewa_czesc = tablica[:srodek]
    prawa_czesc = tablica[srodek:]
    
    # Rekurencyjnie sortujemy obie części
    posortowana_lewa = sortowanie_przez_scalanie(lewa_czesc)
    posortowana_prawa = sortowanie_przez_scalanie(prawa_czesc)
    
    # Scalamy posortowane części
    return scalanie(posortowana_lewa, posortowana_prawa)


def scalanie(lewa, prawa):
    # Tablica wynikowa na scalone elementy
    wynik = []
    
    # Indeksy do przechodzenia przez lewą i prawą tablicę
    indeks_lewy = 0
    indeks_prawy = 0
    
    # Porównujemy elementy z obu tablic i dodajemy mniejszy do wyniku
    while indeks_lewy < len(lewa) and indeks_prawy < len(prawa):
        if lewa[indeks_lewy] <= prawa[indeks_prawy]:
            wynik.append(lewa[indeks_lewy])
            indeks_lewy += 1
        else:
            wynik.append(prawa[indeks_prawy])
            indeks_prawy += 1
    
    # Dodajemy pozostałe elementy z lewej tablicy (jeśli jakieś zostały)
    while indeks_lewy < len(lewa):
        wynik.append(lewa[indeks_lewy])
        indeks_lewy += 1
    
    # Dodajemy pozostałe elementy z prawej tablicy (jeśli jakieś zostały)
    while indeks_prawy < len(prawa):
        wynik.append(prawa[indeks_prawy])
        indeks_prawy += 1
    
    return wynik


# Przykład użycia
liczby = [64, 34, 25, 12, 22, 11, 90]
print("Przed sortowaniem:", liczby)

posortowane_liczby = sortowanie_przez_scalanie(liczby)
print("Po sortowaniu:", posortowane_liczby)
