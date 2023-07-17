import datetime
from typing import (
	Any,
	Tuple,
	Union)
from dataclasses import dataclass

import numpy as np


@dataclass
class User:
	username: str
	created_at: datetime.datetime
	birthday: datetime.datetime | None = None


def validate_user_on_server(_):
	pass


def check_username(_):
	pass


def check_birthday(_):
	pass


def validate_user(user: User):
	""" Проверяет юзера, показывает исключения, если с ним что-то не так """
	validate_user_on_server(user)
	check_username(user)
	check_birthday(user)


# радиус рабочей плоскости
radius: int = 8
# приращение аргумента для производной
global_epsilon: float = 0.000000001
# центр рабочего круга
centre: Tuple[float, float] = (global_epsilon, global_epsilon)
# количество обработанных баллов / 360
arr_shape: int = 100
# шаг между двумя точками
step: float = radius / arr_shape


def differentiable_function(
		x: Union[int, float],
		y: Union[int, float]) -> Any:
	return np.sin(x) * np.exp((1 - np.cos(y)) ** 2)\
		+ np.cos(y) * np.exp((1 - np.sin(x)) ** 2) + (x - y) ** 2


def rotate_vector(length: Union[int, float], a: Union[int, float]) -> Any:
	return length * np.cos(a), length * np.sin(a)


def derivative_x(epsilon: Union[int, float], arg: Union[int, float]) -> Any:
	return (differentiable_function(global_epsilon + epsilon, arg) -
			differentiable_function(epsilon, arg)) / global_epsilon


def derivative_y(epsilon: Union[int, float], arg: Union[int, float]) -> Any:
	return (differentiable_function(arg, epsilon + global_epsilon) -
			differentiable_function(arg, epsilon)) / global_epsilon


def calculate_flip_points() -> Any:
	flip_points = np.array([0, 0])
	points = np.zeros((360, arr_shape), dtype=bool)
	cx, cy = centre

	for i in range(arr_shape):
		for alpha in range(360):
			x, y = rotate_vector(step, alpha)
			x = x * i + cx
			y = y * i + cy
			points[alpha][i] = derivative_x(x, y) + derivative_y(y, x) > 0
			if not points[alpha][i - 1] and points[alpha][i]:
				flip_points = np.vstack((flip_points, np.array([alpha, i - 1])))

	return flip_points


def pick_estimates(positions):
	vx, vy = rotate_vector(step, positions[1][0])
	cx, cy = centre
	best_x, best_y = cx + vx * positions[1][1], cy + vy * positions[1][1]

	for index in range(2, len(positions)):
		vx, vy = rotate_vector(step, positions[index][0])
		x, y = cx + vx * positions[index][1], cy + vy * positions[index][1]
		if differentiable_function(best_x, best_y) > differentiable_function(x, y):
			best_x = x
			best_y = y

	for index in range(360):
		vx, vy = rotate_vector(step, index)
		x, y = cx + vx * (arr_shape - 1), cy + vy * (arr_shape - 1)
		if differentiable_function(best_x, best_y) > differentiable_function(x, y):
			best_x = x
			best_y = y

	return best_x, best_y


def gradient_descent(best_estimates, is_x: Union[int, float]):
	derivative = derivative_x if is_x else derivative_y
	best_x, best_y = best_estimates
	descent_step = step
	value = derivative(best_y, best_x)

	while abs(value) > global_epsilon:
		descent_step *= 0.95
		best_y = best_y - descent_step \
			if derivative(best_y, best_x) > 0 else best_y + descent_step
		value = derivative(best_y, best_x)

	return best_y, best_x


def find_minimum():
	return gradient_descent(
		gradient_descent(
			pick_estimates(
				calculate_flip_points()), False), True)


def get_grid(grid_step):
	samples = np.arange(-radius, radius, grid_step)
	x, y = np.meshgrid(samples, samples)
	return x, y, differentiable_function(x, y)


if __name__ == '__main__':
	min_x, min_y = find_minimum()
	minimum = (min_x, min_y, differentiable_function(min_x, min_y))
	x, y, z = get_grid(0.05)
	print(f'Minimum: {minimum}\nx: {x}\ny: {y}\nz: {z}')
