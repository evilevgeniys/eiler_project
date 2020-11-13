# Какое число является 10001-ым простым числом?
#Создаем функцию для поиска простых чисел
import math
#Пишем функцию для проверки числа на простоту
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

#Метод нахождения 10001-ого просто числа
def find_prime_number():
	j = 0 #Создадим перемененную для хранения кол-ва найденых простых чисел
	for i in range(999999):
		#Вызов метода проверки числа
		if is_prime(i): # Если метод возвращает true, то число является простым
			j += 1
		# Если переменная j удовлетворяет условию, то выводится значение переменной i, на которой выполнилось условие
		# Это и будет необходимое нам число 
		if j == 10001: 
			print(i)   
			break

find_prime_number()