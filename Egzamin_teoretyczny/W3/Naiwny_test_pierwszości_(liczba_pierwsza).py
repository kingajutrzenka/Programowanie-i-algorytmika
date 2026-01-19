#!/usr/bin/env python3

def naiwny_test_pierwszości(n):
	i = 2
	while i * i <= n:
		if n%i == 0:
			return False
		else:
			i += 1
	return True
print(naiwny_test_pierwszości(4))
