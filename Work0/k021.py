nilai = int(input('Masukkan nilai: '))

if nilai <= 50:
	print('Perlu mengulang')
elif 51 <= nilai and nilai <= 60:
	print('Cukup')
elif 61 <= nilai and nilai <= 90:
	print('Baik')  
else:
	print('Baik Sekali')