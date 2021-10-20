def main():
	try:
		f1()
	except SomeError:
		log.error("skjfdkfjslkd")
		raise
	try:
		f2()
	except SomeError2:
		pass


if __name__ == "__main__":
	try:
		main()
	except Exception:
		log.error(...)
		mail(...)
		print('hsjkhfks')


# Этот класс позволяет отслеживать все исключения
class TooShortException(Exception):
	pass


def some_func(name):
	if len(name) < 3:
		raise TooShortException('Имя слишком короткое!')

some_func('Ва')

try:
#	z = 1 / 0
	a = []
	print(a[123])
	while True:
		pass


# Прерывание с помощью клавиатуры (к примеру работу сервера)
except KeyboardInterrupt:
	print('Ок, досвидули!')
	exit()


# Исключение из-за деления на 0 / какое-то число
except ZeroDivisionError:
	print('Ай-яй, на 0 делить нельзя, ну ты чтоооо!')


# Исключение любой ошибки (т.е. это функция отлавливает все непредвиденные ошибки)
except Exception:
	print('произошло что-то странное')


# Исключение из-за ошибки синтаксиса
except SyntaxError:
	print('где-то ты допустил ошибку!')


# Ошибка возникает из-за того что где-то используется табы, а где-то пробелы
except TabError:
	print('смесь табов и пробелов')


# Ошибка значения
except ValueError:
	print('Вы допустили ошибку со значением')
