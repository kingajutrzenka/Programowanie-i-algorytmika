#!/usr/bin/env python3

#Algorytm sprawdzający procent zgodności DNA (podobieństwo organizmów)

DNA1="ACGCCGATTACGTTACGTTTAACCT"
DNA2="ACGTCGAATGCGTTGCATTATCCAT"
n=25

i = 0
inne = 0

while i < n:
	if DNA1[i] != DNA2[i]:
		inne += 1
	i += 1

print(inne)
print((n-inne)*100/n)

