#!/usr/bin/env python3

"""Zadanie 1

Zaimplementuj rekurencyjnie funkcję obliczającą silnię liczby n >= 0, gdzie"""

def rek(n):
	if n == 0:
		return 1 # bierze się to ze wzoru na silnie dla 1
	return n * rek(n-1)
print(rek(1)), print(rek(2)), print(rek(0)), print(rek(5))

"""Zadanie 2

Zaimplementuj rekurencyjnie funkcję obliczającą symbol Newtona dla liczb 0 <= k <= n, gdzie"""

def sNewton(n, k):
	if k==0 or k == n:
		return 1
	return sNewton(n-1, k-1) + sNewton(n-1, k)

print(sNewton(5, 1)), print(sNewton(5, 2)), print(sNewton(5, 3)), print(sNewton(5, 4)), print(sNewton(5, 0)), print(sNewton(5, 5))

"""Zadanie 3.

Zaimplementuj rekurencyjnie funkcję obliczającą największy wspólny dzielnik dwóch liczb
a >= 0, b >= 0, gdzie"""

def NWD(a, b):
	if b == 0 and a != 0:
		return a
	elif a == 0 and b != 0:
		return b
	return NWD(b, a%b)

print(NWD(5, 6)), print(NWD(5, 25)), print(NWD(25, 5)), print(NWD(0, 6))

"""Zadanie 4.

Zaimplementuj rekurencyjnie funkcję obliczającą wartość „funkcji 91“ (McCarthy) dla liczby
N >= 0, gdzie"""

def M(n):
	if n>100:
		return n - 10
	return M(M(n + 11))

print(M(5))

"""Zadanie 5.

Zaimplementuj rekurencyjnie funkcję obliczającą funkcję Ackermanna dla dwóch liczb
m >= 0, n>= 0, gdzie:"""

def A(m,n):
	if m == 0:
		return n+1
	elif m> 0 and n == 0:
		return A(m-1, 1)
	else:
		return A(m-1, A(m, n-1))
		
print(A(3,1))

"""Zadanie 6.

Ciąg liczb Fibonacciego to jeden z popularniejszych przykładów funkcji rekurencyjnych."""

# 1. ”klasyczna” definicja

def Fib(m):
  if m == 0:
    return 0
  elif m == 1:
    return 1
  return Fib(m-1) + Fib(m-2)
  
print(Fib(5))

# 2. ciąg Lucasa

def Fib1(m):
  if m == 0:
    return 2
  if m == 1:
    return 1
  return Fib1(m-1) + Fib1(m-2)

print(Fib1(5))

# 3. słowa Fibonacciego

def Fib2(m):
  if m == 0:
    return "b"
  if m == 1:
    return "a"
  return Fib2(m-1) + Fib2(m-2)

print(Fib2(5))

# 4. inna wersja słowa Fibonacciego

def Fib3(m):
  if m == 0:
    return "0"
  if m == 1:
    return "01"
  return Fib3(m-1) + Fib3(m-2)

print(Fib3(5))

""" Zadania: 
- posortuj 25-te słowo Fibonacciego (w każdej z wersji);
- wypisz liczbę wystąpień każdej z liter występującej w 30-tym słowie Fibonacciego (w każdej
z wersji)."""

lista = list(Fib2(5))
lista.sort()
print(lista)
print(lista.count("a"))
print(lista.count("b"))

