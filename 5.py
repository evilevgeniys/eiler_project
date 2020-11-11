# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
#необходимо использовать правило НОК 

from math import gcd

def lcm():

	number = 1 
	for i in range(2, 21):
		result_lcm = (number * i) // gcd(number, i)
		number = result_lcm
	return number

print(lcm())