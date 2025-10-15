# print("lubie placki, ale tosty nie są złe")
	
# ZADANIE 4

#oficjalne:
a = float(input("Podaj liczbę rzeczywistą: ")) #podaj cyfre
z_licząca = 0  #ustawiamy wartosc która będzie naszym licznikiem odejmowań

if a >= 0: #jesli a jest większe lub równe 0
    while a >= 1: #liczymy ile razy a pomniejszone za każdym razem o 1 da liczbę (0,1)
        a = a - 1 # od a odjmujemy 1 
        z_licząca = z_licząca + 1 #doliczamy 1
    print(f"Podłoga a to: {z_licząca}")
else:      #inaczej (a jest mniejsze od 0)
    while a <= -1: #liczymy ile razy a powiększone za każdym razem o 1 da liczbę (-1, 0)
        a = a + 1 # tu dodajemy, bo dążymy do 0
        z_licząca = z_licząca + 1
    print(f"Podłoga a to: {-z_licząca - 1}") # z_licząca na minusie, bo liczba <0 i odejmujemy 1, bo dno musi być "z tyłu"
