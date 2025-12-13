#!/usr/bin/env python3

"""Zadanie 2.
Zaimplementuj rekurencyjnie funkcję obliczającą symbol Newtona dla liczb 0 <= k <= n, gdzie:

def N(n,k):
	if k == 0 or k == n:
		return 1
	return N(n-1, k-1) + N(n-1, k)

print(N(6, 4))"""

"""słowa Fibonacciego"""

def Fib(m):
	if m == 0:
		return "b"
	elif m == 1:
		return "a"
	return Fib(m-1) + Fib(m-2)

print(Fib(3))

def Fib1(m):
	if m == 0:
		return "0"
	elif m == 1:
		return "01"
	return Fib1(m-1) + Fib1(m-2)

print(Fib1(3))

f = list(Fib(5))
f.sort()
f1 = list(Fib1(5))
f1.sort()

print(f)
print(f1)

print(f"liczba wystąpień a to: {f.count("a")}")
print(f"liczba wystąpień b to: {f.count("b")}")

print(f"liczba wystąpień 0 to: {f1.count("0")}")
print(f"liczba wystąpień 1 to: {f1.count("1")}")
