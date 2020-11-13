# Какое число является 10001-ым простым числом?
#Создаем функцию для поиска простых чисел
import math

def is_prime(num):
	if num < 2:
		return False
	elif num == 2:
		return True
	limit = math.sqrt(num)
	i = 2
	while i <= limit :
		if num%i == 0:
			return False
		i += 1
	return True


def find_prime_number():
	j = 0 #Создадим перемененную для хранения кол-ва найденых простых чисел
	for i in range(999999):
		if is_prime(i):
			j += 1
		if j == 10001:
			print(i)
			break

find_prime_number()