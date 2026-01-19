#!/usr/bin/env python3

# Palindromy algorytm

t = ['k', 'a', 'j', 'a', 'k']
def sprawdzanie_czy_palindrom(t):
    i = 0
    n = len(t) - 1
    k = n // 2
    while i <= k:
        if t[i] != t[n - i]:
            return False
        i += 1
    return True

print(sprawdzanie_czy_palindrom(t))	
