with open('table.txt', 'w') as file:
	for j in range(2, 21):
		i = [j*n for n in range(11)]
		for t in i:
			if t == 0:
				t = str(f'\n{t}')
			t = f'{t}\n'
			file.write(t)

