import random
number = []

for i in range(100):
	number.append(random.randint(111,999))

angka_ganjil = []
angka_genap = []

for i in range(0,len(number)):
	if number[i] % 2 == 0:
		angka_genap.append(number[i])
	else:
		angka_ganjil.append(number[i])

print(number)
print('Angka ganjil adalah:',angka_ganjil)
print('Angka genap adalah:',angka_genap)

	