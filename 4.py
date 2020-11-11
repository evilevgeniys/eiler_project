# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
list_of_polindrome = []

def number_of_polindrome():
	for i in range(100, 1000):
		for j in range(100, 1000):
			number = i * j

			if number < 100000:
				list_of_number = list(str(number))
				first_part_number = int(list_of_number[0] + list_of_number[1])
				second_part_number = int(list_of_number[4] + list_of_number[3])

				if first_part_number == second_part_number:
					list_of_polindrome.append(number) 

			elif number >= 100000 and number < 1000000:
				list_of_number = list(str(number))
				first_part_number = int(list_of_number[0] + list_of_number[1] + list_of_number[2])
				second_part_number = int(list_of_number[5] + list_of_number[4] + list_of_number[3])

				if first_part_number == second_part_number:
					list_of_polindrome.append(number)
	# print(list_of_polindrome)
	print(max(list_of_polindrome))

number_of_polindrome()

