number = [13, 80, 8, 59, 82, 35, 40]

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

	