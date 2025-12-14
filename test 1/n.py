#!/usr/bin/env python3

"""Marta

n = 157
def lubiana(n):
	o = 0
	n = list(str(n))
	for i in n:
		o += int(i)
	if o < 21:
		return True
	else:
		return False

print(lubiana(189))
print(lubiana(4917))

a=5688
b=6000
for i in range(a, b+1):
	if lubiana(i) == True:
		print(i)"""

"""3

lista = ["ala", "platon", "lizak", "pilka", "tola", "torebka", "beczka", "koszulka"]

def fun(a, b):
	b = dict()
	for i in a:
		i = i.lower()
		if str(i[0])in b:
			b[i[0]] += 1
		else:
			b[i[0]] = 1
	return b
	
def fun2(a):
	for i in a:
		i = i.lower()
		if str(i[0])in slowa:
			slowa[i[0]].append(i)
		else:
			slowa[i[0]] = [i]
	return slowa
with open("tekst.txt", "r") as t:
	t = t.readline()
	t = t.strip().split()
	t = list(t)
	slowa = dict()
	print(fun2(t))
	m = 0
	n = []
	for k in slowa:
		if len(slowa[k]) > m:
			m = len(slowa[k])
			n = [k]
		elif len(slowa[k]) == m:
			n.append(k)
	print(n)
	for s in n:
		for z in slowa[s]:
			print(z)"""
			 
		
	
		
		
	
	
	


		

		
