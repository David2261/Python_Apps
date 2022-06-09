<<<<<<< HEAD
# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "Maybach"
    make = "Mercedez"
    number = "S650"
    model = 2020
    # создаем методы класса
    def start(self):
        print ("Заводим двигатель")
 
    def stop(self):
        print ("Отключаем двигатель")

# Создаем объект класса Car под названием car_a
car_a = Car()
 
# Создаем объект класса Car под названием car_b
car_b = Car()

"""Чтобы узнать тип созданных нами объектов, мы можем использовать метод type и передать ему названия наших объектов."""
print(type(car_b))

"""  Вызываем метод start() через объект car_b"""
car_b.start()

"""В Python, каждый объект содержит определенные атрибуты по умолчанию и методы в дополнение к определенным пользователем атрибутами.
Чтобы посмотреть на все атрибуты и методы объекта, используйте встроенную функцию под названием dir()."""
print(dir(car_b))

"""
Сейчас если вы выведите значение атрибута plane_count, вы увидите 2 в выдаче.
Это связано с тем, что атрибут plane_count является атрибутом класса и таким образом он разделяется между экземплярами.
Объект plane_a увеличил свое значение до 1, в то время как plane_b увеличил свое значение еще раз, так что итоговое значение равняется 2.
"""
class Plane:
    # создаем атрибуты класса
    plane_count = 0
 
    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Plane.plane_count += 1

plane_a = Plane()  
plane_a.start("Boing", "AirBus", 2015)  
print(plane_a.name)  
print(plane_a.plane_count)

plane_b = Plane()  
plane_b.start("City", "Honda", 2013)  
print(plane_b.name)  
print(plane_b.plane_count)


#  Статичные методы

class Car:
 
    @staticmethod
    def get_class_details():
        print ("Это класс Car")
 
Car.get_class_details()


#  Возврат множественных значений из метода


class Square:
 
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b
 
print(Square.get_squares(3, 5))


#  Метод str

class Car:
 
    # создание методов класса
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)

"""
Выдача показывает локацию памяти, где хранится наш объект. Каждый объект Python по умолчанию содержит метод __str__ .
Когда вы используете объект в качестве строки, вызывается метод __str__ , который по умолчанию выводит локацию памяти объекта.
Однако, вы также можете предоставить собственное определение метода __str__ ."""


# создание класса Car

class Car:
 
    # создание методов класса
    def __str__(self):
        return "Car class Object"
 
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)

#  Конструкторы
# Конструктор — это специальный метод, который вызывается по умолчанию когда вы создаете объект класса.

class Car:

    # создание атрибутов класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)

car_a = Car()  
car_b = Car()  
car_c = Car()

#  Локальные переменные против глобальных

# создаем класс Car

class Car:  
    def start(self):
        message = "Двигатель заведен"
        return message
car_a = Car()  
#print(car_a.message) # Это связано с тем, что мы не можем получить доступ к локальной переменной вне блока, где эта локальная переменная была определена


#  Глобальная переменная


# создаем класс Car

class Car:  
    message1 = "Двигатель заведен"
 
    def start(self):
        message2 = "Автомобиль заведен"
        return message2
 
car_a = Car()  
print(car_a.message1)

"""
Атрибуты экземпляра и класса отличаются способом получения доступа к ним.
Другими словами, речь идет об использовании названия класса и использовании названия экземпляра.
С другой стороны, глобальные и локальные переменные отличаются своими областями видимости, другими словами, местами, где к ним может быть получен доступ.
Доступ к локальной переменной может быть получен только внутри метода.
Хотя в этой статье локальные переменные и атрибуты экземпляров определяются внутри метода, локальные переменные определяются собственным ключевым словом.
"""

#  Модификаторы доступа

class Lol:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999

car_a = Lol()
print(car_a.name)

#  Наследование

# Создание класса Vehicle
class Vehicle:  
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")
 
# Создание класса Car, который наследует Vehicle
class Car(Vehicle):  
    def car_method(self):
        print("Это метод из дочернего класса")

car_a = Car()  
car_a.vehicle_method() # Вызываем метод родительского класса

#  Множественное наследование
"""В Python, родительский класс может иметь несколько дочерних, и, аналогично,
дочерний класс может иметь несколько родительских классов"""

# создаем класс Vehicle
class Vehicle:  
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")
 
# создаем класс Car, который наследует Vehicle
class Car(Vehicle):  
    def car_method(self):
        print("Это дочерний метод из класса Car")
 
