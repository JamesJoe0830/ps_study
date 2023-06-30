# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
English = list(input())


for i in range(N):
	if English[i].islower() :
		English[i] = English[i].upper()
	else:
		English[i] = English[i].lower()
		
print(''.join(English))