#!/usr/bin/env python3

def Fibonacci_rekurencyjnie(n):
	if n==1 or n==2:
		return 1
	return Fibonacci_rekurencyjnie(n-1) + Fibonacci_rekurencyjnie(n-2)
	
print(Fibonacci_rekurencyjnie(100))
