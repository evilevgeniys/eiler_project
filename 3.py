Рабочий, но очень медленный вариант работы программы  
Пишем функцию проверки числа на простоту
prime_list = []
def if_prime_number(number):
	d = 2
	while d*d <= number and number % d != 0:
		d += 1 
	return d * d > number

def search_prime_number(num):
	for i in range(2, num):
		if num % i == 0:
				if if_prime_number(i):
					prime_list.append(i)
	if not len(prime_list) == 0:
		print (f'Самое большое простое число являющиеся делителем = {prime_list[int(len(prime_list)) - 1]}')
	else:
		print ('Не найдено ни одного простого числа')