# создаем класс Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")

car_a = Car()  
car_a.vehicle_method() # вызов метода родительского класса
car_b = Cycle()  
car_b.vehicle_method() # вызов метода родительского класса

"""Вы можете видеть, как родительский класс наследуется двумя дочерними классами.
Таким же образом, дочерний класс может иметь несколько родительских."""


class Camera:  
    def camera_method(self):
        print("Это родительский метод из класса Camera")
 
class Radio:  
    def radio_method(self):
        print("Это родительский метод из класса Radio")
 
class CellPhone(Camera, Radio):  
     def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")

cell_phone_a = CellPhone()  
cell_phone_a.camera_method()  
cell_phone_a.radio_method()

#  Полиморфизм
""" Полиморфизм означает способность объекта вести себя по-разному.
Перегрузка метода относится к свойству метода вести себя по-разному, в зависимости от количества или типа параметров."""

# создаем класс Car
class Car:  
   def start(self, a, b=None):
        if b is not None:
            print (a + b)
        else:
            print (a)


car_a = Car()  
car_a.start(10)  
car_a.start(10, 20)

# Переопределение метода

"""Переопределение метода относится к наличию метода с одинаковым названием в дочернем и родительском классах.
Определение метода отличается в родительском и дочернем классах, но название остается тем же."""

# создание класса Vehicle
class Vehicle:  
    def print_details(self):
        print("Это родительский метод из класса Vehicle")
 
# создание класса, который наследует Vehicle
class Car(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Car")
 
# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Cycle")

car_a = Vehicle()  
car_a. print_details()
 
car_b = Car()  
car_b.print_details()
 
car_c = Cycle()  
car_c.print_details()

#  Инкапсуляция

# Инкапсуляция просто означает скрытие данных.

# создаем класс Car
class Fly:
 
    # создаем конструктор класса FLy
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model
 
    # создаем свойство модели.
    @property
    def model(self):
        return self.__model
 
    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model
 
    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)
 
carA = Fly(2088)  
print(carA.getCarModel())

"""Свойство имеет три части.
Вам нужно определить атрибут, который является моделью в скрипте выше.
Затем, вам нужно определить свойство атрибута, используя декоратор @property.
Наконец, вам нужно создать установщик свойства, который является дескриптором @model.setter в примере выше.
"""
=======
# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "Maybach"
    make = "Mercedez"
    number = "S650"
    model = 2020
    # создаем методы класса
    def start(self):
        print ("Заводим двигатель")
 
    def stop(self):
        print ("Отключаем двигатель")

# Создаем объект класса Car под названием car_a
car_a = Car()
 
# Создаем объект класса Car под названием car_b
car_b = Car()

"""Чтобы узнать тип созданных нами объектов, мы можем использовать метод type и передать ему названия наших объектов."""
print(type(car_b))

"""  Вызываем метод start() через объект car_b"""
car_b.start()

"""В Python, каждый объект содержит определенные атрибуты по умолчанию и методы в дополнение к определенным пользователем атрибутами.
Чтобы посмотреть на все атрибуты и методы объекта, используйте встроенную функцию под названием dir()."""
print(dir(car_b))

"""
Сейчас если вы выведите значение атрибута plane_count, вы увидите 2 в выдаче.
Это связано с тем, что атрибут plane_count является атрибутом класса и таким образом он разделяется между экземплярами.
Объект plane_a увеличил свое значение до 1, в то время как plane_b увеличил свое значение еще раз, так что итоговое значение равняется 2.
"""
class Plane:
    # создаем атрибуты класса
    plane_count = 0
 
    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Plane.plane_count += 1

plane_a = Plane()  
plane_a.start("Boing", "AirBus", 2015)  
print(plane_a.name)  
print(plane_a.plane_count)

plane_b = Plane()  
plane_b.start("City", "Honda", 2013)  
print(plane_b.name)  
print(plane_b.plane_count)


#  Статичные методы

class Car:
 
    @staticmethod
    def get_class_details():
        print ("Это класс Car")
 
Car.get_class_details()


#  Возврат множественных значений из метода


class Square:
 
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b
 
print(Square.get_squares(3, 5))


#  Метод str

class Car:
 
    # создание методов класса
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)

"""
Выдача показывает локацию памяти, где хранится наш объект. Каждый объект Python по умолчанию содержит метод __str__ .
Когда вы используете объект в качестве строки, вызывается метод __str__ , который по умолчанию выводит локацию памяти объекта.
Однако, вы также можете предоставить собственное определение метода __str__ ."""


