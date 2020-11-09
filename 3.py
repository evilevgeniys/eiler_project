# Пишем функцию проверки числа на простоту
prime_list = []
def if_prime_number(number):
	d = 2
	while d*d <= number and number % d != 0:
		d += 1 
	return d * d > number

#пишем функцию поиска делителей
def search_prime_number(num):
	for i in range(2, num):
		if num % i == 0:
			if if_prime_number(i):
				prime_list.append(i)
	return prime_list[len(prime_list) - 1]

				

print(search_prime_number(600851475143))
			
