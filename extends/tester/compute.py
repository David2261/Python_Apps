""" Индекс относительной силы - RSI (Relative Strength Index) """
import time
from random import randint

start_time = time.monotonic()

"""
RSI = 100 - [100 / (1 + AU_x / AD_x)]

AU - сумма положительных изменений цены за период
AD - сумма отрицательных изменений цены за период
x - кол-во дней
"""

def RSI(AU: int, AD: int) -> float:
	rsi = 100 - (100 / (1 + (AU / AD)))
	return rsi


if __name__ == '__main__':
	mass = list()
	min_x = 1000000
	max_x = 9999999
	for i in range(10):
		AU = randint(min_x, max_x)
		AD = randint(min_x, max_x)
		mass.insert(i, RSI(AU, AD))
	print(mass)
	print(f"Время прошло: {time.monotonic() - start_time}")
# 0.00026304300263291225
