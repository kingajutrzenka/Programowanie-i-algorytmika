#!/usr/bin/env python3

"""Zadanie 1.

Napisz program, który podaną cyfrę wypisze słownie. Skorzystaj ze słownika.

liczba = { 1 : "jeden", 2:"dwa", 3: "trzy"}

print(liczba[3])"""

"""Zadanie 2.

Utwórz słownik zawierający trzy ważne rzeki oraz kraje przez, które one płyną. Para
klucz:wartość może mieć np. wartości ‘Nil’: ‘Egipt’.

a) Wykorzystaj pętle do wyświetlenia zdania o każdej rzece, na przykład: ‘Nil przepływa
przez Egipt’.

b) Wykorzystaj pętlę do wyświetlenia nazw wszystkich rzek przechowywanych w
słowniku.

c) Wykorzystaj pętle do wyświetlenia nazw wszystkich Państw przechowywanych w
słowniku.

d) Poproś użytkownika, aby podał nazwę rzeki. Jeśli tej rzeki nie ma w słowniku, poproś
o podanie kraju i parę tę dopisz do słownika. Wyświetl cały słownik.

rzeki = {"Wisła" : "Polska", "Dunaj" : "Niemcy", "Nil" : "Egipt"}

for i in rzeki:
	print(f"{i} płynie przez {rzeki[i]}")

for i in rzeki:
	print(i)

for i in rzeki:
	print(rzeki[i])

river = input("Podaj nazwę rzeki: ")
if river not in rzeki:
	country = input("Podaj nazwę kraju: ")
	rzeki[river] = country
print(rzeki)"""

"""Zadanie 3.

Wykorzystaj słownik do przechowania ulubionych liczb Twoich znajomych z grupy. Użyj
imion osób jako kluczy. Dla każdej osoby przechowaj w słowniku listę ulubionych liczb.

a) Wyświetl imiona wszystkich osób i ich ulubione liczby.

b) Znajdź liczbę/y najczęściej wybierane najczęściej, jako ulubione

#a

liczby= { "Wera" : [3, 5, 7], "Zosia" : [1, 2, 3, 5], "Osoba_przy_tablicy": [1, 5, 3], "Ja" : [4, 5, 3]}

for i in liczby:
	print(f"Ulubiona liczba osoby : {i} to {liczby[i]}")

# b
lista = []
for i in liczby:
	lista = lista + liczby[i]
print(lista)
liczy = 0
for i in lista:
	if lista.count(i) > liczy:
		liczy = 0
		liczy += lista.count(i)
		liczba = [i]
	elif lista.count(i) == liczy:
		if i not in liczba:
			liczba.append(i)
print(f"Najczęściej wybierane liczby/ liczba to : {liczba}")"""

"""Zadanie 4.

Wykorzystaj słownik do przechowywania informacji o osobie. W słowniku powinny znaleźć
się informacje takie jak: imię, nazwisko, wiek, miasto. Utwórz listę n osób.

a) Wyświetl wszystkie informacje przechowywane w liście słowników (klucze i
wartości).

b) Wyświetl nazwiska osób o wybranym imieniu.

c) Oblicz średni wiek osób.

#a

ludzie = [
    {"imie": "Anna", "nazwisko": "Kowalska", "wiek": 23, "miasto": "Torun"},
    {"imie": "Jan", "nazwisko": "Nowak", "wiek": 30, "miasto": "Warszawa"},
    {"imie": "Maria", "nazwisko": "Wisniewska", "wiek": 27, "miasto": "Gdansk"},
    {"imie": "Piotr", "nazwisko": "Zielinski", "wiek": 35, "miasto": "Poznan"},
    {"imie": "Anna", "nazwisko": "Ząb", "wiek": 40, "miasto": "Wroclaw"},
    {"imie": "Ewa", "nazwisko": "Kaminska", "wiek": 22, "miasto": "Lublin"},
    {"imie": "Tomasz", "nazwisko": "Mazur", "wiek": 29, "miasto": "Krakow"},
    {"imie": "Magdalena", "nazwisko": "Dabrowska", "wiek": 33, "miasto": "Szczecin"},
    {"imie": "Anna", "nazwisko": "Dąb", "wiek": 23, "miasto": "Torun"}]

for i in ludzie:
	if i["imie"] == "Tobiasz":
		print(i["nazwisko"])

wiek = 0
ilość = 0
for k in ludzie:
	wiek += k["wiek"]
	ilość += 1
print(f"średni wiek osób to {(wiek/ilość)}")"""

"""Zadanie 5.

W pliku słowa.txt znajdują się słowa napisane w języku angielskim, po jednym w
każdym wierszu. Utwórz słownik list, w którym w każdej liście będą znajdowały się słowa
zaczynające się od takiej samej litery i wypisz zawartość tego słownika na ekranie. Znajdź i
wypisz na ekranie literę, na którą zaczyna się najwięcej słów. Jeśli jest takich liter więcej,
wypisz wszystkie.

zapis = dict()
with open ("slowa.txt", "r") as slowa:
	for i in slowa:
		i = i.strip()
		if i[0] in zapis:
			zapis[i[0]].append(i)
		else:
			zapis[i[0]] = [i]
	b = ""
	a = 0
	for i in zapis:
		if len(zapis[i]) > a:
			a = len(zapis[i])
			b = i
		elif len(zapis[i]) == a:
			b += i
	print(b)"""
		
