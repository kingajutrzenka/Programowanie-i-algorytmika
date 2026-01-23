#!/usr/bin/env python3

#własny kod nie z prezentacji, bo po chuj te słowniki

słowo1 = "bark"
słowo2 = "krab"

def anagram(x, y):
	k = 0
	x = list(x)
	y= list(y)
	for i in x:
		if i in y:
			k += 1
			y.remove(i)
	return len(x) == k

print(anagram(słowo1, słowo2))
