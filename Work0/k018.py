import random

number=[]

for i in range(100):
	number.append(random.randint(111,999))

angka_maks = number[0]

for i in range(0,len(number)):
	if number[i] > angka_maks:
		angka_maks = number[i]

print(number)
print('Angka terbesar adalah:',angka_maks)
	