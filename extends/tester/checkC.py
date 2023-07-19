import time
from random import randint
from API_RSI import RSI

start_time = time.monotonic()


if __name__ == '__main__':
	mass = list()
	min_x = 1000000
	max_x = 9999999
	for i in range(10):
		AU = float(randint(min_x, max_x))
		AD = float(randint(min_x, max_x))
		mass.insert(i, RSI(AU, AD))
	print(mass)
	print(f"Время прошло: {time.monotonic() - start_time}")
# 0.00026304300263291225
