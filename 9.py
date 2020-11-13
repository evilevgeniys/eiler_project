# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.\

def pythagoras_numbers(number):
	for i in range(0, 1000):
		for j in range(1, 1000):
			for k in range(2, 1000):
				# print(f'i = {i},j = {j}, k = {k}')
				sum_number = i + j + k
				if sum_number == number:
					sum_square = i**2 + j**2
					k_square = k**2
					if sum_square == k_square:
						print(f'a = {i}, b = {j}, c = {k}')
				else:
					print('Решения не обнаружено')
				break
			break	
		break		
					
pythagoras_numbers(1000)
