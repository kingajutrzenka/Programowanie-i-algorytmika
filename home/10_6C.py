#!/usr/bin/env python3

"""Zadanie 10.

Zapoznaj się z problemem Flawiusza.

Danych jest n osób ustawionych w kole, ponumerowanych od 1 do n. Dana tez jest liczba
naturalna k. Podaj która osoba pozostanie w wyniku zastosowania wyliczanki o kroku k
poczynając od pierwszej osoby."""

# wersja rekurencyjna

"""k = int(input("podaj liczbę: "))
def J(n):
	if n == 1:
		return 1
	return((J(n-1) + k - 1) % n) + 1

print(J(10))"""

# wersja z zajęć

"""n = 10
k = 3
a = 0
lista = [i for i in range(1,n+1)]
stos =[]
while len(lista) > 1:
	for i in range(1,len(lista)-k):
		lista.pop(i*k - i)
		#print(lista)
		a = i*k - k
	#print(a)
	del stos[::]
	for x in range(a):
		stos.append(lista[x])
	#print(stos)
	del lista[:len(stos)-1]
	lista.extend(stos[:-1])
	print(lista)"""
	
#wersja ze zmianą pozycji

n = 10
k = 3

lista = [i for i in range(1, n+1)]
i = 0
#n = 0
while len(lista) > 1:
	"""n = n + 1
	print(f"Kolejka {n} ")
	print(i)
	print(len(lista))"""
	i = (i + k - 1) % len(lista)
	"""print(i)
	print(len(lista))"""
	lista.pop(i)                  

print(lista)

#!/usr/bin/env python3

"""Zadanie 10.

Zapoznaj się z problemem Flawiusza.

Danych jest n osób ustawionych w kole, ponumerowanych od 1 do n. Dana tez jest liczba
naturalna k. Podaj która osoba pozostanie w wyniku zastosowania wyliczanki o kroku k
poczynając od pierwszej osoby.

# wersja rekurencyjna

k = int(input("podaj liczbę: "))
def J(n):
	if n == 1:
		return 1
	return((J(n-1) + k - 1) % n) + 1

print(J(15))

#wersja ze zmianą pozycji

n = 15
k = 3

lista = [i for i in range(1, n+1)]
i = 0
while len(lista) > 1:
	i = (i + k - 1) % len(lista)
	lista.pop(i)                  

print(lista)"""

"""Zadanie 4.

Napisz funkcję rekurencyjną, która wypisze na ekranie kolejne przedziały liczb rozważane w
rekurencyjnej wersji jednoczesnego szukania minimum i maksimum.

def MinMaxRek(i,j):
  print("Podlista",i,"",j) 
  if i == j: 
    Min,Max=i,j
    print(x[Min],x[Max])  
  else: 
    if i+1 == j: 
      if x[i] >= x[j]:
        Min,Max=j,i
      else:
        Min,Max=i,j
      print(x[Min],x[Max])    
    else:
      k=(i+j) // 2
      min1,max1=MinMaxRek(i,k)
      min2,max2=MinMaxRek(k+1,j)
      if x[min1] <= x[min2]:
        Min=min1
      else:
        Min=min2
      print(x[Min])  
      if x[max1] >= x[max2]:
        Max=max1
      else:
        Max=max2
      print(x[Max])  
  return Min,Max

print("Dane z wykładu")
x=[4,13,3,21,7,15,11,72,2,3]
print(x)
print("Indeksy minimum imaksimum to: ",MinMaxRek(0,len(x)-1))"""

"""Zadanie 5.
Przeanalizuj program realizujący sortowanie przez scalanie. Wypisz na ekranie kolejne etapy
sortowania

def Scal(l,s,p):
  i=l
  j=s+1
  k=l
  while (i<=s) and (j<=p):
    if x[i]<x[j]:
      pom[k]=x[i]
      i=i+1
    else:
      pom[k]=x[j]
      j=j+1
    k=k+1
  while i<=s:
    pom[k]=x[i]
    k=k+1
    i=i+1
  while j<=p:
    pom[k]=x[j]
    j=j+1
    k=k+1
  x[l:p+1]=pom[l:p+1]

def sortowanie_scalanie(pocz,kon):
  if pocz<kon:
    sr = (pocz+kon) // 2
    sortowanie_scalanie(pocz,sr)
    sortowanie_scalanie(sr+1,kon)
    Scal(pocz,sr,kon)
  
x=[40,13,3,21,7,15,11,72,2,3]
temp=len(x)-1
pom=len(x)*[0]
sortowanie_scalanie(0, temp)
print(x)"""

"""Zadanie 6.
Przeanalizuj działanie programu realizującego sortowanie szybkie. Wypisz na ekranie kolejne
etapy sortowania.


def qsort(t, p, k):
    if p >= k: return
    i, j = p, k
    #pivot = t[(p+k)//2]
    pivot=t[k]
    while i <= j:
        while t[i] < pivot: i += 1
        while t[j] > pivot: j -= 1
        if i <= j:
            t[i], t[j] = t[j], t[i]
            i, j = i + 1, j - 1
    qsort(t, p, j)
    qsort(t, i, k)

t=[3,6,7,8,3,4,2,5,2,1,2,3,4,12,2];
start=0
end=len(t)-1
qsort(t, start,end)
print(t)"""

"""Zadanie 7.

Oznaczmy trzy paliki A, B, C dla zagadnienia wierz Hanoi. Przeanalizuj program z funkcją
rekurencyjną, która wypisuje kolejne przełożenia krążków wieży Hanoi, aby całą przełożyć
na inny krążek. Sprawdź działanie programu na wybranej liczbie krążków."""

n = 4
A = 'A'
B = 'B'
C = 'C'
def move_disks(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {B}")
        return
    move_disks(n - 1, A, C, B)
    print(f"Move disk {n} from {A} to {B}")
    move_disks(n - 1, C, B, A)

move_disks(n, A, B, C)