"""Zadanie 6. POWTÓRZ!!!!!!!!!!!!!!

W pliku liczby.txt znajdują się liczby całkowite, po jednej w każdym wierszu. Utwórz
słownik list, w którym w każdej liście będą znajdowały się liczby kończące się tą samą cyfrą i
wypisz zawartość tego słownika na ekranie. Znajdź i wypisz na ekranie wszystkie cyfry, na
które nie kończy się żadna liczba.

slownik = dict()
with open("liczby.txt", "r") as lc:
	for linie in lc:
		linie = linie.strip()
		if linie[-1] in slownik:	
			slownik[int(linie[-1])].append(linie)
		else:
			slownik[int(linie[-1])] = [linie]
	print(slownik)
	spr = []
	for k in slownik:
		spr.append(k)
	for i in range(0, 10):
		if i not in spr:
			print(i)"""
			
"""Zadanie 7.

Napisz program do nauki nazw cyfr w języku angielskim (lub innym). Utwórz listę
słowników, po jednym słowniku dla każdej cyfry. W każdym słowniku przyjmij następujące
klucze: ‘cyfra’, ‘angielski’, ‘czy_umiem’ i nadaj im odpowiednie wartości. Początkowa
wartość klucza ‘czy_umiem’ dla wszystkich cyfr powinna być równa ‘nie’. Program powinien
uczyć Cię tak długo, aż podasz wszystkie prawidłowe nazwy cyfr w języku angielskim, czyli
wartość klucza dla wszystkich cyfr będzie równa ‘tak’.

digits = [
    {"cyfra": 0, "angielski": "zero", "czy_umiem": "nie"},
    {"cyfra": 1, "angielski": "one", "czy_umiem": "nie"},
    {"cyfra": 2, "angielski": "two", "czy_umiem": "nie"},
    {"cyfra": 3, "angielski": "three", "czy_umiem": "nie"},
    {"cyfra": 4, "angielski": "four", "czy_umiem": "nie"},
    {"cyfra": 5, "angielski": "five", "czy_umiem": "nie"},
    {"cyfra": 6, "angielski": "six", "czy_umiem": "nie"},
    {"cyfra": 7, "angielski": "seven", "czy_umiem": "nie"},
    {"cyfra": 8, "angielski": "eight", "czy_umiem": "nie"},
    {"cyfra": 9, "angielski": "nine", "czy_umiem": "nie"}
]

def gra():
	print("Zaczynamy naukę cyfr po angielsku!!!")
	for i in digits:
		while i["czy_umiem"] == "nie":
			print(f"Podaj nazwę cyfry {i["cyfra"]} po angielsku")
			liczba = input("Podaj cyfre: ")
			if liczba == i["angielski"]:
				i["czy_umiem"] = "tak"
			else:
				print("Spróbuj jeszcze raz!")
	print("Gratulacje!!")

gra()

def gra():
	ile = 5
	ilew = 4
	print("Zaczynamy naukę cyfr po angielsku!!!")
	while ile != ilew:
		ile = 0
		ilew = 0
		for i in digits:
			if i["czy_umiem"] == "nie":
				print(f"Podaj nazwę cyfry {i["cyfra"]} po angielsku")
				liczba = input("Podaj cyfre: ")
				if liczba == i["angielski"]:
					i["czy_umiem"] = "tak"
					ile += 1
					ilew += 1
				else:
					print("Zła odpowiedź ☠️")
					ilew += 1
	print("Gratulacje!!")

gra()"""

"""Zadanie domowe

Szyfrowanie przez podstawienie to prosta metoda ukrywania znaczenie tekstu: każdy znak tekstu wejściowego zamieniany jest na inny, zgodnie z kluczem.

Przykładowo, tekst 

ala ma kota
zaszyfrowany kluczem

klucz = {' ': '5', 'a': 'Ń','k': '0', 'l': 'ą', 'm': '!', 'o': 'Q', 't': 'e'}
ma postać:

ŃąŃ5!Ń50QeŃ

Twoje zadanie jest następujące: napisz program w języku Python, który umożliwia
odczytanie tekstu zaszyfrowanej wiadomości na podstawie klucza służącego do szyfrowania i
odczytaj jawny tekst podanych wiadomości - cytatów przypisywanych Albertowi Einsteinowi.

wynik = ""
tekst = list("TĘIKJTĘŻŚGA7KNLŹ7IYJŃJŁU7DŚNSF7EGŚNIŚÓINBJ57ŻFEGSJPR7AFLŚ7BJ7WŃGNKPR7TŚIGĆA7JEŃÓ5")
klucz = {'a': 'Ę', 'ą': 'U', 'b': 'Ł', 'c': 'I', 'ć': 'R', 'd': 'E', 'e': 'N', 'ę': 'Ó', 'f': 'C', 'g': 'B', 'h': 'Y', 'i': 'Ś', 'j': 'K', 'k': 'S', 'l': 'Ż', 'ł': 'Z', 'm': 'A', 'n': 'T', 'ń': 'Ą', 'o': 'J', 'ó': 'M', 'p': 'W', 'r': 'Ń', 's': 'L', 'ś': 'P', 't': 'Ź', 'u': 'F', 'w': 'D', 'y': 'Ć', 'z': 'G', 'ź': 'O', 'ż': 'H', '.': '5', ',': '6', '!': '1', '?': '4', ';': '3', '-': '2', ' ': '7', ':': '0'}
lista=[]
for i in tekst:
	for k in klucz:
		if str(i) == klucz[k]:
			wynik += k
print(wynik)"""
			
			

