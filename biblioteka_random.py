#!/usr/bin/env python3

# Testuje bibliotekę random

import random

print(random.random())

print(random.randrange(5))

print(random.randrange(6, 9))

a = 0
b = 1
o = 0
while a != b:
	a = random.randrange(-500, 100000)
	b = random.randrange(100000)
	o += 1
print(a)
print(b)
print(o)

print(random.randint(-5, 10))

print(random.uniform(5, 1))

lista = list(range(1, 100))

print(random.choice(lista))
	
random.shuffle(lista)

print(lista)
