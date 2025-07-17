number = [13, 80, 8, 59, 82, 35, 40]

angka_maks = number[0]

for i in range(0,len(number)):
	if number[i] > angka_maks:
		angka_maks = number[i]

print(number)
print('Angka terbesar adalah:',angka_maks)
	