# создание класса Car

class Car:
 
    # создание методов класса
    def __str__(self):
        return "Car class Object"
 
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)

#  Конструкторы
# Конструктор — это специальный метод, который вызывается по умолчанию когда вы создаете объект класса.

class Car:

    # создание атрибутов класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)

car_a = Car()  
car_b = Car()  
car_c = Car()

#  Локальные переменные против глобальных

# создаем класс Car

class Car:  
    def start(self):
        message = "Двигатель заведен"
        return message
car_a = Car()  
#print(car_a.message) # Это связано с тем, что мы не можем получить доступ к локальной переменной вне блока, где эта локальная переменная была определена


#  Глобальная переменная


# создаем класс Car

class Car:  
    message1 = "Двигатель заведен"
 
    def start(self):
        message2 = "Автомобиль заведен"
        return message2
 
car_a = Car()  
print(car_a.message1)

"""
Атрибуты экземпляра и класса отличаются способом получения доступа к ним.
Другими словами, речь идет об использовании названия класса и использовании названия экземпляра.
С другой стороны, глобальные и локальные переменные отличаются своими областями видимости, другими словами, местами, где к ним может быть получен доступ.
Доступ к локальной переменной может быть получен только внутри метода.
Хотя в этой статье локальные переменные и атрибуты экземпляров определяются внутри метода, локальные переменные определяются собственным ключевым словом.
"""

#  Модификаторы доступа

class Lol:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999

car_a = Lol()
print(car_a.name)

#  Наследование

# Создание класса Vehicle
class Vehicle:  
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")
 
# Создание класса Car, который наследует Vehicle
class Car(Vehicle):  
    def car_method(self):
        print("Это метод из дочернего класса")

car_a = Car()  
car_a.vehicle_method() # Вызываем метод родительского класса

#  Множественное наследование
"""В Python, родительский класс может иметь несколько дочерних, и, аналогично,
дочерний класс может иметь несколько родительских классов"""

# создаем класс Vehicle
class Vehicle:  
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")
 
# создаем класс Car, который наследует Vehicle
class Car(Vehicle):  
    def car_method(self):
        print("Это дочерний метод из класса Car")
 
# создаем класс Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")

car_a = Car()  
car_a.vehicle_method() # вызов метода родительского класса
car_b = Cycle()  
car_b.vehicle_method() # вызов метода родительского класса

"""Вы можете видеть, как родительский класс наследуется двумя дочерними классами.
Таким же образом, дочерний класс может иметь несколько родительских."""


class Camera:  
    def camera_method(self):
        print("Это родительский метод из класса Camera")


class Radio:  
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):  
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")


cell_phone_a = CellPhone()  
cell_phone_a.camera_method()  
cell_phone_a.radio_method()

#  Полиморфизм
""" Полиморфизм означает способность объекта вести себя по-разному.
Перегрузка метода относится к свойству метода вести себя по-разному, в зависимости от количества или типа параметров."""

# создаем класс Car
class Car:  
   def start(self, a, b=None):
        if b is not None:
            print (a + b)
        else:
            print (a)


car_a = Car()  
car_a.start(10)  
car_a.start(10, 20)

# Переопределение метода

"""Переопределение метода относится к наличию метода с одинаковым названием в дочернем и родительском классах.
Определение метода отличается в родительском и дочернем классах, но название остается тем же."""

# создание класса Vehicle
class Vehicle:  
    def print_details(self):
        print("Это родительский метод из класса Vehicle")
 
# создание класса, который наследует Vehicle
class Car(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Car")
 
# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Cycle")

car_a = Vehicle()  
car_a. print_details()
 
car_b = Car()  
car_b.print_details()
 
car_c = Cycle()  
car_c.print_details()

#  Инкапсуляция

# Инкапсуляция просто означает скрытие данных.

# создаем класс Car
class Fly:
 
    # создаем конструктор класса FLy
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model
 
    # создаем свойство модели.
    @property
    def model(self):
        return self.__model
 
    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model
 
    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)
 
carA = Fly(2088)  
print(carA.getCarModel())

"""Свойство имеет три части.
Вам нужно определить атрибут, который является моделью в скрипте выше.
Затем, вам нужно определить свойство атрибута, используя декоратор @property.
Наконец, вам нужно создать установщик свойства, который является дескриптором @model.setter в примере выше.
"""
